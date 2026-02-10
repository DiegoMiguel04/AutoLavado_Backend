''' Docstring for schemas.schema_vehiculo'''
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class VehiculoBase(BaseModel):
    '''Clase para modelar los campos de la tabla Vehiculo'''
    marca: str
    modelo: str
    placa: str
    serie: str
    color: str
    tipo: str
    anio: str
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-public-methods, unnecesary-pass
class VehiculoCreate(VehiculoBase):
    '''Clase para crear un Vehiculo basado en la tabla Vehiculo'''
    pass

class VehiculoUpdate(VehiculoBase):
    '''Clase para actualizar un Vehiculo basado en la tabla Vehiculo'''
    pass

class Vehiculo(VehiculoBase):
    '''Clase para realizar operaciones por ID en tabla Vehiculo'''
    id: int
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode = True
