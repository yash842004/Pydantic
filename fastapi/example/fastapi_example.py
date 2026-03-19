from fastapi import FastAPI, Depends
from pydantic import BaseMode, EmailStr


app = FastAPI();


class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class Setting(BaseModel):
    app_name: str = "Chai App"
    admin_email: str = "admin@email.com"


def get_settings():
    return Setting

@app.post('/signUp')
def signUp(user: UserSignUp):
    return {'message':f'User{user.username} sign up'}

@app.get('/setting')
def get_setting(Setting: Setting = Depends(get_settings)) :
    return Setting

