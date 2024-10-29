import os
from functools import lru_cache
from openai import OpenAI

from app.settings.settings import Settings


@lru_cache()
def get_settings():
    return Settings()


@lru_cache()
def get_openai_client():
    return OpenAI(api_key=get_settings().openai_api_key)
