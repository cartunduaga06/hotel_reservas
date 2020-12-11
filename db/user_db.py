from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    nombres: str
    apellidos: str
    direccion: str
    telefono: str
    email: str
    nacionalidad: str
    
    

    

database_users = Dict[str, UserInDB]

database_users = {
    "carlos": UserInDB(**{"username":"carlos",
                            "password":"root",
                            "nombres": "carlos andres",
                            "apellidos":"artunduaga",
                            "direccion":"Carrera 14",
                            "telefono":"3126482921",
                            "email":"cartunduaga@gmail.com",
                            "nacionalidad":"colombiano",

                            }),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "nombres": "carlos andres",
                            "apellidos":"artunduaga",
                            "direccion":"Carrera 14",
                            "telefono":"3126482921",
                            "email":"cartunduaga@gmail.com",
                            "nacionalidad":"colombiano",
                            }),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
