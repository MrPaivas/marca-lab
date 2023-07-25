from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new-user/", response_model=schemas.Usuarios)
def create_user(user: schemas.UsuariosCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já registrado!!")
    return crud.create_user(db, user)


@app.get('/users/', response_model=list[schemas.Usuarios])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get('/users/{user_id}', response_model=schemas.Usuarios)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")


@app.post('/lab/', response_model=schemas.Lab)
def create_lab(user: schemas.Usuarios, lab: schemas.LabCreate, db: Session =Depends(get_db)):
    db_user = crud.get_user_by_id(db, user.id)
    if db_user.tipo != "Administrador":
        raise HTTPException(status_code=403, detail="Usuario sem permissão para criar um Laboratório")
    return crud.create_lab(db, lab)

