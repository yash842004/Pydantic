from pydantic import BaseModel, Field

from typing import List,dict,Optional

class Employee(BaseModel):
    emp_id: int
    name: str = Field(..., min_length=3,
                      max_lenght=23,
                      description="Employees Name",
                      examples="om kumar"
                      )
    departement: Optional[str] = "HR"
    # ge -> greater then 
    salary: float = Field(...,ge=10000)
    


