from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import generate, pipeline, blocks, llms
import logging
import os

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Możesz to ograniczyć do frontendu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpointy
app.include_router(generate.router, prefix="/generate")
app.include_router(pipeline.router, prefix="/pipeline")
app.include_router(blocks.router, prefix="/block")
app.include_router(llms.router, prefix="/llms")

# Logging
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/access.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

@app.get("/")
async def root():
    return {"status": "AI Sandbox backend ready"}
