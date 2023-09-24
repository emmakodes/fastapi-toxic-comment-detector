from fastapi import Depends, FastAPI

from .routers import comments

app = FastAPI()


app.include_router(comments.router)
