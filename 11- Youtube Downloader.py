

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=Yv1QUkFro0U")

try:
    print(yt.title)

    print(yt.thumbnail_url)

    yt = yt.streams.get_highest_resolution()

    yt.download()

except Exception as error1:
    print(error1)