from pytube import YouTube # libray for downloading video
from youtube_transcript_api import YouTubeTranscriptApi # library for downloading captions
import re # regex library
import os # operating system library 

def download(url):
    # creating directory for downloads
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    # capturing video id
    pattern = r"v=([^&]+)"
    videoId = re.search(pattern, url).group(1)
    # downloading video
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True).get_by_itag(22)
    stream.download(filename="downloads/" + videoId+".mp4")
    # generating caption file
    srt = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=['en'])
    outFile = open("downloads/" + videoId+".txt", "w")
    for caption in srt:
        startTime = caption["start"]
        endTime = startTime + caption["duration"]
        output = str(startTime) + "-" + str(endTime) + ": " + caption["text"]
        outFile.write(output + "\n")