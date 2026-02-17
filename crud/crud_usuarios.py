from sqlalchemy.orm import Session
import models.model_usuarios

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_usuarios.Usuario)\
        .offset(skip)\
        .limit(limit)\
        .all()