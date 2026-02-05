'''Esta clase permite generar el modelo de los autos'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de autos'''
    __tablename__ = "tbb_auto"
    
    Id = Colum(Integer, primary_key=True, index=True)
    NombreAuto = Colum(String(15))
    