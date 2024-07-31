FROM python:3.8-slim

LABEL maintainer="your-email@example.com" #Provide email address here

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install sqlite3

# Set environment variables
ENV DATABASE_URL=example.db

CMD ["python", "main.py"]	
	