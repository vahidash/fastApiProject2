FROM python:3.10.1-slim-buster
WORKDIR /usr/src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
# CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]