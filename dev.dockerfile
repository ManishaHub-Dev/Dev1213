FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install sqlite3

CMD ["python", "database_operations.py"]
