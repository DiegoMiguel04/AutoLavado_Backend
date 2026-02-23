from sqlalchemy.orm import Session
import models.model_vehiculos_servicios_usuarios as model


''' Obtiene todos los registros de la tabla AutoServicio (vehículos-servicios-usuarios) '''
def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.AutoServicio)\
        .offset(skip)\
        .limit(limit)\
        .all()


''' Busca y retorna un registro específico de la tabla AutoServicio por su ID '''
def get_by_id(db: Session, registro_id: int):
    return db.query(model.AutoServicio)\
        .filter(model.AutoServicio.id == registro_id)\
        .first()


''' Crea un nuevo registro en la tabla AutoServicio con los datos proporcionados '''
def create(db: Session, data):
    nuevo = model.AutoServicio(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


''' Actualiza un registro existente de AutoServicio identificado por su ID '''
def update(db: Session, registro_id: int, data):
    registro = get_by_id(db, registro_id)
    if not registro:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(registro, key, value)

    db.commit()
    db.refresh(registro)
    return registro


''' Elimina un registro de la tabla AutoServicio utilizando su ID como referencia '''
def delete(db: Session, registro_id: int):
    registro = get_by_id(db, registro_id)
    if not registro:
        return None

    db.delete(registro)
    db.commit()
    return registro