from db.user_db import UserInDB
from db.user_db import update_user, get_user
from models.user_models import UserIn, UserOut
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

api = FastAPI()

db = []


class Habitacion (BaseModel):
    nombre: str
    tipo: str
    numero: int 
    descripcion: str
    caracteristicas: str
    precio: int
    


@api.get('/')
def index():
    return {'key' : 'hola'}

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get('/habitaciones')
def get_habitaciones():
    return db 

@api.get('/habitaciones/{habitacion_id}')
def get_habitacion(habitacion_id: int):
    return db[habitacion_id-1]


@api.post('/habitaciones')
def crear_habitacion (habitacion: Habitacion):
    db.append(habitacion.dict())
    return db[-1]

@api.delete('/habitaciones/{habitacion_id}')
def delete_habitacion(habitacion_id: int):
    db.pop(habitacion_id-1)
    return {}
