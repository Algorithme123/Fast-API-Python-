from multiprocessing.connection import Client
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# import models, schemas, crud
import models, schemas
import crud
# from  .models import models
# from  .schemas import schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/') 
def  read_root(): 
    return { 
        "hello" : "world" 
    } 



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/Client/', response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_id(db, ci=client.ci)

    if db_client:
        raise HTTPException(status_code=400, detail="Cette numero de carte D'identiter existe deja")

    return crud.create_client(db=db, client=client)


@app.get('/clients/', response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)

    return clients


@app.get('/clients/{client_id}', response_model=schemas.Client)
def read_Client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_user(db, client_id=client_id)

    if not db_client:
        raise HTTPException(status_code=404, detail="Client non trouver.")

    return db_client

@app.put("/clients/{id}")
async def update_client(id:int): 
    # client=client.prenom+ "/"+ client.nom 
    # client_dict=client.dict() 
    # client_dict.update({"ci":client}) 
    # return client_dict 
    pass

@app.delete("/clients/{id}")
def deleteClient(id:int):
    client= {"clients_id":client} 
    client_dict=client.dict() 
    del client
    return client_dict
     

@app.post('/clients/{client_id}/banque/', response_model=schemas.Compte)
def create_compte_banquaire_client(client_id: int, comptes: schemas.CompteCreate, db: Session = Depends(get_db)):
    return crud.create_compte_client(db=db, comptes=comptes, client_id=client_id)


@app.get('/Comptes/', response_model=List[schemas.Compte])
def read_comptes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comptes = crud.get_comptes(db, skip=skip, limit=limit)

    return comptes
@app.delete("/comptes/{id}")
def deleteComptes(id:int):
    comptes= {"comptes_id":client} 
    comptes_dict=comptes.dict() 
    del comptes
    return comptes_dict