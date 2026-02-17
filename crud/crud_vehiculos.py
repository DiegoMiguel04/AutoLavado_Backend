from sqlalchemy.orm import Session
import models.model_vehiculos

def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_vehiculos.Vehiculo)\
        .offset(skip)\
        .limit(limit)\
        .all()