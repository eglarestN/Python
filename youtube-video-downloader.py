from pytube import YouTube

yt = YouTube(input("enter URL: "))

print(f"Video Header: {yt.title}")
print(f"Video Streamer: {yt.author}")
print(f"Video views: {yt.views}")
print(f"Video Length: {yt.length}")

video = yt.streams.get_highest_resolution()

path = ""

video.download(path)
