import jwt
from src.auth.schemas import USER_LOGIN
from src.config.environment import JWT_KEY, JWT_ALGO


def generate_paylaod(info:USER_LOGIN):
  payload = {
    "email":info.email,
    "password":info.password
  }

def store_token(payload:dict):
  token = jwt.encode(payload,JWT_KEY,JWT_ALGO)