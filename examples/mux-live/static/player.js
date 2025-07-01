// Initialize HLS.js for video playback
function initializePlayer(videoId) {
    const video = document.getElementById(videoId);
    if (!video || !video.src) return;

    if (Hls.isSupported()) {
        const hls = new Hls({
            debug: false,
            enableWorker: true,
            lowLatencyMode: true
        });
        
        hls.loadSource(video.src);
        hls.attachMedia(video);
        
        hls.on(Hls.Events.MANIFEST_PARSED, function() {
            video.play().catch(e => console.log('Autoplay blocked'));
        });
        
        hls.on(Hls.Events.ERROR, function(event, data) {
            if (data.fatal) {
                console.error('Fatal HLS error:', data);
                if (data.type === Hls.ErrorTypes.NETWORK_ERROR) {
                    setTimeout(() => hls.startLoad(), 1000);
                }
            }
        });
    } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        // Safari native HLS support
        video.play().catch(e => console.log('Autoplay blocked'));
    }
}

// Initialize players when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializePlayer('live-video-player');
    initializePlayer('video-player');
});