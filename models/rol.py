'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from config.db import Base

class Rol(Base):
    '''Clase para especificar tabla de roles de usuarios'''
    __tablename__ = "tbc_roles"
    
    Id = Colum(Integer, primary_key=True, index=True)
    nombreRol = Colum(String(15))
    estado = Colum(Boolean)
