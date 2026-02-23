from pydantic import BaseModel
from datetime import datetime, time


''' Modelo base para la tabla AutoServicio que relaciona vehículos, cajeros, operadores y servicios '''
class AutoServicioBase(BaseModel):
    vehiculo_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: datetime
    hora: time
    estatus: bool = True


''' Modelo utilizado para la creación de un nuevo registro de AutoServicio '''
class AutoServicioCreate(BaseModel):
    vehiculo_id: int
    cajero_id: int
    operador_id: int
    servicio_id: int
    fecha: datetime
    hora: time


''' Modelo utilizado para la actualización de un registro existente de AutoServicio '''
class AutoServicioUpdate(BaseModel):
    vehiculo_id: int | None = None
    cajero_id: int | None = None
    operador_id: int | None = None
    servicio_id: int | None = None
    fecha: datetime | None = None
    hora: time | None = None
    estatus: bool | None = None


''' Modelo completo de AutoServicio que se utiliza para las respuestas de la API '''
class AutoServicio(AutoServicioBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
