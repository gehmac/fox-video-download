import yt_dlp
import os

def download_video(url: str) -> dict:
    ydl_opts = {
        'format': 'best',  # ou outro formato desejado
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Diretório onde o vídeo será salvo
        'quiet': True,     # Para suprimir a saída do console
    }
    
    os.makedirs('downloads', exist_ok=True)  # Cria o diretório se não existir
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)  
    return file_path