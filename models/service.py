'''Esta clase permite generar el modelo para los tipos de servicio'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de servicio'''
    __tablename__ = "tbc_servicio"
    
    Id = Colum(Integer, primary_key=True, index=True)
    Auto_Service_Id = Colum(Integer, ForeignKey("tbb_auto_service.Id"))
    