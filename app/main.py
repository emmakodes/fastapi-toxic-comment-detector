from fastapi import Depends, FastAPI

from .dependencies import check_toxicity
from .routers import comments

app = FastAPI()


app.include_router(comments.router)
