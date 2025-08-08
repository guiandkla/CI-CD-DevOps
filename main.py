from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/message")
async def root():
    return {"message": "Hello World! Bem vindo ao teste."}

@app.get("/num")
async def funcaonumero():
    return {"numero_aleatorio": random.randint(0, 200)}

@app.get("/name")
async def funcaonome():
    return {"name": "Guilherme Andrei Klabunde"}