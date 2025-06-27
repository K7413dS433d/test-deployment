# AI Feature Image Search API

This FastAPI application provides image search functionality using DeepImageSearch.

## Features
- Image upload and similarity search
- MongoDB integration for image data retrieval
- Asynchronous processing

## Local Development
1. Install dependencies: `pip install -r requirements.txt`
2. Set up MongoDB connection in `.env` file (see `.env.example`)
3. Run the server: `uvicorn main:main_app --reload`
