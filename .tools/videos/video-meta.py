import yt_dlp
import sys

def get_youtube_video_details(video_id):
    url = f"https://youtu.be/{video_id}"
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if info:
            title = info.get('title', 'Unknown Title')
            publisher = info.get('uploader', 'Unknown Publisher')
            publish_date = info.get('upload_date', 'Unknown Date')
            return title, publisher, publish_date[:4] + '-' + publish_date[4:6] + '-' + publish_date[6:]
        else:
            return None, None, None

def generate_prompt(video_id, title, publisher, publish_date):
    video_url = f"https://youtu.be/{video_id}"
    prompt = (
        f"\n\n\nIn 50 words or so, what is this video about, by {publisher}, titled '{title}': {video_url}?\n"
        "\nInstructions:\n"
        #"- Describe the events in past verbal time.\n"
        "- If necessary, search the internet for relevant related information about the topics in the video.\n"
        "- In the description, instead of saying 'This video', say 'The video'.\n"
        "- After that, tell me who published it and (in 10 to 20 words) what the publisher is, from which country, and when was the video published.\n\n"
    )
    return prompt

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <VIDEO_ID>")
        sys.exit(1)
    
    VIDEO_ID = sys.argv[1]
    
    title, publisher, publish_date = get_youtube_video_details(VIDEO_ID)
    
    if title and publisher:
        prompt = generate_prompt(VIDEO_ID, title, publisher, publish_date)
        print(prompt)
    else:
        print("Failed to retrieve video details. Check the video ID.")