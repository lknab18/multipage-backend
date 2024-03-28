import io
import sys
from PIL import Image

import streamlit as st

sys.path.insert(0, 'C:\\Users\lknab\python-files\streamlit-example')
from helpers.segmentation_helper import process

# construct UI layout
st.title("DeepLabV3 image segmentation")

st.write(
    """Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
         This streamlit example uses a FastAPI service as backend.
         Visit this URL at `:8000/docs` for FastAPI documentation."""
)  # description and instructions

input_image = st.file_uploader("insert image")  # image upload widget

if st.button("Get segmentation map"):

    col1, col2 = st.columns(2)

    if input_image:
        segments = process(input_image)
        original_image = Image.open(input_image).convert("RGB")
        segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
        col1.header("Original")
        col1.image(original_image, use_column_width=True)
        col2.header("Segmented")
        col2.image(segmented_image, use_column_width=True)

    else:
        # handle case with no image
        st.write("Insert an image!")