from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == {"data": "This is a post."}


def test_create_post():
    response = client.post("/posts", json={"title": "t1", "content": "c1"})
    print(response.json())
    assert response.status_code == 201
    assert response.json() == {"title": "t1", "content": "c1"}
