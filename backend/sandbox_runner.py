from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
import logging

router = APIRouter()

class SandboxRequest(BaseModel):
    code: str
    language: Literal["html", "js", "sql"]

class SandboxResponse(BaseModel):
    status: str
    message: str

@router.post("/run", response_model=SandboxResponse)
async def run_code(request: SandboxRequest):
    # UWAGA: to jest tylko atrapa — faktyczne uruchomienie kodu
    # następuje po stronie frontendowego sandboxa (iframe/sql.js)
    
    # Tu możesz kiedyś dodać walidator lub pre-parser (np. eslint, js-beautify)
    try:
        logging.info(f"Przyjęto kod do sandboxu ({request.language}), długość: {len(request.code)} znaków")
        return SandboxResponse(
            status="accepted",
            message="Kod został przyjęty i zostanie uruchomiony po stronie frontendowego sandboxa"
        )
    except Exception as e:
        logging.error(f"Błąd sandbox runnera: {e}")
        raise HTTPException(status_code=500, detail="Nie udało się przetworzyć kodu")
