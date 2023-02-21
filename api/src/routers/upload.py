from fastapi import APIRouter

router = APIRouter()

@router.post("/upload/", tags=["upload"])
async def upload():
    return []