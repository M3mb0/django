from pytube import YouTube
from django.conf import settings


def mp3_download(url):
    yt = YouTube(url)
    out_file = yt.streams.filter(only_audio=True) \
        .order_by('abr') \
        .desc() \
        .first() \
        .download(output_path=settings.DOWNLOADS_DIR, skip_existing=True)
    return out_file
