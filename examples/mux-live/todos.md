# Mux Live Example - Implementation Tasks

## Phase 1: Fix Live Stream API Error

### Task 1.1: Fix CreateAssetRequest Import
**Description**: Update the create_live_stream call to use the correct Mux API classes
**Files**: `main.py`
**Changes**:
- Change `mux_python.CreateAssetSettings` to `mux_python.CreateAssetRequest`
- Change `playback_policy` to `playback_policies`
**Test**: 
- Run `fastapi dev main.py`
- Login and navigate to /host
- Fill form and submit
- Should redirect to /session/{id} without 500 error
- Verify stream object is created in memory

### Task 1.2: Add Proper Error Handling
**Description**: Wrap Mux API calls in try/except blocks with user-friendly errors
**Files**: `main.py`
**Changes**:
- Add try/except around `live_api.create_live_stream()`
- Return Air error page on failure
- Log actual error for debugging
**Test**:
- Temporarily use invalid Mux credentials
- Try to create a stream
- Should see friendly error page instead of 500
- Restore valid credentials

## Phase 2: Add Video Upload Feature

### Task 2.1: Create Upload Form Page
**Description**: Add a page where users can initiate video uploads
**Files**: `main.py`
**Changes**:
- Add `GET /upload` endpoint with Air form
- Include title field and file upload instructions
- Only show to logged-in users
**Test**:
- Navigate to /upload when logged in
- Should see upload form with title field
- Navigate to /upload when logged out
- Should redirect to /login

### Task 2.2: Create Direct Upload Endpoint
**Description**: Generate Mux direct upload URLs
**Files**: `main.py`
**Changes**:
- Import and initialize `DirectUploadsApi`
- Add `POST /create-upload` endpoint
- Create upload with CORS origin for browser uploads
- Store upload info in memory
- Return upload URL and instructions
**Test**:
- Submit upload form
- Should receive upload URL from Mux
- URL should be valid (starts with https://storage.googleapis.com)
- Upload ID should be stored in memory

### Task 2.3: Add Upload Instructions Page
**Description**: Show users how to upload their video file
**Files**: `main.py`
**Changes**:
- Add `GET /upload/{upload_id}/instructions` endpoint
- Display upload URL and curl/fetch example
- Add form to mark upload as complete
**Test**:
- After creating upload, should see instructions page
- Instructions should include actual upload URL
- Should show example curl command

### Task 2.4: Handle Upload Completion
**Description**: Check upload status and create video entry
**Files**: `main.py`
**Changes**:
- Add `POST /upload/{upload_id}/check` endpoint
- Use `get_direct_upload` to check status
- When asset is created, store in videos dict
- Redirect to video view page
**Test**:
- Actually upload a small video file to the URL
- Click "Check Status" button
- Once processed, should redirect to video page
- Video should play successfully

### Task 2.5: Create Video Listing Page
**Description**: Show all uploaded videos
**Files**: `main.py`
**Changes**:
- Add `GET /videos` endpoint
- List all videos from memory
- Show title, uploader, and thumbnail
- Link to individual video pages
**Test**:
- Navigate to /videos
- Should see all uploaded videos
- Each video should link to its page
- Empty state when no videos

### Task 2.6: Create Individual Video Page
**Description**: Display a single video with player
**Files**: `main.py`
**Changes**:
- Add `GET /video/{asset_id}` endpoint
- Show video title and uploader
- Include Air.Video element with HLS URL
- Add basic HLS.js script for browser support
**Test**:
- Click on video from listing
- Video should load and play
- Controls should work
- Non-existent video should show 404

## Phase 3: Enhance Live Streaming

### Task 3.1: Add Stream Status Management
**Description**: Allow hosts to update stream status
**Files**: `main.py`
**Changes**:
- Update go_live to actually check stream status
- Add "End Stream" button for hosts
- Show current status on session page
**Test**:
- Create a stream
- Click "Start Live" - status should change
- Click "End Stream" - status should update
- Viewers should see status changes

### Task 3.2: Add HLS.js Support for Live Streams
**Description**: Improve live video playback with HLS.js
**Files**: `main.py`
**Changes**:
- Add Script tag to load HLS.js from CDN
- Add inline script to initialize HLS when supported
- Fallback to native playback
**Test**:
- Start a live stream
- Video element should use HLS.js in Chrome/Firefox
- Should fall back to native in Safari
- Console should show "HLS.js initialized" or similar

### Task 3.3: Show Stream Key Better
**Description**: Improve stream key display for hosts
**Files**: `main.py`
**Changes**:
- Hide stream key by default
- Add "Show Stream Key" button
- Format key in monospace font
- Add copy button functionality
**Test**:
- Host should see "Show Stream Key" button
- Clicking reveals the key
- Key should be in monospace/code font
- Non-hosts shouldn't see any key info

## Phase 4: Improve Access Control

### Task 4.1: Add Proper Signup Tracking
**Description**: Better tracking of who signed up for what
**Files**: `main.py`
**Changes**:
- Add timestamp to signups
- Show signup count to hosts
- List attendees on session page (for hosts)
**Test**:
- Multiple users sign up for a stream
- Host sees attendee count
- Host sees list of emails
- Viewers don't see other attendees

### Task 4.2: Restrict Video Access
**Description**: Only allow signed-up users to watch
**Files**: `main.py`
**Changes**:
- Check signup status before showing video element
- Show "Sign up to watch" for non-attendees
- Allow hosts to always watch their streams
**Test**:
- Non-signed-up user sees signup prompt
- After signup, video appears
- Host can always see video
- Logged out users see login prompt

## Phase 5: Polish and Cleanup

### Task 5.1: Add Navigation Menu
**Description**: Consistent navigation across all pages
**Files**: `main.py`
**Changes**:
- Create nav_menu() function returning Air elements
- Include: Home, Videos, Host, My Sessions
- Show login status
- Add to all pages
**Test**:
- Every page has navigation
- Links work correctly
- Login status shows correctly
- Active page is indicated

### Task 5.2: Improve Error Pages
**Description**: Better error handling and display
**Files**: `main.py`
**Changes**:
- Create error_page() function
- Use for 404s, permission denied, etc.
- Include helpful navigation options
**Test**:
- Visit /video/nonexistent - see nice 404
- Try to host when logged out - see auth error
- All errors have way back to home

### Task 5.3: Add README Documentation
**Description**: Document how to use the example
**Files**: `README.md`
**Changes**:
- Update with setup instructions
- Add Mux account requirements
- Include OBS configuration steps
- Add troubleshooting section
**Test**:
- Follow README from scratch
- Should successfully set up Mux account
- Should successfully stream with OBS
- Common errors are documented

## Testing Checklist

After all tasks are complete, perform full integration test:

1. **Account Setup**
   - [ ] Can create Mux account
   - [ ] Can get API credentials
   - [ ] Environment variables work

2. **Video Upload Flow**
   - [ ] Can navigate to upload page
   - [ ] Can create direct upload
   - [ ] Can upload video file
   - [ ] Video processes successfully
   - [ ] Can view uploaded video

3. **Live Streaming Flow**
   - [ ] Can create live stream
   - [ ] Can get stream key
   - [ ] Can stream from OBS
   - [ ] Viewers can sign up
   - [ ] Viewers can watch stream
   - [ ] Can end stream properly

4. **Access Control**
   - [ ] Login required for hosting
   - [ ] Login required for signup
   - [ ] Signup required for viewing
   - [ ] Hosts can manage their streams

5. **Error Handling**
   - [ ] Invalid pages show 404
   - [ ] API errors handled gracefully
   - [ ] Missing credentials show helpful error
   - [ ] Network issues don't crash app