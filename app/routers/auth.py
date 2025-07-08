from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/ping")
def ping():
    """
    Simple endpoint to check if the service is running.
    """
    return {"message": "Service is up and running"}