# Clase en vídeo: https://youtu.be/_y9qQZXE24A

### Hola Mundo ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from typing import Union

app =FastAPI()

#url local: http://127.0.0.1:8000
@app.get('/')
def read_root():
    return {"¡Hola FastApi!"}

#url local: http://127.0.0.1:8000/items/{item_id}

@app.get("/items/{item_id}")
async def read_item(item_id:int, q: Union[str, None]= None):
    return {"item_id":item_id, "q":q}    

# Inicia el server: uvicorn main:app --reload
# Destener el server: CTRL + C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc