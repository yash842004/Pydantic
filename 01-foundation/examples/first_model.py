from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool


# (it wil not work because of name field missmatch)
#  input_data = {'id': 101, 'name': 'om', 'isactive': True} 
# input_data = {'id': 101, 'name': 'om', 'is_active': True} 
# (it will work)
input_data = {'id': 101, 'name': 'om', 'is_active': 'True'} 


user = User(**input_data)
print(user);


