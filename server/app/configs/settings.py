from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List, Optional

class DatabaseSettings(BaseSettings):
    database_type: str = Field(default="postgresql", alias="DATABASE_TYPE")
    database_url: Optional[str] = Field(default=None, alias="DATABASE_URL")
    
    postgres_driver: str = Field(default="postgresql+psycopg2", alias="POSTGRES_DRIVER")
    postgres_user: str = Field(default="postgres", alias="POSTGRES_USER")
    postgres_password: str = Field(default="Allah786#", alias="POSTGRES_PASSWORD")
    postgres_host: str = Field(default="localhost", alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, alias="POSTGRES_PORT")
    postgres_db: str = Field(default="aip_leaves_bot", alias="POSTGRES_DB")

    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")

    def get_db_url(self) -> str:
        #print(f"##### PostgreSQL connection URL (self URL) in settings.py file: {self.database_url} #####")
        if self.database_url:
            return self.database_url
        
        # Default to PostgreSQL
        #print(f"##### PostgreSQL connection URL (new URL) in setting.py file: {self.postgres_driver}://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db} #####")
        return f"{self.postgres_driver}://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


class ServerSettings(BaseSettings):
    cors_urls: List[str] = Field(default=["localhost"], alias="CORS_URLS")
    #public_paths: List[str] = Field(default=["/"], alias="PUBLIC_PATHS")
    api_secret_key: str = Field(default="AIPROXYS", alias="API_SECRET_KEY")
    api_rate_limit: int = Field(default=1000, alias="API_RATE_LIMIT")
    token_secret_key: str = Field(default="AIPROXYS", alias="TOKEN_SECRET_KEY")
    token_expire_minutes: int = Field(default=60, alias="TOKEN_EXPIRE_MINUTES")
    token_issuer: str = Field(default="AIPROXYS", alias="TOKEN_ISSUER")
    token_algorithm: str = Field(default="HS256", alias="TOKEN_KEY_ALGORITHM")
    api_name: str = Field(default="AIPROXYS Chatbot API Server", alias="API_NAME")
    version: str = Field(default="0.1.1", alias="VERSION")
    
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")


class AppSettings(BaseSettings):
    db: DatabaseSettings = Field(default_factory=DatabaseSettings)
    server: ServerSettings = Field(default_factory=ServerSettings)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Singleton instance
settings = AppSettings()
