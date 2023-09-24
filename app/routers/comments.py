from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import check_toxicity



router = APIRouter(
    prefix="/comments",
    tags=["comments"],
)


@router.post('/')
async def check_toxic_comment(toxicity_check: Annotated[dict, Depends(check_toxicity)]):
    return toxicity_check