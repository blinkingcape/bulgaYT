from pytube import YouTube
from sys import argv

link = input("Link do video: ")
yt = YouTube(link)

print("Title:", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download()