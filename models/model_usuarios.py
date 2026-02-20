'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime
from passlib.context import CryptContext
from passlib.exc import UnknownHashError

class User(Base):
    '''Clase para especificar la tabla de usuarios'''
    __tablename__ = "tbb_usuarios"
    
    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column("rol_Id", Integer, ForeignKey("tbc_roles.Id"))
    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    direccion = Column(String(200))
    correo_electronico = Column(String(100))
    numero_telefono = Column(String(20))
    contrasena = Column(String(40))
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Columnn(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    rols = relationship("Rol", back_populates="usuarios")
    vehiculos = relationship()
    servicio = relationship()


