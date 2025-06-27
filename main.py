from fastapi import FastAPI
from src.search_by_image.search import app as search_app

main_app = FastAPI()

# Root-level route for testing
@main_app.get("/")
def root():
    return {"message": "Main App is running"}

# Mount the inner app under a prefix
main_app.mount("/search", search_app)

#  uvicorn main:main_app --reload
#  uvicorn main:main_app --host 0.0.0.0 --port 8000
#  python -m uvicorn main:main_app --host 0.0.0.0 --port 8000

# docker run -p 8000:8000 ai-feature-app:latest
# docker run --env-file .env -p 8000:8000 --name ai-feature-container ai-feature
# docker build -t ai-feature:latest .
# This is the start command for container: docker start ai-feature-container