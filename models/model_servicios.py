'''Esta clase permite generar el modelo para los tipos de servicio'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de servicio'''
    __tablename__ = "tbc_servicios"
    
    Id = Colum(Integer, primary_key=True, index=True)
    nombre = Colum(String(60))
    descripcion = Column(String(150))
    costo = Column(Float)
    duracion = Column(Integer)
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    '''Auto_Service_Id = Colum(Integer, ForeignKey("tbb_auto_service.Id"))'''
    