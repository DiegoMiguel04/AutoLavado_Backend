from sqlalchemy.orm import Session
import models.model_servicios

def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_servicios.Servicio)\
        .offset(skip)\
        .limit(limit)\
        .all()