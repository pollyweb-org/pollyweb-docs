import subprocess
import os
import sys
import re
from concurrent.futures import ThreadPoolExecutor

def download_with_limit(video_id, max_size):
    resolutions = [1080, 720, 480, 360]  # Resolutions to try, in descending order
    max_size_bytes = parse_size(max_size)  # Convert max_size to bytes 

    # Construct the video URL from the video ID
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    output_file = f"{video_id}.mp4"

    # Check if the file already exists
    if os.path.exists(output_file):
        print(f"File '{output_file}' already exists. Skipping download.")
        return

    for res in resolutions:
        print(f"Attempting to download at resolution {res}p...")

        # Remove any preexisting file from previous attempts
        if os.path.exists(output_file):
            os.remove(output_file)

        # Construct the yt-dlp command
        command = [
            "yt-dlp",
            "--format", f"bestvideo[height<={res}][ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]",
            "--merge-output-format", "mp4",
            "-o", output_file,
            video_url
        ]

        # Run the command and capture the result
        try:
            subprocess.run(command, check=True)
            print(f"Downloaded file at resolution {res}p.")

            # Check file size
            if os.path.exists(output_file):
                file_size_bytes = os.path.getsize(output_file)
                print(f"File size: {file_size_bytes / (1024 * 1024):.2f} MB")

                if file_size_bytes <= max_size_bytes:
                    print(f"File within size limit: {max_size}. Download successful.")
                    return
                else:
                    print(f"File exceeds size limit: {max_size}. Deleting and trying lower resolution.")
                    os.remove(output_file)
            else:
                print(f"File not found after download attempt at resolution {res}p.")

        except subprocess.CalledProcessError:
            print(f"Failed to download at resolution {res}p. Trying the next resolution...")

    print("No suitable resolution was found within the file size limit.")

def parse_size(size_str):
    """Convert a size string like '100M' to bytes."""
    size_str = size_str.upper()
    if size_str.endswith('K'):
        return int(float(size_str[:-1]) * 1024)
    elif size_str.endswith('M'):
        return int(float(size_str[:-1]) * 1024 * 1024)
    elif size_str.endswith('G'):
        return int(float(size_str[:-1]) * 1024 * 1024 * 1024)
    else:
        return int(size_str)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_with_limit.py <video_id1,video_id2,...> [<max_size>, e.g. 100M]")
        sys.exit(1)

    video_ids = sys.argv[1].split(",")

    if len(sys.argv) < 3:
        max_size = '100M'
    else:
        max_size = sys.argv[2]  # File size limit, e.g., '100M'

    # Use ThreadPoolExecutor for parallel downloads
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_with_limit, video_id, max_size) for video_id in video_ids]

        for future in futures:
            try:
                future.result()  # Wait for each download to complete
            except Exception as e:
                print(f"An error occurred: {e}")
