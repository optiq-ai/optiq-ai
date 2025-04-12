from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import yaml
import os
import requests
import logging

router = APIRouter()

LLM_CONFIG_PATH = os.getenv("LLM_CONFIG", "config/llm_config.yaml")

def load_llms():
    with open(LLM_CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
    return config.get("llms", {})

@router.get("/", response_model=List[str])
async def list_models():
    llms = load_llms()
    return list(llms.keys())

class TestRequest(BaseModel):
    model: str
    test_prompt: str = "Wygeneruj komponent React z przyciskiem"

@router.post("/test")
async def test_model_connection(data: TestRequest):
    from utils.llm_router import route_to_llm

    try:
        result = route_to_llm(prompt=data.test_prompt, model_name=data.model)
        return {
            "status": "ok",
            "preview": result.get("code", "")[:300],
            "commentary": result.get("commentary", "")[:300],
        }
    except Exception as e:
        logging.error(f"Test modelu {data.model} nie powiódł się: {e}")
        raise HTTPException(status_code=500, detail=str(e))
