from fastapi import FastAPI
from db import Base, engine
import products
import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Loja de Copos + Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(products.router)
app.include_router(chat.router)
