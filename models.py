from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from db import Base


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    dateNaissance = Column(String, index=True)
    profession = Column(String, index=True)
    nationalite = Column(String, index=True)
    ci = Column(String)
    comptes = relationship('Compte', back_populates='proprio')


class Compte(Base):
    __tablename__ = 'compte'

    id = Column(Integer, primary_key=True, index=True)
    numeroCompte = Column(String, index=True)
    dateCreation = Column(Date, index=True)
    nomAgence = Column(String, index=True)
    nomAgent = Column(String, index=True)
    soldeInitiale = Column(Integer, index=True)
    dateOperation = Column(Date, index=True)
    proprio_id = Column(Integer, ForeignKey('client.id'))

    proprio = relationship('Client', back_populates='comptes')
