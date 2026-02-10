'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Colum, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    '''Clase para especificar la tabla de usuarios'''
    __tablename__ = "tbb_usuarios"
    
    Id = Colum(Integer, primary_key=True, index=True)
    rol_Id = Colum(Integer, ForeignKey("tbc_roles.Id"))
    nombre = Colum(String(60))
    primer_apellido = Colum(String(60))
    segundo_apellido = Colum(String(60))
    direccion = Colum(String(200))
    correo_electronico = Colum(String(100))
    numero_telefono = Colum(String(20))
    contrasena = Colum(String(40))
    estatus = Colum(Boolean)
    fecha_registro = Colum(DateTime)
    fecha_actualizacion = Colum(DateTime)
    