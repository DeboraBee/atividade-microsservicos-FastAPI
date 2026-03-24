from fastapi import FastAPI # type: ignore
import asyncio

app = FastAPI()


@app.get("/estoque/{id}")
async def get_estoque(id: int, delay: int = 0):
    
    if delay > 0:
        await asyncio.sleep(delay)

    
    estoque_db = {
        1: {"id": 1, "item": "Teclado Mecânico", "quantidade": 15},
        2: {"id": 2, "item": "Mouse Gamer", "quantidade": 0},
        3: {"id": 3, "item": "Monitor 144hz", "quantidade": 7}
    }

    return estoque_db.get(id, {"erro": "Item não encontrado no estoque"})