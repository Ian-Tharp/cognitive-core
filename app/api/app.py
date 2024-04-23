from fastapi import FastAPI
# #from app.main import process_user_input

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
#
# # @app.post("/process/")
# # async def process(input: dict):
# #     result = process_user_input(input["data"])
# #     return result
