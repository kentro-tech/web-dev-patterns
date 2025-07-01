import os
import mux_python
import air
from functools import wraps
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"))
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Mux with single client
mux_client = mux_python.ApiClient(
    mux_python.Configuration(
        username=os.getenv("MUX_TOKEN_ID"),
        password=os.getenv("MUX_TOKEN_SECRET")
    )
)
live_api = mux_python.LiveStreamsApi(mux_client)
direct_uploads_api = mux_python.DirectUploadsApi(mux_client)
assets_api = mux_python.AssetsApi(mux_client)

# In-memory storage
streams = {}
videos = {}
uploads = {}


# Helper functions
def page(title: str, *body):
    """Create a standard page with common structure"""
    return air.Html(
        air.Head(
            air.Title(title),
            air.Script(src="https://cdn.jsdelivr.net/npm/hls.js@latest"),
            air.Script(src="/static/player.js")
        ),
        air.Body(*body)
    )


def with_back_link(*content, href="/"):
    """Add a back link to content"""
    return (*content, air.Hr(), air.A("Back", href=href))


def get_user_email(request: Request):
    """Get email from session"""
    return request.session.get("email")


def require_auth(func):
    """Decorator to require authentication"""
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        if not get_user_email(request):
            return RedirectResponse("/login", status_code=303)
        return await func(request, *args, **kwargs)
    return wrapper


def get_resource_or_404(resource_dict, resource_id):
    """Get resource from dict or raise 404"""
    if resource_id not in resource_dict:
        raise HTTPException(status_code=404)
    return resource_dict[resource_id]


def simple_form(action: str, button_text: str, *inputs):
    """Create a simple form with common structure"""
    return air.Form(
        *inputs,
        air.Button(button_text, type="submit"),
        action=action,
        method="post"
    )


def video_player(playback_id: str, video_id: str = "video-player", autoplay: bool = False):
    """Create a video player element"""
    return air.Video(
        id=video_id,
        src=f"https://stream.mux.com/{playback_id}.m3u8",
        controls=True,
        style="width: 100%; max-width: 800px;",
        autoplay=autoplay,
        muted=autoplay  # Muted if autoplay to comply with browser policies
    )


def stream_list_item(stream_id: str, stream: dict):
    """Create a list item for a stream"""
    return air.Li(
        air.A(stream["title"], href=f"/live/{stream_id}"),
        f" - Status: {stream['status']}"
    )


def video_list_item(asset_id: str, video: dict):
    """Create a list item for a video"""
    return air.Li(
        air.A(video["title"], href=f"/video/{asset_id}"),
        f" - by {video['uploader']}"
    )


# Routes
@app.get("/", response_class=air.TagResponse)
async def index(request: Request):
    email = get_user_email(request)
    
    return page("Mux Example",
        air.H1("Mux Live Streaming & Video"),
        air.P(f"Logged in as: {email}" if email else "Not logged in"),
        air.Hr(),
        air.H2("Features"),
        air.Ul(
            air.Li(air.A("Live Streaming", href="/live")),
            air.Li(air.A("Video Upload", href="/upload")),
            air.Li(air.A("Browse Videos", href="/videos"))
        ),
        air.Hr(),
        air.A("Login", href="/login") if not email else air.A("Logout", href="/logout")
    )


@app.get("/login", response_class=air.TagResponse)
async def login_form():
    return page("Login",
        air.H1("Login"),
        simple_form("/login", "Login",
            air.Input(type="email", name="email", placeholder="email@example.com", required=True)
        )
    )


@app.post("/login")
async def login(request: Request, email: str = Form()):
    request.session["email"] = email
    return RedirectResponse("/", status_code=303)


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


# Live Streaming
@app.get("/live", response_class=air.TagResponse)
@require_auth
async def live_streams(request: Request):
    email = get_user_email(request)
    user_streams = [(sid, s) for sid, s in streams.items() if s["host"] == email]
    
    return page("Live Streams",
        *with_back_link(
            air.H1("Live Streams"),
            air.A("Create New Stream", href="/live/create"),
            air.Hr(),
            air.H2("Your Streams"),
            air.Ul(*[stream_list_item(sid, s) for sid, s in user_streams]) if user_streams else air.P("No streams yet")
        )
    )


@app.get("/live/create", response_class=air.TagResponse)
@require_auth
async def create_stream_form(request: Request):
    return page("Create Stream",
        *with_back_link(
            air.H1("Create Live Stream"),
            simple_form("/live/create", "Create",
                air.Input(type="text", name="title", placeholder="Stream Title", required=True)
            ),
            href="/live"
        )
    )


@app.post("/live/create")
@require_auth
async def create_stream(request: Request, title: str = Form()):
    email = get_user_email(request)
    
    # Create Mux live stream
    live_stream = live_api.create_live_stream(
        mux_python.CreateLiveStreamRequest(
            playback_policies=["public"],
            new_asset_settings=mux_python.CreateAssetRequest(
                playback_policies=["public"]
            )
        )
    )
    
    stream_id = live_stream.data.id
    streams[stream_id] = {
        "title": title,
        "host": email,
        "stream_key": live_stream.data.stream_key,
        "playback_id": live_stream.data.playback_ids[0].id,
        "status": "idle"
    }
    
    return RedirectResponse(f"/live/{stream_id}", status_code=303)


@app.get("/live/{stream_id}", response_class=air.TagResponse)
async def stream_details(request: Request, stream_id: str):
    email = get_user_email(request)
    stream = get_resource_or_404(streams, stream_id)
    is_host = email == stream["host"]
    
    return page(stream["title"],
        *with_back_link(
            air.H1(stream["title"]),
            air.P(f"Host: {stream['host']}"),
            
            # Host controls
            air.Div(
                air.H2("Stream Setup"),
                air.P("RTMP URL: ", air.Code("rtmp://live.mux.com/app")),
                air.P("Stream Key: ", air.Code(stream['stream_key'])),
                air.Hr(),
                simple_form(f"/live/{stream_id}/toggle", 
                    "Go Live" if stream["status"] == "idle" else "End Stream"
                )
            ) if is_host else "",
            
            # Video player
            air.Div(
                air.H2("Watch"),
                video_player(stream['playback_id'], "live-video-player", autoplay=True)
                if stream["status"] == "active" else air.P("Stream is not live")
            ) if email else air.P("Login to watch"),
            
            href="/live"
        )
    )


@app.post("/live/{stream_id}/toggle")
@require_auth
async def toggle_stream(request: Request, stream_id: str):
    email = get_user_email(request)
    stream = get_resource_or_404(streams, stream_id)
    
    if stream["host"] != email:
        raise HTTPException(status_code=403)
    
    stream["status"] = "idle" if stream["status"] == "active" else "active"
    return RedirectResponse(f"/live/{stream_id}", status_code=303)


# Video Upload
@app.get("/upload", response_class=air.TagResponse)
@require_auth
async def upload_form(request: Request):
    return page("Upload Video",
        *with_back_link(
            air.H1("Upload Video"),
            simple_form("/upload", "Get Upload URL",
                air.Input(type="text", name="title", placeholder="Video Title", required=True)
            )
        )
    )


@app.post("/upload")
@require_auth
async def create_upload(request: Request, title: str = Form()):
    email = get_user_email(request)
    
    # Create direct upload
    upload = direct_uploads_api.create_direct_upload(
        mux_python.CreateUploadRequest(
            cors_origin=os.getenv("APP_URL", "http://localhost:8000"),
            new_asset_settings=mux_python.CreateAssetRequest(
                playback_policies=["public"]
            )
        )
    )
    
    upload_id = upload.data.id
    uploads[upload_id] = {
        "title": title,
        "user": email,
        "url": upload.data.url
    }
    
    return RedirectResponse(f"/upload/{upload_id}", status_code=303)


@app.get("/upload/{upload_id}", response_class=air.TagResponse)
@require_auth
async def upload_instructions(request: Request, upload_id: str):
    upload = get_resource_or_404(uploads, upload_id)
    
    return page("Upload Instructions",
        *with_back_link(
            air.H1("Upload Your Video"),
            air.P(f"Title: {upload['title']}"),
            air.Hr(),
            air.P("Upload your video file using:"),
            air.Pre(f'curl -X PUT "{upload["url"]}" -T your-video.mp4'),
            air.Hr(),
            simple_form(f"/upload/{upload_id}/check", "Check Status"),
            href="/upload"
        )
    )


@app.post("/upload/{upload_id}/check")
@require_auth
async def check_upload(request: Request, upload_id: str):
    upload = get_resource_or_404(uploads, upload_id)
    
    # Check upload status
    upload_status = direct_uploads_api.get_direct_upload(upload_id)
    
    if upload_status.data.status == "asset_created":
        asset_id = upload_status.data.asset_id
        asset = assets_api.get_asset(asset_id)
        
        videos[asset_id] = {
            "title": upload["title"],
            "uploader": upload["user"],
            "playback_id": asset.data.playback_ids[0].id if asset.data.playback_ids else None,
            "status": asset.data.status
        }
        
        return RedirectResponse(f"/video/{asset_id}", status_code=303)
    
    return RedirectResponse(f"/upload/{upload_id}", status_code=303)


# Video Playback
@app.get("/videos", response_class=air.TagResponse)
async def list_videos():
    ready_videos = [(aid, v) for aid, v in videos.items() if v.get("status") == "ready"]
    
    return page("Videos",
        *with_back_link(
            air.H1("All Videos"),
            air.Ul(*[video_list_item(aid, v) for aid, v in ready_videos]) if ready_videos else air.P("No videos yet"),
            air.Hr(),
            air.A("Upload Video", href="/upload")
        )
    )


@app.get("/video/{asset_id}", response_class=air.TagResponse)
async def view_video(asset_id: str):
    video = get_resource_or_404(videos, asset_id)
    
    return page(video["title"],
        *with_back_link(
            air.H1(video["title"]),
            air.P(f"Uploaded by: {video['uploader']}"),
            air.Hr(),
            video_player(video['playback_id']) if video.get("status") == "ready" and video.get('playback_id') 
            else air.P("Video processing..."),
            href="/videos"
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)