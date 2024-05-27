from fastapi.params import Body
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.get("/posts")
async def read_posts():
    return {"data": "This is a post."}


@app.post("/posts")
async def create_post(payload: dict = Body(...)):
    print(payload)
    # return {"data": f"title: {payload['title']}, content: {payload['content']}"}
    # return {"data": f"{payload}"}
    return payload
