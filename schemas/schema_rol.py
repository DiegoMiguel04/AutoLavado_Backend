''' Docstring for schemas.schema_rol'''
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    '''Clase para modelar los campos de la tabla Rol'''
    nombre: str
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-public-methods, unnecesary-pass
class RolCreate(RolBase):
    '''Clase para crear un Rol basado en la tabla Rol'''
    nombre: str
    pass

class RolUpdate(RolBase):
    '''Clase para actualizar un Rol basado en la tabla Rol'''
    nombre: str | None = None
    estatus: bool | None = None
    pass

class Rol(RolBase):
    '''Clase para realizar operaciones por ID en tabla Rol'''
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode = True
