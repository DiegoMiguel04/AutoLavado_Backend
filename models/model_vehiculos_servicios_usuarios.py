'''Esta clase permite generar el modelo de los autos'''
from sqlalchemy import Column, Integer, Boolean, DateTime, Time, Enum, DateTime, ForeignKey
from config.db import Base
from datetime import datetime

class Estatus(Enum):
    Programado = "Programado"
    Proceso = "En proceso"
    Realizado = "Realizado"
# pylint : disable=too-few-public-methods
class VehiculoServicio(Base):
    '''Clase para especificar la tabla de autos'''
    __tablename__ = "tbd_vehiculos_servicios_usuario"

    Id = Column("Id", Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    cajero_Id = Column(Integer, ForeignKey("tbb_vehiculos.Id"))
    operador_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    servicio_Id = Column(Integer, ForeignKey("tbc_servicios.Id"))
    fecha = Column(DateTime)
    hora = Column(Time)
    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    