from pydantic import BaseModel
from typing import Optional, List, Literal

class Block(BaseModel):
    id: Optional[str]
    name: str
    type: Literal["component", "api", "style", "hook", "merged"]
    code: str
    commentary: Optional[str] = ""
    llm: Optional[str] = ""
    status: Optional[str] = "draft"

class GenerateRequest(BaseModel):
    prompt: str
    model: str

class GenerateResponse(BaseModel):
    code: str
    commentary: str
    llm_used: str

class PipelineStep(BaseModel):
    model: str
    task: str
    input_from_previous: bool = True

class PipelineRequest(BaseModel):
    prompt: str
    steps: List[PipelineStep]

class PipelineResponse(BaseModel):
    blocks: List[Block]
