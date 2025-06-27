
FROM python:3.10


RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

COPY .cache/huggingface /root/.cache/huggingface


EXPOSE 8000


CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000"]
