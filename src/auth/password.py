import bcrypt
from pydantic import BaseModel

def hash_password(password: str):
  salt = bcrypt.gensalt()
  return bcrypt.hashpw(password.encode('utf-8'),salt)

# check = bcrypt.checkpw(password, hashed_password)