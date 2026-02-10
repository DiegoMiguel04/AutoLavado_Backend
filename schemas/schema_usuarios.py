''' Docstring for schemas.schema_usuario'''
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    '''Clase para modelar los campos de la tabla Usuario'''
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    contrasena: str
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-public-methods, unnecesary-pass
class UsuarioCreate(UsuarioBase):
    '''Clase para crear un Usuario basado en la tabla Usuario'''
    pass

class UsuarioUpdate(UsuarioBase):
    '''Clase para actualizar un Usuario basado en la tabla Usuario'''
    pass

class Usuario(UsuarioBase):
    '''Clase para realizar operaciones por ID en tabla Usuario'''
    id: int
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode = True

class UsuarioLogin(BaseModel):
    '''Clase para realizar login por numero de telefono o correo'''
    numero_telefono: Optional[str] = None 
    correo_electronico: Optional[str] = None 
    contrasena: str 
