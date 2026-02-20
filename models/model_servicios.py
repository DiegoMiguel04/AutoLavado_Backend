'''Esta clase permite generar el modelo para los tipos de servicio'''
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class User(Base):
    '''Clase para especificar la tabla de servicio'''
    __tablename__ = "tbc_servicios"
    
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60), nullable=False)
    descripcion = Column(String(150), nullable=False)
    costo = Column(Float, nullable=False)
    duracion = Column(Integer)
    estado = Column(Boolean, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    '''Auto_Service_Id = Colum(Integer, ForeignKey("tbb_auto_service.Id"))'''
    