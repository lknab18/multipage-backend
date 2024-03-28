FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir -p /api/segmentation

COPY requirements.txt /api/segmentation

WORKDIR /api/segmentation

RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /api/segmentation

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]