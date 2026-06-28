from pydantic import BaseModel

class TASK(BaseModel):
  title:str
  description:str
  priority:int