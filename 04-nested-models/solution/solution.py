from pydantic import BaseModel
from typing import List,Optional

class Model(BaseModel):
    model_id: int
    name: str
    lessons: Optional[List[lessons]] = None

class Course(BaseModel):
    course_id: int
    model: List[Model]

class lessons(BaseModel):
    lesson_id: int
    lesson_name: str




