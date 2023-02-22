from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Mboasend API"
    databse_host: str
    databse_port: str
    databse_name: str
    databse_username: str
    databse_password: str

    class Config:
        env_file = ".env"

    def get_database_connection_string(self) -> str:
        return "postgresql://{}:{}@{}:{}/{}".format(self.databse_username, self.databse_password, self.databse_host, self.databse_port, self.databse_name)
