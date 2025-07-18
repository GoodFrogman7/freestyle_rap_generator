from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import lyrics

app = FastAPI(
    title="Freestyle Rap Lyrics Generator",
    description="Generate freestyle rap lyrics using GPT-2",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lyrics.router, prefix="/api/v1")
