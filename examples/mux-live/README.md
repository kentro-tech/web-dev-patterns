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
uv sync
python main.py
```

## Usage

### Live Streaming

> [!WARNING]
> You must have this deployed to live stream, as streaming services can't reach localhost!  You can deploy the project as is to railway if you'd like to test it.

1. Login with any email
2. Go to "Live Streaming" → "Create New Stream"
3. Use the RTMP URL and Stream Key in OBS or Zoom:
   - Server: `rtmp://live.mux.com/app`
   - Stream Key: (from the app)
4. Click "Go Live" to activate the stream

> [!NOTE] 
> There is a configuration setting in zoom account to enable streaming that you need to do to have the option available to you

### Video Upload

1. Go to "Video Upload"
2. Get an upload URL
3. Upload your video using the curl command provided (at the end, change to point to your video file)
4. Click "Check Status"
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