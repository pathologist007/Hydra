import os
import yt_dlp
from tqdm import tqdm

# Global progress bar
progress_bar = None

def download_audio():
    global progress_bar

    # Set the destination folder dynamically based on the operating system
    home_dir = os.path.expanduser("~")
    download_path = os.path.join(home_dir, "Music")

    # Get the video URL and file format from the user
    video_url = input("Enter the video URL: ").strip()
    
    # Allow user to choose audio format (mp3 or m4a)
    while True:
        print("Choose the audio format:")
        print("1. .mp3")
        print("2. .m4a")
        format_choice = input("Enter the number of your choice (1 or 2): ").strip()
        if format_choice == "1":
            file_format = "mp3"
            break
        elif format_choice == "2":
            file_format = "m4a"
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

    # Define the options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best available audio
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save with title and chosen extension
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_format,  # Convert to the chosen format (mp3 or m4a)
        }],
        'progress_hooks': [progress_hook],
        'quiet': True,  # Disable yt-dlp's default progress output
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'geo_bypass': True,  # Bypass geo-restrictions
    }

    # Download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Starting audio download...")
            ydl.download([video_url])
            print("\nDownload completed successfully!")
        except yt_dlp.utils.DownloadError as e:
            print(f"Download error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if progress_bar:
                progress_bar.close()
                progress_bar = None

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
    download_audio()
    input("\nPress Enter to exit...")

