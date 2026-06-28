from pydantic import BaseModel

class note(BaseModel):
  title:str
  content:str