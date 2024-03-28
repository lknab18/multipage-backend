import io
import sys
from starlette.responses import Response

from fastapi import FastAPI, File

#sys.path.insert(0, 'C:\\Users\lknab\python-files\streamlit-example')
from helper import get_segmentator, get_segments

model = get_segmentator()

app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)


@app.post("/predict")
def predict(file: bytes = File(...)):
    """Get segmentation maps from image file"""
    segmented_image = get_segments(model, file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")

@app.get("/get")
def get():
    return Response('hello', status_code=200)