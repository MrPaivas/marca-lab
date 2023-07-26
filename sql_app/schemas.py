from pydantic import BaseModel


class MarcacoesBase(BaseModel):
    material: str
    descricao: str
    data_inicio: str
    data_final: str | None = None


class MarcacoesCreate(MarcacoesBase):
    id_lab: int
    id_user: int


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

    class Config:
        orm_mode = True


class UsuariosBase(BaseModel):
    nome: str
    email: str
    telefone: str
    funcao: str
    tipo: str


class UsuariosCreate(UsuariosBase):
    senha: str


class Usuarios(UsuariosBase):
    id: int

    class Config:
        orm_mode = True