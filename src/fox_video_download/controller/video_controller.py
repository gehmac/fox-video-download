from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from fox_video_download.service.video_service import download_video
import os

router = APIRouter()

@router.get("/download")
def download_endpoint(url: str = Query(..., description="URL do vídeo")):
    output_file = download_video(url)
    # print(f"Video downloaded to: {output_file}")
    return FileResponse(output_file, media_type='video/mp4', filename=os.path.basename(output_file))
