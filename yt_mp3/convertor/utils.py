from pytube import YouTube
from django.conf import settings
from io import BytesIO


def mp3_download(url):
    yt = YouTube(url)
    out_file = BytesIO()
    audio = yt.streams.filter(only_audio=True) \
        .order_by('abr') \
        .desc() \
        .first()

    name = audio.default_filename
    audio.stream_to_buffer(out_file)
    # .download(output_path=settings.DOWNLOADS_DIR, skip_existing=True)
    return out_file, name
