'''Esta clase permite generar el modelo de los autos'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from config.db import Base
from datetime import datetime

class User(Base):
    '''Clase para especificar la tabla de autos'''
    __tablename__ = "tbb_auto"
    
    Id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column("usuario_Id", Integer, ForeignKey("tbb_usuarios.Id"))
    marca = Column(String(60), nullable=False)
    modelo = Column(String(10), nullable=False)
    placa = Column(String(10), nullable=False, unique=True)
    serie = Column(String(60), nullable=False)
    color = Column(String(60), nullable=False)
    tipo = Column(String(50), nullable=False)
    anio = Column(Integer, nullable=False)
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
