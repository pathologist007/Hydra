# Hydra YouTube Video Downloader

This script allows you to download videos from various sources using `yt-dlp`. It supports dynamic destination folders, video format selection (mp4 or mkv), and video resolution options.

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    ```

2. **Navigate to the repository folder:**
    ```sh
    cd <repository_folder>
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Important Note for Linux Users

It is recommended to use a virtual environment to install the prerequisites. This helps avoid conflicts with system-wide packages and ensures a clean environment for your project. Here are the steps to create and activate a virtual environment:

1. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**
    - On **Ubuntu/Debian**:
        ```sh
        source venv/bin/activate
        ```
    - On **Fedora**:
        ```sh
        source venv/bin/activate
        ```

3. **Install the required dependencies within the virtual environment:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```sh
    python download_video.py
    ```

2. **Enter the video URL when prompted.**

3. **Choose the desired video format (mp4 or mkv) and resolution.**

4. **The video will be downloaded to your `Downloads` folder.**

## Requirements

- Python 3.x
- `yt-dlp`
- `tqdm`
- `FFmpeg`

## License

This project is licensed under the MIT License.

---

Feel free to replace `<repository_url>` and `<repository_folder>` with the actual URL and folder name of your repository. If you have any more questions or need further assistance, just let me know!
