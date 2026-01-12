from redis import asyncio as aioredis
from src.config import Config

JTI_EXPIRY= 3600

token_blockList= aioredis.StrictRedis(
    host= Config.REDIS_HOST,
    port= Config.REDIS_PORT,
    db= 0,
    decode_responses=True
)

async def add_jti_to_blockList(jti:str)->None:
    await token_blockList.set(
        name= jti,
        value="",
        ex= JTI_EXPIRY
    )

async def token_in_blockList(jti:str)-> bool:
    jti= await token_blockList.get(jti)
    return jti is not None