'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de usuarios'''
    __tablename__ = "tbb_usuarios"
    
    Id = Colum(Integer, primary_key=True, index=True)
    Rol_Id = Colum(Integer, ForeignKey("tbc_roles.Id"))
    Nombre = Colum()
    