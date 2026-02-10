''' Docstring for schemas.schema_rol'''
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    '''Clase para modelar los campos de la tabla Rol'''
    fecha: date
    hora: time
    estatus: str
    estado: str
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-public-methods, unnecesary-pass
class RolCreate(RolBase):
    '''Clase para crear un Rol basado en la tabla Rol'''
    pass

class RolUpdate(RolBase):
    '''Clase para actualizar un Rol basado en la tabla Rol'''
    pass

class Rol(RolBase):
    '''Clase para realizar operaciones por ID en tabla Rol'''
    id: int
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode = True
