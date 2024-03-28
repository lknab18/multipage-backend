import sys
from fastapi.testclient import TestClient

from segmentation.api import app

client = TestClient(app)


# working test with no real functionality
def test_get():
    response = client.get("/get")
    assert response.status_code == 200
    assert response.content == b'hello'

def test_get_segmentation_map():
    f = open('image.jpg','wb')

    filename="../../photos/dog1.jpg"
    response = client.post("/predict", files={"file": ("filename", open(filename, "rb"), "image/jpg")})

    f.write(response.content)
    f.close()
