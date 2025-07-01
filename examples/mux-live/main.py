import os
import mux_python
import air
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from markupsafe import Markup
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"))

# Initialize Mux
configuration = mux_python.Configuration()
configuration.username = os.getenv("MUX_TOKEN_ID")
configuration.password = os.getenv("MUX_TOKEN_SECRET")

live_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
direct_uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))

# In-memory store for simplicity
streams, signups, videos, uploads = {}, {}, {}, {}

def format_datetime_et(dt_string: str) -> str:
    """Format datetime string to Eastern Time"""
    dt = datetime.fromisoformat(dt_string.replace('Z', '+00:00'))
    et = dt.astimezone(ZoneInfo('America/New_York'))
    return et.strftime('%B %d, %Y at %I:%M %p ET')

def error_page(title: str, message: str, email: str = None, links: list = None):
    """Create a consistent error page"""
    if links is None:
        links = [("Back to Home", "/")]
    
    return air.Html(
        air.Head(air.Title(title)),
        air.Body(
            nav_menu(email),
            air.H1(title),
            air.P(message),
            air.Hr(),
            *[air.Div(air.A(text, href=href), air.Br()) for text, href in links]
        )
    )


def nav_menu(email: str = None, current_page: str = None):
    """Create a consistent navigation menu for all pages"""
    links = [
        ("Home", "/", current_page == "home"),
        ("Browse Videos", "/videos", current_page == "videos"),
        ("Host Live", "/host", current_page == "host"),
        ("Upload Video", "/upload", current_page == "upload"),
        ("My Sessions", "/my-sessions", current_page == "my-sessions")
    ]
    
    nav_items = []
    for title, href, is_active in links:
        nav_items.append(air.A(title, href=href))
        nav_items.append(air.Span(" | "))
    
    return air.Nav(
        *nav_items,
        air.Br(),
        air.Span(f"Logged in as: {email} | ") if email else "",
        air.A("Logout", href="/logout") if email else air.A("Login", href="/login"),
        air.Hr()
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    email = request.session.get("email")
    
    if exc.status_code == 404:
        return air.TagResponse(error_page(
            "Page Not Found",
            "Sorry, the page you're looking for doesn't exist.",
            email,
            [("Back to Home", "/"), ("Browse Videos", "/videos")]
        ))
    elif exc.status_code == 403:
        return air.TagResponse(error_page(
            "Access Denied",
            "You don't have permission to access this resource.",
            email,
            [("Back to Home", "/"), ("Login", "/login")]
        ))
    elif exc.status_code == 401:
        return RedirectResponse("/login", status_code=303)
    else:
        return air.TagResponse(error_page(
            f"Error {exc.status_code}",
            exc.detail or "An error occurred.",
            email
        ))


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    email = request.session.get("email")
    return air.TagResponse(error_page(
        "Invalid Request",
        "The request contained invalid data. Please check your input and try again.",
        email
    ))


@app.get("/", response_class=air.TagResponse)
async def index(request: Request):
    email = request.session.get("email")
    
    return air.Html(
        air.Head(air.Title("Live Course Platform")),
        air.Body(
            nav_menu(email, "home"),
            air.H1("Course Platform"),
            air.H2("Upcoming Live Sessions"),
            air.Ul(
                *[air.Li(
                    f"{stream['title']} - {format_datetime_et(stream['start_time'])}",
                    air.Form(
                        air.Button("Sign Up", type="submit"),
                        action=f"/signup/{stream_id}",
                        method="post"
                    ) if email and email not in signups.get(stream_id, {}) else air.Span(" (Signed up)") if email else ""
                ) for stream_id, stream in streams.items() if stream['status'] == 'scheduled']
            ) if streams else air.P("No upcoming sessions")
        )
    )


@app.get("/login", response_class=air.TagResponse)
async def login_form():
    return air.Html(
        air.Head(air.Title("Login")),
        air.Body(
            air.H1("Login"),
            air.Form(
                air.Label("Email:", for_="email"),
                air.Input(type="email", name="email", id="email", required=True),
                air.Button("Login", type="submit"),
                action="/login",
                method="post"
            )
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


@app.get("/host", response_class=air.TagResponse)
async def host_form(request: Request):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    return air.Html(
        air.Head(air.Title("Host Session")),
        air.Body(
            nav_menu(email, "host"),
            air.H1("Schedule Live Session"),
            air.Form(
                air.Label("Session Title:", for_="title"),
                air.Input(type="text", name="title", id="title", required=True),
                air.Br(),
                air.Label("Start Time:", for_="start_time"),
                air.Input(type="datetime-local", name="start_time", id="start_time", required=True),
                air.Br(),
                air.Button("Create Session", type="submit"),
                action="/host",
                method="post"
            )
        )
    )


@app.post("/host")
async def create_session(request: Request, title: str = Form(), start_time: str = Form()):
    email = request.session.get("email")
    if not email:
        raise HTTPException(status_code=401)
    
    # Create Mux live stream
    create_live_stream_request = mux_python.CreateLiveStreamRequest(
        playback_policies=["public"],
        new_asset_settings=mux_python.CreateAssetRequest(
            playback_policies=["public"]
        )
    )
    
    try:
        live_stream = live_api.create_live_stream(create_live_stream_request)
        
        stream_id = live_stream.data.id
        streams[stream_id] = {
            "title": title,
            "start_time": start_time,
            "host": email,
            "stream_key": live_stream.data.stream_key,
            "playback_id": live_stream.data.playback_ids[0].id,
            "status": "scheduled"
        }
        
        return RedirectResponse(f"/session/{stream_id}", status_code=303)
    except Exception as e:
        print(f"Error creating live stream: {e}")  # Log for debugging
        return air.Html(
            air.Head(air.Title("Error")),
            air.Body(
                air.H1("Error Creating Stream"),
                air.P("Sorry, we couldn't create your live stream. Please try again."),
                air.P(f"Error details: {str(e)}" if os.getenv("DEBUG") else ""),
                air.A("Back to Host Form", href="/host"),
                air.Br(),
                air.A("Back to Home", href="/")
            )
        )


@app.get("/session/{stream_id}", response_class=air.TagResponse)
async def session_details(request: Request, stream_id: str):
    email = request.session.get("email")
    if stream_id not in streams:
        raise HTTPException(status_code=404)
    
    stream = streams[stream_id]
    is_host = email == stream["host"]
    is_signed_up = email in signups.get(stream_id, {})
    
    return air.Html(
        air.Head(
            air.Title(stream["title"]),
            air.Script(src="https://cdn.jsdelivr.net/npm/hls.js@latest")
        ),
        air.Body(
            air.H1(stream["title"]),
            air.P(f"Start time: {format_datetime_et(stream['start_time'])}"),
            air.P(f"Host: {stream['host']}"),
            air.P(f"Attendees: {len(signups.get(stream_id, {}))}"),
            air.Hr(),
            air.Div(
                air.H2("Host Controls"),
                air.Details(
                    air.Summary("Show Stream Key & Setup Instructions"),
                    air.Div(
                        air.H4("For OBS:"),
                        air.P("Server: ", air.Code("rtmp://live.mux.com/app", style="background: #f0f0f0; padding: 2px 5px;")),
                        air.P("Stream Key: ", air.Code(stream['stream_key'], style="background: #f0f0f0; padding: 2px 5px;")),
                        air.Hr(),
                        air.H4("For Zoom:"),
                        air.P("1. In Zoom settings, go to 'In Meeting (Advanced)' → Enable 'Allow live streaming meetings'"),
                        air.P("2. In your meeting, click 'More' → 'Live on Custom Live Streaming Service'"),
                        air.P("3. Enter these values:"),
                        air.P("Stream URL: ", air.Code("rtmp://live.mux.com/app", style="background: #f0f0f0; padding: 2px 5px;")),
                        air.P("Stream Key: ", air.Code(stream['stream_key'], style="background: #f0f0f0; padding: 2px 5px;")),
                        air.P("Live streaming page URL: ", air.Code(f"{os.getenv('APP_URL', 'http://localhost:8000')}/session/{stream_id}", style="background: #f0f0f0; padding: 2px 5px; word-break: break-all;"))
                    )
                ),
                air.Form(
                    air.Button("Start Live", type="submit"),
                    action=f"/go-live/{stream_id}",
                    method="post"
                ) if stream["status"] == "scheduled" else (
                    air.Form(
                        air.Button("End Stream", type="submit"),
                        action=f"/end-stream/{stream_id}",
                        method="post"
                    ) if stream["status"] == "live" else air.P("Status: " + stream["status"])
                ),
                air.P(f"Mux Stream Status: {stream.get('mux_status', 'Unknown')}", style="font-size: 0.9em; color: #666;") if stream.get('mux_status') else "",
                air.Hr(),
                air.Details(
                    air.Summary("View Attendees"),
                    air.Ul(
                        *[air.Li(attendee) for attendee in signups.get(stream_id, {})]
                    ) if signups.get(stream_id) else air.P("No signups yet")
                )
            ) if is_host else "",
            air.Div(
                air.H2("Watch Live"),
                air.Div(
                    air.Video(
                        id="live-video-player",
                        src=f"https://stream.mux.com/{stream['playback_id']}.m3u8",
                        controls=True,
                        style="width: 100%; max-width: 800px;",
                        autoplay=True,
                        muted=True
                    ),
                    air.P("Note: It may take 10-30 seconds for the stream to appear after clicking 'Go Live' in Zoom.", style="color: #666; font-size: 0.9em;"),
                    air.Button("Refresh Stream", onclick="location.reload()", type="button", style="margin: 10px 0;"),
                    air.Details(
                        air.Summary("Troubleshooting"),
                        air.Ul(
                            air.Li("Make sure you clicked 'Go Live!' in the Zoom streaming dialog"),
                            air.Li("Wait 10-30 seconds for the stream to initialize"),
                            air.Li("Try refreshing this page"),
                            air.Li("Check browser console for errors (F12)")
                        )
                    ) if is_host else "",
                    air.Details(
                        air.Summary("Debug Info (Host Only)"),
                        air.P("Stream Playback ID: ", air.Code(stream['playback_id'], style="font-size: 0.8em;")),
                        air.P("HLS URL: ", air.A(f"https://stream.mux.com/{stream['playback_id']}.m3u8", href=f"https://stream.mux.com/{stream['playback_id']}.m3u8", target="_blank", style="font-size: 0.8em;")),
                        air.P("Test in VLC: Copy the HLS URL above and open it in VLC Media Player to test if the stream is active"),
                        air.P("Mux Dashboard: ", air.A("View in Mux Dashboard", href=f"https://dashboard.mux.com/organizations/ry02dm/video/live-streams/{stream_id}", target="_blank"))
                    ) if is_host else ""
                ) if stream["status"] == "live" else air.P("Stream will appear here when live"),
                air.RawHTML("""<script>
                (function() {
                    var video = document.getElementById('live-video-player');
                    if (video) {
                        console.log('Initializing video player for:', video.src);
                        
                        if (typeof Hls !== 'undefined' && Hls && Hls.isSupported()) {
                            var hls = new Hls({
                                debug: true,
                                enableWorker: true,
                                lowLatencyMode: true,
                                liveSyncDurationCount: 2,
                                liveMaxLatencyDurationCount: 4,
                                liveDurationInfinity: true,
                                manifestLoadingTimeOut: 30000,
                                manifestLoadingMaxRetry: 10,
                                manifestLoadingRetryDelay: 2000
                            });
                            
                            hls.loadSource(video.src);
                            hls.attachMedia(video);
                            
                            hls.on(Hls.Events.MANIFEST_PARSED, function() {
                                console.log('HLS manifest loaded, attempting to play');
                                video.play().then(function() {
                                    console.log('Playback started successfully');
                                }).catch(function(e) {
                                    console.log('Autoplay failed (expected), please click play:', e);
                                });
                            });
                            
                            hls.on(Hls.Events.ERROR, function(event, data) {
                                console.error('HLS Error:', data);
                                if (data.fatal) {
                                    switch(data.type) {
                                        case Hls.ErrorTypes.NETWORK_ERROR:
                                            console.log('Network error - retrying...');
                                            setTimeout(function() { hls.startLoad(); }, 2000);
                                            break;
                                        case Hls.ErrorTypes.MEDIA_ERROR:
                                            console.log('Media error - recovering...');
                                            hls.recoverMediaError();
                                            break;
                                        default:
                                            console.error('Fatal error:', data);
                                            break;
                                    }
                                }
                            });
                            
                            hls.on(Hls.Events.LEVEL_LOADED, function(event, data) {
                                console.log('Stream level loaded:', data);
                            });
                            
                        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
                            console.log('Using native HLS support');
                            video.play().catch(function(e) { console.log('Autoplay blocked:', e); });
                        }
                    }
                })();
                </script>""") if stream["status"] == "live" else ""
            ) if is_signed_up or is_host else air.Form(
                air.Button("Sign up to watch", type="submit"),
                action=f"/signup/{stream_id}",
                method="post"
            ) if email else air.A("Login to sign up", href="/login"),
            air.Hr(),
            air.A("Back", href="/")
        )
    )


@app.post("/signup/{stream_id}")
async def signup_for_session(request: Request, stream_id: str):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    if stream_id not in streams:
        raise HTTPException(status_code=404)
    
    if stream_id not in signups:
        signups[stream_id] = {}
    
    if email not in signups[stream_id]:
        signups[stream_id][email] = {
            "signed_up_at": datetime.now().isoformat()
        }
    
    return RedirectResponse(f"/session/{stream_id}", status_code=303)


@app.post("/go-live/{stream_id}")
async def go_live(request: Request, stream_id: str):
    email = request.session.get("email")
    if not email or stream_id not in streams or streams[stream_id]["host"] != email:
        raise HTTPException(status_code=401)
    
    # Check actual stream status from Mux
    try:
        mux_stream = live_api.get_live_stream(stream_id)
        print(f"Mux stream status: {mux_stream.data.status}")
        
        # Update with fresh data from Mux
        streams[stream_id]["mux_status"] = mux_stream.data.status
        streams[stream_id]["active_asset_id"] = mux_stream.data.active_asset_id if hasattr(mux_stream.data, 'active_asset_id') else None
        
        # Log more details
        print(f"Stream details - Status: {mux_stream.data.status}, Active: {mux_stream.data.active}, Active Asset: {getattr(mux_stream.data, 'active_asset_id', 'None')}")
    except Exception as e:
        print(f"Error getting stream status: {e}")
    
    streams[stream_id]["status"] = "live"
    streams[stream_id]["started_at"] = datetime.now().isoformat()
    return RedirectResponse(f"/session/{stream_id}", status_code=303)


@app.post("/end-stream/{stream_id}")
async def end_stream(request: Request, stream_id: str):
    email = request.session.get("email")
    if not email or stream_id not in streams or streams[stream_id]["host"] != email:
        raise HTTPException(status_code=401)
    
    streams[stream_id]["status"] = "ended"
    streams[stream_id]["ended_at"] = datetime.now().isoformat()
    
    # Try to disable the live stream in Mux
    try:
        live_api.disable_live_stream(stream_id)
    except Exception as e:
        print(f"Error disabling live stream: {e}")
    
    return RedirectResponse(f"/session/{stream_id}", status_code=303)


@app.get("/upload", response_class=air.TagResponse)
async def upload_form(request: Request):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    return air.Html(
        air.Head(air.Title("Upload Video")),
        air.Body(
            nav_menu(email, "upload"),
            air.H1("Upload Video"),
            air.P("Upload a video to share with others"),
            air.Form(
                air.Label("Video Title:", for_="title"),
                air.Input(type="text", name="title", id="title", required=True, placeholder="My Amazing Video"),
                air.Br(),
                air.Br(),
                air.P("After submitting, you'll receive instructions on how to upload your video file."),
                air.Button("Get Upload URL", type="submit"),
                action="/create-upload",
                method="post"
            )
        )
    )


@app.post("/create-upload")
async def create_upload(request: Request, title: str = Form()):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    try:
        # Create a direct upload
        create_upload_request = mux_python.CreateUploadRequest(
            cors_origin=os.getenv("APP_URL", "http://localhost:8000"),
            new_asset_settings=mux_python.CreateAssetRequest(
                playback_policies=["public"],
                video_quality="basic"
            )
        )
        
        upload_response = direct_uploads_api.create_direct_upload(create_upload_request)
        upload_id = upload_response.data.id
        
        # Store upload info
        uploads[upload_id] = {
            "user": email,
            "title": title,
            "created_at": datetime.now().isoformat(),
            "status": "waiting",
            "upload_url": upload_response.data.url
        }
        
        return RedirectResponse(f"/upload/{upload_id}/instructions", status_code=303)
    except Exception as e:
        print(f"Error creating upload: {e}")
        return air.Html(
            air.Head(air.Title("Error")),
            air.Body(
                air.H1("Error Creating Upload"),
                air.P("Sorry, we couldn't create an upload URL. Please try again."),
                air.P(f"Error details: {str(e)}" if os.getenv("DEBUG") else ""),
                air.A("Back to Upload Form", href="/upload"),
                air.Br(),
                air.A("Back to Home", href="/")
            )
        )


@app.get("/upload/{upload_id}/instructions", response_class=air.TagResponse)
async def upload_instructions(request: Request, upload_id: str):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    if upload_id not in uploads:
        raise HTTPException(status_code=404)
    
    upload_info = uploads[upload_id]
    if upload_info["user"] != email:
        raise HTTPException(status_code=403)
    
    return air.Html(
        air.Head(air.Title("Upload Instructions")),
        air.Body(
            air.H1("Upload Your Video"),
            air.P(f"Title: {upload_info['title']}"),
            air.Hr(),
            air.H2("Upload Instructions"),
            air.P("Use one of the following methods to upload your video file:"),
            air.H3("Option 1: Using curl (Command Line)"),
            air.Pre(f"""curl -X PUT "{upload_info['upload_url']}" \\
     -H "Content-Type: video/mp4" \\
     --data-binary @your-video.mp4""", style="background: #f0f0f0; padding: 10px; overflow-x: auto;"),
            air.H3("Option 2: Using a web form"),
            air.P("You can also use any HTTP client or file upload tool that supports PUT requests."),
            air.Hr(),
            air.P("After uploading your file, click the button below to check the status:"),
            air.Form(
                air.Button("Check Upload Status", type="submit"),
                action=f"/upload/{upload_id}/check",
                method="post"
            ),
            air.Hr(),
            air.A("Back to Home", href="/")
        )
    )


@app.post("/upload/{upload_id}/check")
async def check_upload_status(request: Request, upload_id: str):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    if upload_id not in uploads:
        raise HTTPException(status_code=404)
    
    upload_info = uploads[upload_id]
    if upload_info["user"] != email:
        raise HTTPException(status_code=403)
    
    try:
        # Check upload status
        upload_status = direct_uploads_api.get_direct_upload(upload_id)
        
        if upload_status.data.status == "asset_created":
            # Upload is complete and asset was created
            asset_id = upload_status.data.asset_id
            uploads[upload_id]["status"] = "asset_created"
            uploads[upload_id]["asset_id"] = asset_id
            
            # Get asset details
            asset = assets_api.get_asset(asset_id)
            
            # Store video info
            videos[asset_id] = {
                "title": upload_info["title"],
                "uploader": email,
                "upload_time": datetime.now().isoformat(),
                "playback_id": asset.data.playback_ids[0].id if asset.data.playback_ids else None,
                "status": asset.data.status,
                "duration": asset.data.duration if hasattr(asset.data, 'duration') else None
            }
            
            return RedirectResponse(f"/video/{asset_id}", status_code=303)
        
        elif upload_status.data.status == "errored":
            # Upload failed
            return air.Html(
                air.Head(air.Title("Upload Failed")),
                air.Body(
                    air.H1("Upload Failed"),
                    air.P("The upload failed. Please try again."),
                    air.P(f"Error: {upload_status.data.error.message}" if hasattr(upload_status.data, 'error') else ""),
                    air.A("Try Another Upload", href="/upload"),
                    air.Br(),
                    air.A("Back to Home", href="/")
                )
            )
        else:
            # Still processing
            return air.Html(
                air.Head(air.Title("Upload Processing")),
                air.Body(
                    air.H1("Upload Processing"),
                    air.P(f"Status: {upload_status.data.status}"),
                    air.P("Your video is still being processed. Please check back in a moment."),
                    air.Form(
                        air.Button("Check Again", type="submit"),
                        action=f"/upload/{upload_id}/check",
                        method="post"
                    ),
                    air.Hr(),
                    air.A("Back to Home", href="/")
                )
            )
    except Exception as e:
        print(f"Error checking upload status: {e}")
        return air.Html(
            air.Head(air.Title("Error")),
            air.Body(
                air.H1("Error Checking Upload"),
                air.P("Sorry, we couldn't check your upload status."),
                air.P(f"Error details: {str(e)}" if os.getenv("DEBUG") else ""),
                air.A("Back to Instructions", href=f"/upload/{upload_id}/instructions"),
                air.Br(),
                air.A("Back to Home", href="/")
            )
        )


@app.get("/videos", response_class=air.TagResponse)
async def list_videos(request: Request):
    email = request.session.get("email")
    
    # Get all ready videos
    ready_videos = [(aid, v) for aid, v in videos.items() if v.get("status") == "ready"]
    
    return air.Html(
        air.Head(air.Title("Browse Videos")),
        air.Body(
            nav_menu(email, "videos"),
            air.H1("All Videos"),
            air.Div(
                *[air.Div(
                    air.H3(air.A(video["title"], href=f"/video/{asset_id}")),
                    air.P(f"Uploaded by: {video['uploader']}"),
                    air.P(f"Duration: {video['duration']:.1f}s" if video.get('duration') else "Processing..."),
                    air.Hr()
                ) for asset_id, video in ready_videos]
            ) if ready_videos else air.P("No videos uploaded yet."),
            air.A("Upload a Video", href="/upload") if email else air.A("Login to Upload", href="/login")
        )
    )


@app.get("/video/{asset_id}", response_class=air.TagResponse)
async def view_video(request: Request, asset_id: str):
    email = request.session.get("email")
    
    if asset_id not in videos:
        raise HTTPException(status_code=404)
    
    video = videos[asset_id]
    playback_url = f"https://stream.mux.com/{video['playback_id']}.m3u8" if video.get('playback_id') else None
    
    return air.Html(
        air.Head(
            air.Title(video["title"]),
            air.Script(src="https://cdn.jsdelivr.net/npm/hls.js@latest")
        ),
        air.Body(
            nav_menu(email),
            air.H1(video["title"]),
            air.P(f"Uploaded by: {video['uploader']}"),
            air.P(f"Upload time: {video['upload_time']}"),
            air.P(f"Duration: {video['duration']:.1f} seconds" if video.get('duration') else "Processing..."),
            air.Hr(),
            air.Div(
                air.Video(
                    id="video-player",
                    controls=True,
                    style="width: 100%; max-width: 800px;",
                    src=playback_url
                ) if playback_url else air.P("Video is still processing..."),
                air.RawHTML("""<script>
                    var video = document.getElementById('video-player');
                    if (video && video.src && Hls.isSupported()) {
                        var hls = new Hls();
                        hls.loadSource(video.src);
                        hls.attachMedia(video);
                        hls.on(Hls.Events.MANIFEST_PARSED, function() {
                            console.log('HLS manifest loaded');
                        });
                    } else if (video && video.canPlayType('application/vnd.apple.mpegurl')) {
                        // Safari native HLS support
                        console.log('Using native HLS support');
                    }
                </script>
                """) if playback_url else ""
            ),
        )
    )


@app.get("/my-sessions", response_class=air.TagResponse)
async def my_sessions(request: Request):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)
    
    hosted = [(sid, s) for sid, s in streams.items() if s["host"] == email]
    attending = [(sid, s) for sid, s in streams.items() if email in signups.get(sid, {})]
    
    return air.Html(
        air.Head(air.Title("My Sessions")),
        air.Body(
            nav_menu(email, "my-sessions"),
            air.H1("My Sessions"),
            air.H2("Hosting"),
            air.Ul(*[air.Li(air.A(s["title"], href=f"/session/{sid}")) for sid, s in hosted]) if hosted else air.P("None"),
            air.H2("Attending"),
            air.Ul(*[air.Li(air.A(s["title"], href=f"/session/{sid}")) for sid, s in attending]) if attending else air.P("None")
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)