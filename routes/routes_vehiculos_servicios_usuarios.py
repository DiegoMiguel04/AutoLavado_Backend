from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_vehiculos_servicios_usuarios as crud
import schemas.schema_vehiculos_servicios_usuarios as schema
import config.db

# Crea un router de FastAPI para manejar todas las rutas relacionadas con la tabla AutoServicio
router = APIRouter(prefix="/vehiculos-servicios-usuarios", tags=["AutoServicio"])


''' Obtiene una sesión de base de datos y la cierra automáticamente después de usarla '''
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


''' Endpoint GET /vehiculos-servicios-usuarios - Obtiene una lista paginada de todos los registros
de la tabla AutoServicio que relaciona vehículos, servicios y usuarios '''
@router.get("/", response_model=list[schema.AutoServicio])
def listar(db: Session = Depends(get_db)):
    return crud.get_all(db)


''' Endpoint GET /vehiculos-servicios-usuarios/{registro_id} - Obtiene un registro específico por su ID '''
@router.get("/{registro_id}", response_model=schema.AutoServicio)
def obtener(registro_id: int, db: Session = Depends(get_db)):
    registro = crud.get_by_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


''' Endpoint POST /vehiculos-servicios-usuarios - Crea un nuevo registro de relación
entre vehículo, servicio y usuario con los datos proporcionados '''
@router.post("/", response_model=schema.AutoServicio)
def crear(data: schema.AutoServicioCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


''' Endpoint PUT /vehiculos-servicios-usuarios/{registro_id} - Actualiza un registro existente por su ID '''
@router.put("/{registro_id}", response_model=schema.AutoServicio)
def actualizar(registro_id: int, data: schema.AutoServicioUpdate, db: Session = Depends(get_db)):
    registro = crud.update(db, registro_id, data)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


''' Endpoint DELETE /vehiculos-servicios-usuarios/{registro_id} - Elimina un registro específico por su ID '''
@router.delete("/{registro_id}")
def eliminar(registro_id: int, db: Session = Depends(get_db)):
    registro = crud.delete(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro eliminado correctamente"}
