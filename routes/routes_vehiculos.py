from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_vehiculos as crud
import schemas.schema_vehiculos as schema
import config.db

# Crea un router de FastAPI para manejar todas las rutas relacionadas con vehículos
router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])


''' Obtiene una sesión de base de datos y la cierra automáticamente después de usarla '''
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


''' Endpoint GET /vehiculos - Obtiene una lista paginada de todos los vehículos registrados '''
@router.get("/", response_model=list[schema.Vehiculo])
def listar_vehiculos(db: Session = Depends(get_db)):
    return crud.get_vehiculos(db)


''' Endpoint GET /vehiculos/{vehiculo_id} - Obtiene un vehículo específico por su ID '''
@router.get("/{vehiculo_id}", response_model=schema.Vehiculo)
def obtener_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = crud.get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo


''' Endpoint POST /vehiculos - Crea un nuevo vehículo con los datos proporcionados '''
@router.post("/", response_model=schema.Vehiculo)
def crear_vehiculo(data: schema.VehiculoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo(db, data)


''' Endpoint PUT /vehiculos/{vehiculo_id} - Actualiza un vehículo existente por su ID '''
@router.put("/{vehiculo_id}", response_model=schema.Vehiculo)
def actualizar_vehiculo(vehiculo_id: int, data: schema.VehiculoUpdate, db: Session = Depends(get_db)):
    vehiculo = crud.update_vehiculo(db, vehiculo_id, data)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo


''' Endpoint DELETE /vehiculos/{vehiculo_id} - Elimina un vehículo específico por su ID '''
@router.delete("/{vehiculo_id}")
def eliminar_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = crud.delete_vehiculo(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return {"mensaje": "Vehículo eliminado correctamente"}