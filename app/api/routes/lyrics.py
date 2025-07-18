from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os, requests, json

router = APIRouter()

class GenerationRequest(BaseModel):
    prompt: str = "Yo, check it"
    max_length: int = 50
    temperature: float = 0.8
    top_p: float = 0.9
    top_k: int = 50

# Use Hugging Face Inference API instead of hosting the model locally.
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "EleutherAI/gpt-neo-2.7B")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # Create at https://huggingface.co/settings/tokens

API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
# Prepare static headers once
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"} if HF_API_TOKEN else {}

@router.post("/generate")
def generate_lyrics(request: GenerationRequest):
    payload = {
        "inputs": request.prompt,
        "parameters": {
            "max_new_tokens": request.max_length,
            "temperature": request.temperature,
            "top_p": request.top_p,
            "top_k": request.top_k,
            "repetition_penalty": 1.2,
            "do_sample": True
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"HF API error: {e}")

    # The API can return {'error': 'Model loading'} while it spins up
    data = response.json()
    if isinstance(data, dict) and data.get("error"):
        raise HTTPException(status_code=503, detail=data["error"])

    # Successful response is a list of generated strings
    if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
        return {"lyrics": data[0]["generated_text"]}

    # Fallback
    return {"lyrics": str(data)}
