from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.get("/posts")
async def read_posts():
    return {"data": "This is a post."}
