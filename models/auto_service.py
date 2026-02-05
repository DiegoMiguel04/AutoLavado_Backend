'''Esta clase permite generar el modelo para el auto servicio'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de auto servicio'''
    __tablename__ = "tbb_auto_service"
    
    Id = Colum(Integer, primary_key=True, index=True)
    Auto_Id = Colum(Integer, ForeignKey("tbb_auto.Id"))
    Nombre = Colum()
    