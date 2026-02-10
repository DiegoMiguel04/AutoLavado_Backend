'''Esta clase permite generar el modelo de los autos'''
from sqlalchemy import Colum, Integer, String, Boolean, Date, DateTime, Time, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Estatus(Enum):
    Programado = "Programado"
    Proceso = "En proceso"
    Realizado = "Realizado"
# pylint : disable=too-few-public-methods
class VehiculoServicio(Base):
    '''Clase para especificar la tabla de autos'''
    __tablename__ = "tbd_vehiculos_servicios_usuario"

    Id = Colum(Integer, primary_key=True, index=True)
    vehiculo_id = Colum(Integer, ForeignKey("tbb_usuarios.Id"))
    cajero_Id = Colum(Integer, ForeignKey("tbb_vehiculos.Id"))
    operador_Id = Colum(Integer, ForeignKey("tbb_usuarios.Id"))
    servicio_Id = Colum(Integer, ForeignKey("tbc_servicios.Id"))
    fecha = Colum(Date)
    hora = Colum(Time)
    estatus = Colum(Enum(Estatus), default=Estatus.Programado)
    estado = Colum(Boolean)
    fecha_registro = Colum(DateTime)
    fecha_actualizacion = Colum(DateTime)
    