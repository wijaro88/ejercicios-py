from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user

#baseModel nos deja crear el objeto 
class User(BaseModel):
    name:str
    surname:str
    url:str
    age:int

users_list = [User(name="wilson",surname="javier",url="https://wilss.com",age=33),
         User(name="wilson33",surname="javier",url="https://wilss.com",age=34),
         User(name="wilson44",surname="javier",url="https://wilss.com",age=35)]


@app.get('/usersjson')
async def usersjson():
    return [{"name":"wilson", "surname":"javier","url":"https://wilss.com","age":33},      
            {"name":"wilson2", "surname":"javier2","url":"https://wilss3.com","age":34},
            {"name":"wilson3", "surname":"javier3","url":"https://wilss2.com","age":35}]


@app.get("/users")
async def users():
    return users_list
