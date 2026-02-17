from sqlalchemy.orm import Session
import models.model_auto_servicio

def get_vehiculos_servicios_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_vehiculos_servicios_vehiculos.VehiculoServicioVehiculo)\
        .offset(skip)\
        .limit(limit)\
        .all()