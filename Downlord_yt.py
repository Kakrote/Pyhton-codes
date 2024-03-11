from pytube import YouTube as yt
link=yt("") # paste link here;
video=link.streams.get_highest_resolution()
import os
os.chdir("C://Users//anshu//Downloads")
# print(os.listdir())

video.download()