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


@app.post("/create-user/", response_model=schemas.Usuarios)
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
    return db_user


@app.post('/create-lab/{user_id}', response_model=schemas.Lab)
def create_lab(user_id: int, lab: schemas.LabCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user.tipo != "Administrador":
        raise HTTPException(status_code=403, detail="Usuario sem permissão para criar um Laboratório")
    return crud.create_lab(db, lab)


@app.get('/labs/', response_model=list[schemas.Lab])
def read_labs(db: Session = Depends(get_db)):
    db_labs = crud.get_labs(db)
    return db_labs


@app.post('/create-booking/', response_model=schemas.Marcacoes)
def create_booking(new_book: schemas.MarcacoesCreate, db: Session = Depends(get_db)):
    db_book = crud.get_bookings(db)
    for book in db_book:
        if book.data_inicio == new_book.data_inicio:
            if book.id_lab == new_book.id_lab:
                raise HTTPException(status_code=409, detail="Horário não Disponível")
    return crud.create_booking(db, new_book)


@app.get('/bookings/', response_model= list[schemas.Marcacoes])
def read_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)