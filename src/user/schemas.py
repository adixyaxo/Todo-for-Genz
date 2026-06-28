from pydantic import BaseModel

class USER(BaseModel):
    uid:str
    first_name: str
    last_name: str
    email: str
    password: str
    bio:str
    id:str
    preferences:list