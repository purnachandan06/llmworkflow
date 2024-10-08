from fastapi import APIRouter

router = APIRouter(prefix="/sample", tags=["sample"])

@router.get("")
def get_sample():
    """
    Method for sample test router
    """
    return {"message": "Hello World"}
