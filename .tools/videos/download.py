import argparse
import subprocess
import os
import re
from concurrent.futures import ThreadPoolExecutor

TIME_PATTERN = re.compile(r"^\d+(?::\d{1,2}){0,2}$")
SECTION_OFFSET_SECONDS = 2  # Compensate for early trims observed in output

FORMAT_OPTIONS = {
    "mp4": {
        "extension": "mp4",
        "merge_format": "mp4",
        "selector": lambda res: (
            f"bestvideo[height<={res}][ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]"
        ),
    },
    "webm": {
        "extension": "webm",
        "merge_format": "webm",
        "selector": lambda res: (
            f"bestvideo[height<={res}][ext=webm]+bestaudio[ext=webm]/"
            f"best[height<={res}][ext=webm]/"
            "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]"
        ),
    },
}


def parse_timecode(time_str):
    """Validate and normalize a timestamp to HH:MM:SS."""
    if not TIME_PATTERN.match(time_str):
        raise ValueError(
            f"Invalid timestamp '{time_str}'. Use SS, MM:SS, or HH:MM:SS format."
        )

    parts = [int(part) for part in time_str.split(":")]

    if len(parts) == 1:
        total_seconds = parts[0]
    elif len(parts) == 2:
        minutes, seconds = parts
        if seconds >= 60:
            raise ValueError("Seconds must be less than 60 when minutes are provided.")
        total_seconds = minutes * 60 + seconds
    else:
        hours, minutes, seconds = parts
        if minutes >= 60 or seconds >= 60:
            raise ValueError("Minutes and seconds must be less than 60.")
        total_seconds = hours * 3600 + minutes * 60 + seconds

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    normalized = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return total_seconds, normalized


def format_seconds(total_seconds):
    """Convert seconds to an HH:MM:SS string."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def download_with_limit(
    video_id,
    max_size,
    start_time=None,
    end_time=None,
    requested_segment=None,
    offset_seconds=0,
    target_format="mp4",
):
    resolutions = [1080, 720, 480, 360]  # Resolutions to try, in descending order
    max_size_bytes = parse_size(max_size)  # Convert max_size to bytes 

    # Construct the video URL from the video ID
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    format_config = FORMAT_OPTIONS[target_format]

    segment_suffix = ""
    if requested_segment:
        display_start, display_end = requested_segment
        segment_suffix = f"_{display_start.replace(':', '-')}-{display_end.replace(':', '-')}"
    elif start_time and end_time:
        segment_suffix = f"_{start_time.replace(':', '-')}-{end_time.replace(':', '-')}"

    output_file = f"{video_id}{segment_suffix}.{format_config['extension']}"

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
        format_selector = format_config["selector"](res)
        command = [
            "yt-dlp",
            "--format", format_selector,
            "-o", output_file,
        ]

        merge_format = format_config.get("merge_format")
        if merge_format:
            command.extend(["--merge-output-format", merge_format])

        if start_time and end_time:
            section_arg = f"*{start_time}-{end_time}"
            command.extend([
                "--download-sections", section_arg,
                "--force-keyframes-at-cuts",
            ])

        command.append(video_url)

        # Run the command and capture the result
        try:
            subprocess.run(command, check=True)
            print(f"Downloaded file at resolution {res}p.")

            if requested_segment:
                print(
                    f"Requested segment: {requested_segment[0]} to {requested_segment[1]}"
                    f" (applied +{offset_seconds}s internal offset)."
                )
                print(f"Command segment: {start_time} to {end_time}.")
            elif start_time and end_time:
                print(f"Trimmed segment: {start_time} to {end_time}.")
            print(f"Output format: {target_format}.")

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
    parser = argparse.ArgumentParser(
        description=(
            "Download one or more YouTube videos within a size limit, optionally trimming "
            "to a specific time segment."
        )
    )
    parser.add_argument(
        "video_ids",
        help="Comma-separated list of YouTube video IDs to download.",
    )
    parser.add_argument(
        "max_size",
        nargs="?",
        default="100M",
        help="Maximum allowed file size per video (default: 100M).",
    )
    parser.add_argument(
        "--start",
        dest="start_time",
        help="Segment start time (SS, MM:SS, or HH:MM:SS).",
        metavar="TIME",
    )
    parser.add_argument(
        "--end",
        dest="end_time",
        help="Segment end time (SS, MM:SS, or HH:MM:SS).",
        metavar="TIME",
    )
    parser.add_argument(
        "--format",
        dest="target_format",
        choices=sorted(FORMAT_OPTIONS.keys()),
        default="webm",
        help="Container format for the output file (default: webm).",
    )

    args = parser.parse_args()

    if args.start_time or args.end_time:
        if not args.start_time or not args.end_time:
            parser.error("Both --start and --end must be provided together.")

        try:
            start_seconds, start_display = parse_timecode(args.start_time)
            end_seconds, end_display = parse_timecode(args.end_time)
        except ValueError as exc:
            parser.error(str(exc))

        if end_seconds <= start_seconds:
            parser.error("End time must be greater than start time.")

        start_seconds_shifted = start_seconds + SECTION_OFFSET_SECONDS
        end_seconds_shifted = end_seconds + SECTION_OFFSET_SECONDS

        start_time = format_seconds(start_seconds_shifted)
        end_time = format_seconds(end_seconds_shifted)
        requested_segment = (start_display, end_display)
        offset_seconds = SECTION_OFFSET_SECONDS
    else:
        start_time = None
        end_time = None
        requested_segment = None
        offset_seconds = 0

    target_format = args.target_format

    video_ids = [vid.strip() for vid in args.video_ids.split(",") if vid.strip()]

    if not video_ids:
        parser.error("No valid video IDs provided.")

    # Use ThreadPoolExecutor for parallel downloads
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(
                download_with_limit,
                video_id,
                args.max_size,
                start_time,
                end_time,
                requested_segment,
                offset_seconds,
                target_format,
            )
            for video_id in video_ids
        ]

        for future in futures:
            try:
                future.result()  # Wait for each download to complete
            except Exception as e:
                print(f"An error occurred: {e}")
