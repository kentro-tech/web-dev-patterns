# Mux Live Example Implementation Plan

## Overview
This plan outlines the implementation of a minimal but complete Mux-powered Air application that demonstrates:
1. **Video Storage & Playback**: Upload and embed recorded videos
2. **Live Streaming**: Stream live content via OBS/Zoom
3. **Access Control**: Permission-based viewing using session authentication

## Air Framework Principles
- Use `air.TagResponse` for all HTML responses
- Build UI with Air tags (no separate templates)
- Keep it simple - in-memory storage is fine for examples
- Use Form submissions with POST/redirect/GET pattern
- Minimal JavaScript - rely on server-side rendering

## Key Issues to Fix

### 1. Fix CreateAssetSettings Error
- **Current**: `mux_python.CreateAssetSettings` (doesn't exist)
- **Correct**: `mux_python.CreateAssetRequest`
- **Also fix**: `playback_policy` → `playback_policies` (plural)

### 2. Implement Proper Video Storage
Add functionality for uploading and storing recorded videos:
- Use `DirectUploadsApi` for creating upload URLs
- Allow users to upload video files
- Display uploaded videos in a gallery

### 3. Enhance Live Streaming
- Add proper stream status management (idle, active, disabled)
- Implement simulcast targets for streaming to multiple platforms
- Add recording functionality for live streams

## Implementation Steps

### Phase 1: Fix Existing Live Stream Creation
1. Update the `create_session` function to use correct Mux API:
   ```python
   create_live_stream_request = mux_python.CreateLiveStreamRequest(
       playback_policies=["public"],
       new_asset_settings=mux_python.CreateAssetRequest(
           playback_policies=["public"]
       )
   )
   ```

2. Add error handling for Mux API failures

3. Store additional stream metadata (asset_id for recordings)

### Phase 2: Add Video Upload Feature
1. Create new endpoints:
   - `GET /upload` - Upload form
   - `POST /create-upload` - Generate Mux upload URL
   - `GET /videos` - List uploaded videos
   - `GET /video/{asset_id}` - View individual video

2. Implement upload workflow:
   - Generate direct upload URL with CORS settings
   - Provide upload interface (with progress)
   - Poll for upload completion
   - Display video once ready

3. Store video metadata:
   ```python
   videos = {}  # asset_id -> {title, uploader, upload_time, playback_id, status}
   ```

### Phase 3: Enhance Live Streaming Features
1. Add stream management:
   - Enable/disable streams
   - Show connection status
   - Display viewer count

2. Add recording controls:
   - Toggle recording during live stream
   - Access recordings after stream ends

3. Improve stream playback:
   - Use proper HLS player (hls.js)
   - Add quality selection
   - Show buffering/loading states

### Phase 4: Improve Access Control
1. Keep it simple with session-based auth:
   - Logged-in users can host streams
   - Logged-in users can sign up to watch
   - Non-logged-in users see public content only

2. Basic signup flow:
   - Store signups in memory
   - Show "Signed up" status
   - Control video access based on signup

### Phase 5: Air-Specific UI Improvements
1. Server-side video player:
   - Use standard HTML5 `air.Video` element
   - HLS.js loaded via CDN for browser support
   - Simple controls attribute

2. Clean Air layouts:
   - Semantic HTML with Air tags
   - Forms for all interactions
   - Clear navigation with `air.A` links

## Data Models

### Stream Model
```python
streams[stream_id] = {
    "title": str,
    "start_time": str,
    "host": str,
    "stream_key": str,
    "playback_id": str,
    "status": "scheduled" | "live" | "ended",
    "asset_id": str | None,  # For recordings
    "viewer_count": int
}
```

### Video Model
```python
videos[asset_id] = {
    "title": str,
    "uploader": str,
    "upload_time": str,
    "playback_id": str,
    "status": "uploading" | "processing" | "ready" | "error",
    "duration": float,
    "thumbnail": str
}
```

### Upload Model
```python
uploads[upload_id] = {
    "user": str,
    "created_at": str,
    "asset_id": str | None,
    "status": "waiting" | "asset_created" | "errored" | "cancelled"
}
```

## Environment Variables
```
MUX_TOKEN_ID=your_mux_token_id
MUX_TOKEN_SECRET=your_mux_token_secret
SESSION_SECRET=<generated-secret>
APP_URL=http://localhost:8000
```

## No Additional Frontend Dependencies
- Use native HTML5 video element with Air
- Load HLS.js from CDN only when needed
- Keep it simple - no React or complex components

## Security Considerations
1. Validate upload file types and sizes
2. Implement rate limiting for API calls
3. Use signed URLs for private content
4. Sanitize user inputs (titles, descriptions)

## Testing Plan
1. Test upload flow with various file formats
2. Test live streaming with OBS and Zoom
3. Verify access control works correctly
4. Test error scenarios (failed uploads, API errors)

## Future Enhancements (Out of Scope for Example)
- Payment integration (see stripe example)
- Real-time chat (would need WebSockets)
- Analytics dashboard
- Advanced streaming features