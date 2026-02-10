'''Esta clase permite generar el modelo de los autos'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de autos'''
    __tablename__ = "tbb_auto"
    
    Id = Colum(Integer, primary_key=True, index=True)
    usuario_id = Colum(Integer, ForeignKey("tbb_usuarios.Id"))
    marca = Colum(String(60))
    modelo = Colum(String(10))
    placa = Colum(String(10))
    serie = Colum(String(60))
    color = Colum(String(60))
    tipo = Colum(String(50))
    anio = Colum(Integer)
    estatus = Colum(Boolean)
    fecha_registro = Colum(DateTime)
    fecha_actualizacion = Colum(DateTime)
    