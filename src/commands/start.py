import sys
import uvicorn
from fox_video_download import main

def main():
    uvicorn.run("src.fox_video_download.main:app", reload=True, port=3000)

def start():
    # Chama a função principal da interface Tkinter
    sys.exit(main.main())
