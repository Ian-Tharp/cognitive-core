import os


class Settings:
    openai_api_key: str

    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
