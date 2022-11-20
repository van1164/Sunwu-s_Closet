from fastapi import APIRouter, UploadFile, File
from ..models.s3service import s3service
router = APIRouter()

@router.post("/s3", tags=["s3bucket"])
async def put_images(file: UploadFile = File(None)):
    s3 = s3service()
    res = await s3.upload_file(file)
    return res