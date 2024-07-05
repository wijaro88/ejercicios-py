from fastapi import FastAPI

app = FastAPI()

@app.get('/users')
async def read_users():
    return {"¡Hola Users!"}
