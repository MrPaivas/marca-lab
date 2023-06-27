from sqlalchemy import Integer, String, ForeignKey, Column, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    email = Column(String, nullable=True)
    telefone = Column(String, nullable=True)
    funcao = Column(String, nullable=True)
    tipo = Column(String, nullable=True)
    senha = Column(String, nullable=True)


class Lab(Base):
    __tablename__ = 'laboratorio'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    lotacao = Column(Integer, nullable=True)
    softwares = Column(String)
    descricao = Column(String)
    id_responsavel = Column(Integer, ForeignKey("usuarios.id"))

    aulas = relationship("Marcacoes", back_populates="labs")


class Marcacoes(Base):
    __tablename__ = 'marcacoes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_lab = Column(Integer, ForeignKey("laboratorio.id"))
    id_user = Column(Integer, ForeignKey("usuarios.id"))
    material = Column(String, nullable=True)
    descricao = Column(String, nullable=True)
    data_inicio = Column(DateTime, nullable=False)
    data_final = Column(DateTime, nullable=False)

    labs = relationship("Lab", back_populates="aulas")