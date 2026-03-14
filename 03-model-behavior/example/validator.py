from pydantic import BaseModel, fiedl_validator,model_validator,computed_field;

class User(BaseModel):
    username: str

    @field_validator('username')
    def user_name(cls, v):
        if len(v) < 4:
            raise ValueError("username must be more then 4 char")
        return v
    


class SignUpData(BaseModel):
    username: str
    password: str

    @model_validator(model='after')
    def password_match(cls,v):
        if v.username != v.password:
            raise ValueError("password not mathch")
        return v


class Product(BaseModel):
    price: float
    quentaty: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quentaty
    

    