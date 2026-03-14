from pydantic import BaseModel
from typing import List,dict,Optional


class Card(BaseModel):
    user_id: int
    items: List[str]
    queataty:dist[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None




