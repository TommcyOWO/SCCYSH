from pydantic import BaseModel,EmailStr

class register_reset(BaseModel):
    email: EmailStr
    username: str
    password: str   
class login(BaseModel):
    username: str
    password: str