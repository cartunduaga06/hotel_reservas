from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
   

class UserOut(BaseModel):
    username: str
    nombres: str
    apellidos: str
    direccion: str
    telefono: str
    email: str
    nacionalidad: str