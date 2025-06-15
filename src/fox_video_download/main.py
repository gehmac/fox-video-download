from fastapi import FastAPI
from fox_video_download.controller.video_controller import router

app = FastAPI()
app.include_router(router)