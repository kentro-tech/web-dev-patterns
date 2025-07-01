# Mux Live Streaming and Video Example

This example demonstrates how to build a complete video platform using Mux with Air and FastAPI.

## Features

### Live Streaming
- Host live streams with stream key for OBS/Zoom
- Real-time HLS video playback with adaptive bitrate
- Stream status management (scheduled, live, ended)
- Attendee signup and access control
- Automatic recording of live streams

### Video Storage
- Direct video uploads to Mux
- Automatic processing and encoding
- HLS playback with browser compatibility
- Video listing and individual video pages

### Access Control
- Simple session-based authentication
- Host controls for stream management
- Signup required for viewing live streams
- Public access to recorded videos

## Setup

### 1. Create a Mux Account

1. Sign up at [https://mux.com](https://mux.com)
2. Navigate to Settings → API Access Tokens
3. Create a new token with "Mux Video" permissions
4. Save the Token ID and Token Secret

### 2. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your credentials:
# MUX_TOKEN_ID=your_token_id_here
# MUX_TOKEN_SECRET=your_token_secret_here
# SESSION_SECRET=<generate with: python -c "import secrets; print(secrets.token_urlsafe(32))">
```

### 3. Install and Run

```bash
# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Run the application
fastapi dev main.py
```

Visit http://localhost:8000 to see the platform.

## Usage Guide

### Hosting a Live Stream

1. **Login**: Click "Login" and enter your email
2. **Create Stream**: Click "Host Live" and schedule your stream
3. **Get Stream Key**: On the session page, click "Show Stream Key"
4. **Configure OBS**:
   - Settings → Stream
   - Service: Custom
   - Server: `rtmp://live.mux.com/app`
   - Stream Key: (paste your key)
5. **Start Streaming**: Click "Start Streaming" in OBS
6. **Go Live**: Click "Start Live" on the session page
7. **End Stream**: Click "End Stream" when done

### Uploading Videos

1. **Login**: Must be logged in to upload
2. **Upload**: Click "Upload Video" in navigation
3. **Get URL**: Enter title and get upload URL
4. **Upload File**: 
   ```bash
   curl -X PUT "upload_url_here" \
        -H "Content-Type: video/mp4" \
        --data-binary @your-video.mp4
   ```
5. **Check Status**: Click "Check Upload Status"
6. **View**: Once ready, video appears in "Browse Videos"

### Watching Content

- **Live Streams**: Sign up for a session to watch when live
- **Recorded Videos**: Browse and watch all uploaded videos
- **My Sessions**: Track streams you're hosting or attending

## Technical Details

### Architecture

- **Framework**: FastAPI with Air for HTML generation
- **Storage**: In-memory (example only - use database in production)
- **Video**: Mux for encoding, storage, and streaming
- **Playback**: HLS with hls.js for browser compatibility

### Key Endpoints

- `GET /` - Home page with upcoming streams
- `GET /host` - Create new live stream
- `GET /upload` - Upload video form
- `GET /videos` - Browse all videos
- `GET /video/{id}` - Watch specific video
- `GET /session/{id}` - Live stream page
- `POST /signup/{id}` - Sign up for stream
- `POST /create-upload` - Get upload URL
- `POST /go-live/{id}` - Start streaming
- `POST /end-stream/{id}` - End streaming

### Mux Integration

The example uses three main Mux APIs:

1. **Live Streams API**: Create and manage live streams
2. **Direct Uploads API**: Generate secure upload URLs
3. **Assets API**: Access video information

### Security Notes

This example uses:
- Session-based auth (simple email login)
- In-memory storage (not for production)
- Public playback policies (consider signed URLs for private content)

## Troubleshooting

### Stream Not Showing
- Ensure OBS is configured correctly
- Check stream key is copied exactly
- Verify "Start Live" was clicked
- Check browser console for HLS errors

### Upload Failing
- Ensure file is a valid video format
- Check upload URL hasn't expired
- Verify Mux credentials are correct
- Use Content-Type header matching your file

### Video Not Playing
- Wait for processing to complete
- Check browser supports HLS
- Verify playback_id exists
- Check console for JavaScript errors

### Common Errors

- **500 Error on Create Stream**: Check Mux credentials
- **403 on Upload**: Must be logged in
- **404 on Video**: Video doesn't exist or still processing
- **Stream Key Not Working**: Ensure using rtmp://live.mux.com/app

## Production Considerations

Before deploying to production:

1. **Database**: Replace in-memory storage with PostgreSQL/Redis
2. **Authentication**: Implement proper auth (OAuth, magic links)
3. **File Uploads**: Add file type/size validation
4. **Error Handling**: Add monitoring and alerting
5. **Scaling**: Use Redis for session storage
6. **Security**: Implement rate limiting and CORS
7. **CDN**: Consider using Mux's image/thumbnail APIs

## Learn More

- [Mux Documentation](https://docs.mux.com)
- [Mux Python SDK](https://github.com/muxinc/mux-python)
- [Air Framework](https://github.com/kobaltz/air)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [HLS.js Documentation](https://github.com/video-dev/hls.js)