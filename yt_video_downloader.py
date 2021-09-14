from pytube import YouTube

url=input ("enter the video link\n")
myvideo=YouTube(url)

print(myvideo.title)

myvideo=myvideo.streams.get_highest_resolution()
myvideo.download()