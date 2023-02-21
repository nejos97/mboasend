from fastapi import APIRouter

router = APIRouter()

@router.get("/download/", tags=["download"])
async def download():
    return []

@router.get("/check/", tags=["download"])
async def download():
    return []