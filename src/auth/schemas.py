from pydantic import BaseModel , EmailStr

class USER_LOGIN(BaseModel):
    email: str
    password: str

class USER_REGISTER(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str