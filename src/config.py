from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = ""
    JWT_SECRET: str = ""
    JWT_ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRY: int = 0
    REDIS_HOST: str= ""
    REDIS_PORT: int= 6379
    JTI_EXPIRY: int= 3600
    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore"
    )

Config = Settings()