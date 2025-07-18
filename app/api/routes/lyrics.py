from fastapi import APIRouter, Query
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

router = APIRouter()

class GenerationRequest(BaseModel):
    prompt: str = "Yo, check it"
    max_length: int = 50
    temperature: float = 0.8
    top_p: float = 0.9
    top_k: int = 50

# Load model and tokenizer
MODEL_PATH = "models/checkpoints"
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
model.eval()

@router.post("/generate")
def generate_lyrics(request: GenerationRequest):
    inputs = tokenizer.encode(request.prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=request.max_length,
        temperature=request.temperature,
        top_p=request.top_p,
        top_k=request.top_k,
        do_sample=True,
        num_return_sequences=1
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"lyrics": text}
