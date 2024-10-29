from fastapi import APIRouter, Request
from app.models.user_input import UserInput

router = APIRouter()


@router.post("")
def core_entry(user_input: UserInput, request: Request):
    pass


@router.post("/comprehension")
async def comprehension(user_input: UserInput, request: Request):
    pass


@router.post("/orchestration")
async def orchestration(user_input: UserInput, request: Request):
    pass


@router.post("/reasoning")
async def reasoning(user_input: UserInput, request: Request):
    pass


@router.post("/evaluation")
async def evaluation(user_input: UserInput, request: Request):
    pass
