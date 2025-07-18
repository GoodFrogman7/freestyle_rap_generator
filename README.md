# 🎤 Freestyle Rap Lyrics Generator

This project generates freestyle rap lyrics using a fine-tuned GPT-2 model via Hugging Face and FastAPI.

## 🚀 Features

- GPT-2 based lyrics generation
- FastAPI backend with `/generate` endpoint
- Dockerized setup
- Mock dataset included for testing
- Ready for fine-tuning and deployment

## 📦 Requirements

- Docker or Python 3.10+
- pip (if running locally)

## 🛠️ Setup Instructions

### Option 1: Run with Docker
```bash
docker-compose up --build
```

### Option 2: Run locally
```bash
pip install -r requirements.txt
python app/services/generation.py
uvicorn app.main:app --reload
```

## 🎯 Usage

Send a POST request to:
```
http://localhost:8000/api/v1/generate
```

With JSON body:
```json
{
  "prompt": "Yo, I'm coming up next",
  "max_length": 50,
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 50
}
```

## 📁 Project Structure

- `app/`: FastAPI backend
- `data/`: Mock dataset
- `models/`: Checkpoints
- `config/`: Settings
- `frontend/`: React app (optional starter)

