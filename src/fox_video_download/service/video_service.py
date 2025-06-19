import yt_dlp
import os
import sys

def get_ffmpeg_path():
    base = getattr(sys, '_MEIPASS', os.path.abspath("."))
    ffmpeg_path = os.path.join(base, "ffmpeg.exe")
    return ffmpeg_path

def download_video(url: str, output_dir: str, progress_callback=None) -> str:
    os.makedirs(output_dir, exist_ok=True)
    ffmpeg_path = get_ffmpeg_path()
    def hook(d):
        if d['status'] == 'downloading' and progress_callback:
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if total:
                percent = int(downloaded / total * 100)
                progress_callback(percent)
        elif d['status'] == 'finished' and progress_callback:
            progress_callback(100)
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
        'progress_hooks': [hook],
        'ffmpeg_location': ffmpeg_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
    return file_path