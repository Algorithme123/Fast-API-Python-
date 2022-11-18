from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class ClientBase(BaseModel):
    nom: str
    prenom: str
    dateNaissance: datetime
    profession: str
    nationalite: str
    ci: str

class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True

# Comptes

class CompteBase(BaseModel):
    numeroCompte:str
    dateCreation:date
    nomAgence:str
    nomAgent:str
    dateOperation:str
    
class CompteCreate(CompteBase):
    pass

class Compte(CompteBase):
    id=int
    proprio_id: int


    class Config:
        orm_mode=True
