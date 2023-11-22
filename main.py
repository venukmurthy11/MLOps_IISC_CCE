from fastapi import FastAPI

app = FastAPI()

@new_app.get("/") def read_root(): return {"Hello": "World"}
