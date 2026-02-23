from sqlalchemy.orm import Session
import models.model_vehiculos as model


''' Obtiene una lista paginada de todos los vehículos registrados en la base de datos '''
def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Vehiculo).offset(skip).limit(limit).all()


''' Busca y retorna un vehículo específico utilizando su ID como identificador único '''
def get_vehiculo_by_id(db: Session, vehiculo_id: int):
    return db.query(model.Vehiculo).filter(model.Vehiculo.id == vehiculo_id).first()


''' Crea un nuevo vehículo en la base de datos con los datos proporcionados '''
def create_vehiculo(db: Session, data):
    nuevo = model.Vehiculo(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


''' Actualiza los datos de un vehículo existente identificado por su ID '''
def update_vehiculo(db: Session, vehiculo_id: int, data):
    vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(vehiculo, key, value)

    db.commit()
    db.refresh(vehiculo)
    return vehiculo


''' Elimina un vehículo de la base de datos utilizando su ID como referencia '''
def delete_vehiculo(db: Session, vehiculo_id: int):
    vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        return None

    db.delete(vehiculo)
    db.commit()
    return vehiculo