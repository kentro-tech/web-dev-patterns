# Mux Live Streaming and Video Example

A minimal example demonstrating Mux integration with FastAPI and Air for live streaming and video uploads.

## Features

- **Live Streaming**: Create streams, get RTMP credentials for OBS/Zoom
- **Video Upload**: Direct uploads to Mux with playback
- **Authentication**: Simple session-based login
- **HLS Playback**: Cross-browser video streaming

## Setup

### 1. Get Mux Credentials

1. Sign up at [mux.com](https://mux.com)
2. Create an API Access Token
3. Save the Token ID and Secret

### 2. Configure Environment

```bash
cp .env.example .env

# Edit .env with your credentials:
# MUX_TOKEN_ID=your_token_id
# MUX_TOKEN_SECRET=your_token_secret
# SESSION_SECRET=your_session_secret
```

### 3. Install and Run

```bash
uv sync
fastapi dev main.py
```

## Usage

### Live Streaming

1. Login with any email
2. Go to "Live Streaming" → "Create New Stream"
3. Use the RTMP URL and Stream Key in OBS:
   - Server: `rtmp://live.mux.com/app`
   - Stream Key: (from the app)
4. Click "Go Live" to activate the stream

### Video Upload

1. Go to "Video Upload"
2. Get an upload URL
3. Upload your video:
   ```bash
   curl -X PUT "upload_url" -T video.mp4
   ```
4. Click "Check Status" until ready
5. View in "Browse Videos"

## Architecture

- **Framework**: FastAPI with Air for HTML
- **Video**: Mux for streaming and storage
- **Auth**: Session-based (in-memory)
- **Player**: HLS.js for adaptive streaming

## Key Files

- `main.py`: All application logic
- `static/player.js`: HLS.js initialization
- `.env.example`: Environment template