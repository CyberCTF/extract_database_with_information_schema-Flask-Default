FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libmariadb-dev gcc pkg-config && rm -rf /var/lib/apt/lists/*
COPY build/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY build/ ./
EXPOSE 5000
CMD ["python", "app.py"] 