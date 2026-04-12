from fastapi import FastAPI

app = FastAPI()

@app.post("/wl/fight/{id}")
def fight(id: int):
    return {"message": f"Fighting with id {id}"}

@app.post("/wl/battle/{id}")
def legion(id: int):
    return {"message": f"Battling with id {id}"}