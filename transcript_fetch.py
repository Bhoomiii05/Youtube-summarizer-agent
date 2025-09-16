from youtube_transcript_api import YouTubeTranscriptApi

video_id = "GpsWTFciswE"

yt_api = YouTubeTranscriptApi()
transcript = yt_api.fetch(video_id)

# Convert to one string
clean_text = " ".join([entry.text for entry in transcript])

print("=== Clean Transcript ===")
print(clean_text)
# Save clean transcript into a text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("Transcript saved to transcript.txt ✅")
