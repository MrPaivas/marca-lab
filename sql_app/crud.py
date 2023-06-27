from sqlalchemy.orm import Session


from database import SessionLocal
import models
import schemas


def get_user(db: Session, user_id: int):
    busca = db.query(models.Usuarios).filter(models.Usuarios.id == user_id).first()
    return busca


def get_lab_by_id(db: Session, lab_id: int):
    busca = db.query(models.Lab).filter(models.Lab.id == lab_id).first()
    return busca


def get_labs(db: Session):
    busca = db.query(models.Lab).all()
    return busca


def get_users(db: Session):
    busca = db.query(models.Usuarios).all()
    return busca


def get_booking_by_id(db: Session, book_id: int):
    busca = db.query(models.Marcacoes).filter(models.Marcacoes.id == book_id).first()
    return busca


def get_booking_by_lab_id(db: Session, lab_id: int):
    busca = db.query(models.Marcacoes).filter(models.Marcacoes.id_lab == lab_id).all()
    return busca


def get_booking_by_user_id(db: Session, user_id: int):
    busca = db.query(models.Marcacoes).filter(models.Marcacoes.id_user == user_id).all()
    return busca


def get_bookings(db: Session):
    busca = db.query(models.Marcacoes).all()
    return busca


def create_user(db: Session, user: schemas.UsuariosCreate):  
    db_user = models.Usuarios(
        nome=user.nome,
        email=user.email,
        telefone=user.telefone,
        funcao=user.funcao,
        tipo=user.tipo,
        senha=user.senha
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_lab(db: Session, lab: schemas.LabCreate):
    db_lab = models.Lab(
        nome=lab.nome,
        lotacao=lab.lotacao,
        softwares=lab.softwares,
        descricao=lab.descricao,
        id_responsavel=lab.id_responsavel
    )
    db.add(db_lab)
    db.commit()
    db.refresh(db_lab)
    return db_lab


def create_booking(db: Session, book: schemas.MarcacoesCreate):
    booking = models.Marcacoes(
        id_lab = book.id_lab,
        id_user = book.id_user,
        material = book.material,
        descricao = book.descricao,
        data_inicio = book.data_inicio,
        data_final = book.data_final
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking