from pydantic import BaseModel


class UserInput(BaseModel):
    user_input: str
    user_role: str
