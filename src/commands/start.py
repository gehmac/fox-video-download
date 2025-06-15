import uvicorn

def main():
    uvicorn.run("src.fox_video_download.main:app", reload=True, port=3000)
