FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
