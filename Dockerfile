from python:3.12-slim

workdir /app

copy . .

run pip install --no-cache-dir -r requirements.txt

expose 5000

cmd ["python", "app.py"]