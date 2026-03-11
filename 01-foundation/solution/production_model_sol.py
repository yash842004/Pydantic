from pydantic import BaseModel
#Todo: Create Production model with id, name , price in stock

class Production(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True;



stored_data = {'id':1,'name':'om','price':11.2}
    


production = Production(**stored_data)
print(production);