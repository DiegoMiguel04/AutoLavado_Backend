'''Esta clase permite generar el modelo de los clientes'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de clientes'''
    __tablename__ = "tbb_client"
    
    Id = Colum(Integer, primary_key=True, index=True)
    Nombre = Colum(String(15))
    ApellidoPaterno = Colum(String(15))
    