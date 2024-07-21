from typing import Annotated
from fastapi import FastAPI, Body, status

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.get("/posts")
async def read_posts():
    return {"data": "This is a post."}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(payload: Annotated[dict, Body()]):
    # print(payload)
    # return {"data": f"title: {payload['title']}, content: {payload['content']}"}
    # return {"data": f"{payload}"}
    return payload
