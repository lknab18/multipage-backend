FROM python:3.11-slim

RUN mkdir /ui

COPY requirements.txt /ui

WORKDIR /ui

RUN pip install -r requirements.txt

COPY . /ui

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]