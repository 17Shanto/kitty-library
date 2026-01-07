import bcrypt, jwt
from src.config import Config
from datetime import timedelta, datetime, timezone
import uuid
import logging

def generate_password_hash(password:str)->str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')

def verify_password(password:str, hash:str)->bool:
    password_bytes = password.encode('utf-8')
    hash_bytes = hash.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)

def create_access_token(user_data: dict, expiry: timedelta | None = None, refresh: bool = False):
    payload = {}
    payload['user'] = user_data
    
    
    # 1. Calculate the actual future datetime
    if expiry is not None:
        expire_at = datetime.now(timezone.utc) + expiry
    else:
        # If no expiry provided, use your constant
        expire_at = datetime.now(timezone.utc) + timedelta(seconds= Config.ACCESS_TOKEN_EXPIRY)
    
    # 2. Convert to Unix Timestamp (Integer)
    payload['exp'] = int(expire_at.timestamp())
    
    
    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh
    
    token = jwt.encode(
        payload = payload,
        key = Config.JWT_SECRET,
        algorithm = Config.JWT_ALGORITHM
    )
    return token


def decode_token(token: str)->dict|None:
     
    try:
        token_data = jwt.decode(
            jwt= token,
            key= Config.JWT_SECRET,
            algorithms= [Config.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e)
        return None