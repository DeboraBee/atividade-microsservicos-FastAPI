from fastapi import FastAPI # type: ignore
import requests # type: ignore
import os

app = FastAPI()


ESTOQUE_URL = os.getenv("ESTOQUE_URL")

@app.get("/produtos/{id}") 
def get_produto(id: int, delay: int = 0): 
    try:
        
        response = requests.get(f"{ESTOQUE_URL}/estoque/{id}?delay={delay}", timeout=2)
        estoque = response.json()
    except Exception:
        
        estoque = {"erro": "Serviço de estoque indisponível ou lento demais"}

    return {
        "id": id,
        "nome": f"Produto {id}", 
        "info_estoque": estoque   
    }