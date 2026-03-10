from pydantic import BaseModel
#Todo: Create Production model with id, name , price in stock

class Production(BaseModel):
    id: int
    name: str
    price: float
    in_stock: True;



stored_data = {id:1,'name':'om','pric_in_stock':11.2}
    # {2,'om',19.2},


production = Production(**stored_data)
print(production);