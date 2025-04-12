from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from utils.llm_router import route_to_llm
import logging

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    model: str  # Nazwa modelu z llm_config.yaml

class GenerateResponse(BaseModel):
    code: str
    commentary: str
    llm_used: str

@router.post("/", response_model=GenerateResponse)
async def generate_code(request: GenerateRequest):
    logging.info(f"Generowanie kodu z modelu: {request.model}")

    try:
        result = route_to_llm(prompt=request.prompt, model_name=request.model)
        return GenerateResponse(
            code=result.get("code", ""),
            commentary=result.get("commentary", ""),
            llm_used=request.model,
        )
    except Exception as e:
        logging.error(f"LLM Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
