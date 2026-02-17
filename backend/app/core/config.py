# loadenv is a function that reads the key-value pairs from a .env file and adds them to the environment variables.
from dotenv import load_dotenv
# os module provides a way of using operating system dependent functionality like reading environment variables.
import os

# Load environment variables from the .env file into the system's environment variables.
load_dotenv()

class Settings:
    # Define the settings class to hold the configuration values for the application.
    # The values are read from the environment variables, which can be set in the .env file.
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))


# Create an instance of the Settings class to be used throughout the application.
settings = Settings()