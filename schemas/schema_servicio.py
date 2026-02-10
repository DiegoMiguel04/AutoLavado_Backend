''' Docstring for schemas.schema_servicio'''
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class ServicioBase(BaseModel):
    '''Clase para modelar los campos de la tabla Servicio'''
    nombre: str
    description: str
    costo: float
    duracion: int
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-public-methods, unnecesary-pass
class ServicioCreate(ServicioBase):
    '''Clase para crear un Servicio basado en la tabla Servicio'''
    pass

class ServicioUpdate(ServicioBase):
    '''Clase para actualizar un Servicio basado en la tabla Servicio'''
    pass

class Servicio(ServicioBase):
    '''Clase para realizar operaciones por ID en tabla Servicio'''
    id: int
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode = True
