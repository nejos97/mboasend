from sqlalchemy.orm import Session
from .models.upload import Upload
from .models.file import File

async def get_upload(db: Session, upload_id: int):
    return db.query(Upload).filter(Upload.id == upload_id).first()

async def get_upload_files(db: Session, upload_id: int):
    return db.query(File).filter(File.upload == upload_id).first()
