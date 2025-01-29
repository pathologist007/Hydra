import os
import yt_dlp
from tqdm import tqdm

# Global progress bar
progress_bar = None

def download_video():
    # Set the destination folder dynamically based on the operating system
    home_dir = os.path.expanduser("~")
    download_path = os.path.join(home_dir, "Downloads")
    
    # Get the video URL and file format from the user
    video_url = input("Enter the video URL: ")
    
    # Allow user to choose video format (mp4 or mkv)
    print("Choose the video format:")
    print("1. .mp4")
    print("2. .mkv")
    format_choice = input("Enter the number of your choice (1 or 2): ")
    
    if format_choice == "1":
        file_format = "mp4"
    elif format_choice == "2":
        file_format = "mkv"
    else:
        print("Invalid choice! Defaulting to .mp4")
        file_format = "mp4"
    
    # Allow user to choose video resolution
    print("Choose the resolution:")
    print("1. 144p")
    print("2. 240p")
    print("3. 360p")
    print("4. 480p")
    print("5. 720p")
    print("6. 1080p")
    resolution_choice = input("Enter the number of your choice (1 to 6): ")

    # Validate resolution choice
    resolution_map = {
        "1": 144,
        "2": 240,
        "3": 360,
        "4": 480,
        "5": 720,
        "6": 1080
    }
    if resolution_choice in resolution_map:
        resolution = resolution_map[resolution_choice]
    else:
        print("Invalid choice! Defaulting to 720p.")
        resolution = 720

    # Define the options for yt-dlp
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': file_format,  # convert to mp4 or mkv
        }],
        'progress_hooks': [progress_hook],
        'quiet': True,  # Disable yt-dlp's default progress output
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'geo_bypass': True,  # Bypass geo-restrictions
        'force_generic_extractor': True  # Fallback extractor
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Starting video download...")
            ydl.download([video_url])
            print("\nDownload completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

# Progress hook to show download progress
def progress_hook(d):
    global progress_bar
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes', 0)
        if progress_bar is None and total_size > 0:
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading")
        downloaded = d.get('downloaded_bytes', 0)
        if progress_bar:
            progress_bar.n = downloaded
            progress_bar.refresh()
    elif d['status'] == 'finished':
        if progress_bar:
            progress_bar.n = progress_bar.total
            progress_bar.close()
            progress_bar = None
        print(f"\nDownload completed: {d['filename']}")

if __name__ == "__main__":
    download_video()
    input("\nPress Enter to exit...")

