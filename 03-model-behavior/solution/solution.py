from pydantic import BaseModel, field_validator,component_field,model_validator


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    rate_per_night: float
    total_amount: float

    @field_validator('nights')
    def night_validator(cls,v):
        if len(v) < 1:
            raise ValueError ("night must be greater then 1")
        return v
    
    @component_field
    @property
    def total_price(self)-> float:
        return self.rate_per_night * self.nights
    
        

