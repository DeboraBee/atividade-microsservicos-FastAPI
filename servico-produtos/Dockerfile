FROM python:3.11-slim

WORKDIR /app

# Copia os requisitos (fastapi, uvicorn, requests)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Mantemos a porta 8000 para o serviço de Produtos
EXPOSE 8000

# O comando roda na porta 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]