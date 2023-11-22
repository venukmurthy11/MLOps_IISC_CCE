from fastapi import FastAPI

new_app = FastAPI()

@new_app.get("/")
def read_root():
    return {"Hello": "World"}
