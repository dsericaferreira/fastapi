from fastapi import FastAPI
from pydantic import BaseModel
from fibonnaci import Fibonacci

app = FastAPI()

class FibonacciRequest(BaseModel):
    lista: int

@app.get("/api/health")
def health_check():
    return "Estou saudavel!!! :)"

@app.post("/api/fibonacci")
def calculate_fibonacci(request: FibonacciRequest):
    lista = request.lista
    reques_resul = Fibonacci().calculate(lista)  # Usando a classe Fibonacci para calcular a sequência
    return reques_resul