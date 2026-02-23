from pydantic import BaseModel
from datetime import datetime

''' Modelo base para la tabla de vehículos '''
class VehiculoBase(BaseModel):
    usuario_id: int
    modelo: str
    marca: str
    placa: str
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool = True


''' Modelo utilizado para la creación de un nuevo vehículo '''
class VehiculoCreate(BaseModel):
    usuario_id: int
    modelo: str
    marca: str
    placa: str
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None


''' Modelo utilizado para la actualización de un vehículo existente '''
class VehiculoUpdate(BaseModel):
    usuario_id: int | None = None
    modelo: str | None = None
    marca: str | None = None
    placa: str | None = None
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool | None = None


''' Modelo completo de Vehículo que se utiliza para las respuestas de la API '''
class Vehiculo(VehiculoBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
