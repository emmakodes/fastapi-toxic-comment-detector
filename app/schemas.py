from pydantic import BaseModel


class Comment(BaseModel):
    comments: str