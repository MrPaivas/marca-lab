from pydantic import BaseModel

class MarcacoesBase(BaseModel):
    material: str
    descricao: str
    data_inicio: str
    data_final: str


class MarcacoesCreate(MarcacoesBase):
    pass


class Marcacoes(MarcacoesBase):
    id: int


class LabBase(BaseModel):
    nome: str
    lotacao: int
    softwares: str | None = None
    descricao: str | None = None
    

class LabCreate(LabBase):
    id_responsavel: int


class Lab(LabBase):
    id: int
    aulas: list[Marcacoes] = []

    class Config:
        orm_mode = True