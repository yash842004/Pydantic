from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postelCode: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content:str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

address = Address(
    street = "abc omage road",
    city = 'mumbai',
    postelCode = '1234'
)

user = User(
    id = 1,
    name = "raj",
    address = address
)

comment = Comment(
    id = 1,
    content = "nice peace of work",
    replies=[
        Commnet(id = 2,content = "nice")
        ,Commnet(id = 3, content = "good")
        ]
)


