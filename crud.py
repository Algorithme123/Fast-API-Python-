from http import client
from sqlalchemy.orm import Session

import models, schemas

# from  .models import models
# from  .schemas import schemas



def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_client_by_ci(db: Session, ci: str):
    return db.query(models.Client).filter(models.Client.ci == ci).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
 
    db_client = models.Client(nom=client.nom,prenom=client.prenom,dateNaissance=client.dateNaissance,profession=client.profession,nationalite=client.nationalite,ci=client.ci )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


def get_comptes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Compte).offset(skip).limit(limit).all()


def create_compte_client(db: Session, comptes: schemas.Compte, client_id: int):
    db_comptes = models.Compte(**comptes.dict(), proprio_id=client_id,numeroCompte=comptes.numeroCompte,dateCreation=comptes.dateCreation,nomAgence=comptes.nomAgence,nomAgent=comptes.nomAgent,soldeInitiale=comptes.soldeInitiale,dateOperation=comptes.dateOperation)
    db.add(db_comptes)
    db.commit()
    db.refresh(db_comptes)

    return db_comptes

