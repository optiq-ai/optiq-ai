from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
import logging

router = APIRouter()

# Prosty storage w pamięci – wersja MVP (docelowo: baza danych)
blocks_db = {}

class Block(BaseModel):
    id: Optional[str]
    name: str
    type: str  # np. component, api, style
    code: str
    commentary: Optional[str] = ""
    llm: Optional[str] = ""
    status: Optional[str] = "draft"

@router.post("/", response_model=Block)
async def create_block(block: Block):
    block_id = str(uuid.uuid4())
    block.id = block_id
    blocks_db[block_id] = block
    logging.info(f"Dodano blok: {block.name}")
    return block

@router.get("/", response_model=List[Block])
async def get_all_blocks():
    return list(blocks_db.values())

@router.get("/{block_id}", response_model=Block)
async def get_block(block_id: str):
    block = blocks_db.get(block_id)
    if not block:
        raise HTTPException(status_code=404, detail="Blok nie istnieje")
    return block

@router.put("/{block_id}", response_model=Block)
async def update_block(block_id: str, updated: Block):
    if block_id not in blocks_db:
        raise HTTPException(status_code=404, detail="Nie znaleziono bloku")
    blocks_db[block_id] = updated
    return updated

@router.post("/merge", response_model=Block)
async def merge_blocks(ids: List[str]):
    merged_code = ""
    merged_commentary = ""
    for block_id in ids:
        block = blocks_db.get(block_id)
        if block:
            merged_code += f"\n\n// --- {block.name} ---\n{block.code}"
            merged_commentary += f"\n\n# {block.name}\n{block.commentary}"
    merged_block = Block(
        id=str(uuid.uuid4()),
        name="Merged Block",
        type="merged",
        code=merged_code.strip(),
        commentary=merged_commentary.strip()
    )
    blocks_db[merged_block.id] = merged_block
    return merged_block
