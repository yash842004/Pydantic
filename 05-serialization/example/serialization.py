from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    city: str
    street: str
    zip_code: str

class User(BaseModel):
    user_id:int
    name: str
    email: str
    isActive: bool = True;
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda V: V.strftime(
            '%d-%m-%Y %H:%M:%S' 
        )}
    )
      
    
# create a user instance
User = User(
    user_id =1,
    name = 'raj',
    email = 'raj@14.com',
    isActive = True,
    createdAt = datetime(2024,3,15,14,30),
    address = Address
    (city = 'rajkot',street = 'road',zip_code = '1010'),
    tags = ['yo','cool','nice']
);

# Using modul_dump() -> dict
python_dict = User.model_dump()
print(python_dict)
print("=====================================================")
# Using modul_dump() -> dict
python_json = User.model_dump_json()
print(python_json)






