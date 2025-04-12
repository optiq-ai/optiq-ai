from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from utils.llm_router import route_to_llm
import logging

router = APIRouter()

class PipelineStep(BaseModel):
    model: str
    task: str  # Opis, np. "frontend", "api", "testy"
    input_from_previous: bool = True

class PipelineRequest(BaseModel):
    prompt: str
    steps: List[PipelineStep]

class PipelineBlock(BaseModel):
    task: str
    model: str
    code: str
    commentary: str

class PipelineResponse(BaseModel):
    blocks: List[PipelineBlock]

@router.post("/", response_model=PipelineResponse)
async def run_pipeline(pipeline: PipelineRequest):
    logging.info(f"Uruchamiam pipeline z {len(pipeline.steps)} krokami")

    output_blocks = []
    last_output = pipeline.prompt

    try:
        for step in pipeline.steps:
            result = route_to_llm(prompt=last_output, model_name=step.model)
            block = PipelineBlock(
                task=step.task,
                model=step.model,
                code=result.get("code", ""),
                commentary=result.get("commentary", "")
            )
            output_blocks.append(block)
            if step.input_from_previous:
                last_output = result.get("code", "")
        return PipelineResponse(blocks=output_blocks)

    except Exception as e:
        logging.error(f"Błąd w pipeline: {e}")
        raise HTTPException(status_code=500, detail=str(e))
