from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from db import get_db
from models import Product
import google.generativeai as genai
import os
import re

router = APIRouter(prefix="/chat", tags=["chat"])

# ===================== IA =====================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

def gerar_resposta_ia(prompt: str) -> str:
    result = model.generate_content(
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )
    return result.text.strip()

# ===================== REGRAS DE NEGÓCIO =====================

PALAVRAS_COPOS = {
    "copo", "copos", "taça", "caneca", "estoque", "preço",
    "valor", "quantos", "tem", "disponível"
}

CORES = {
    "azul": "azul",
    "azuis": "azul",
    "vermelho": "vermelho",
    "vermelhos": "vermelho",
    "verde": "verde",
    "verdes": "verde",
    "roxo": "roxo",
    "roxos": "roxo",
    "lilás": "lilás",
    "lilas": "lilás",
    "preto": "preto",
    "pretos": "preto",
    "branco": "branco",
    "brancos": "branco",
    "laranja": "laranja",
    "cinza": "cinza"
}

def mensagem_relacionada_a_copos(msg: str) -> bool:
    return any(p in msg for p in PALAVRAS_COPOS)

def detectar_cor(msg: str):
    for palavra in re.findall(r"\w+", msg.lower()):
        if palavra in CORES:
            return CORES[palavra]
    return None

# ===================== ENDPOINT =====================
@router.post("/")
def chat(data: dict = Body(...), db: Session = Depends(get_db)):

    message = data.get("message", "").lower().strip()
    if not message:
        return {"response": "Mensagem inválida."}

    # 1️⃣ Escopo
    if not mensagem_relacionada_a_copos(message):
        return {"response": "Atendemos apenas sobre copos."}

    # 2️⃣ INTENÇÃO ESPECÍFICA (COR)
    cor = detectar_cor(message)

    if cor:
        produto = db.query(Product).filter(
            Product.name.ilike(f"%{cor}%")
        ).first()

        if not produto:
            return {"response": f"No momento não temos copo {cor} em estoque."}

        prompt = f"""
Use EXATAMENTE estas informações.
Não invente dados.
Não cumprimente.
Não faça perguntas.

Resposta obrigatória:
Temos {produto.stock} unidades do {produto.name} disponíveis no estoque.
O valor de cada unidade é R$ {produto.price}.
"""
        return {"response": gerar_resposta_ia(prompt)}

    # 3️⃣ PERGUNTA GERAL (LISTAGEM)
    produtos = db.query(Product).all()
    if not produtos:
        return {"response": "Nenhum copo disponível no estoque no momento."}

    lista = ""
    for p in produtos:
        lista += f"- {p.name}: R$ {p.price} ({p.stock} unidades)\n"

    prompt = f"""
Use SOMENTE as informações abaixo.
Não invente valores.
Não faça perguntas.

Copos disponíveis no estoque no momento:
{lista}
"""
    return {"response": gerar_resposta_ia(prompt)}
