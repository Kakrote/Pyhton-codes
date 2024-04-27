from pytube import YouTube as yt
try:
    link=yt("https://youtu.be/jYuO8GWp5EM?si=dXHp-L6Gll3Qchxz") # paste link here;
    n=int(input("Enter 1 for vedio and 2 for audio only"))
    if n==2:
        video=link.streams.get_audio_only()
    else:
        video=link.streams.get_highest_resolution()
    import os
    os.chdir("C://Users//anshu//Downloads")
    # print(os.listdir())

    video.download()
except Exception as e:
    print(e)
    