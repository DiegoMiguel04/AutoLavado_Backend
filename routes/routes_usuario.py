from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_usuario as crud
import schemas.schema_usuario as schema
import config.db

# Crea un router de FastAPI para manejar todas las rutas relacionadas con usuarios
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


''' Obtiene una sesión de base de datos y la cierra automáticamente después de usarla '''
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


''' Endpoint GET /usuarios - Obtiene una lista de todos los usuarios registrados '''
@router.get("/", response_model=list[schema.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)


''' Endpoint GET /usuarios/{usuario_id} - Obtiene un usuario específico por su ID '''
@router.get("/{usuario_id}", response_model=schema.Usuario)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario_by_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


''' Endpoint POST /usuarios - Crea un nuevo usuario con los datos proporcionados '''
@router.post("/", response_model=schema.Usuario)
def crear_usuario(data: schema.UsuarioCreate, db: Session = Depends(get_db)):
    if crud.get_usuario_por_correo(db, data.correo_electronico):
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return crud.create_usuario(db, data)


''' Endpoint PUT /usuarios/{usuario_id} - Actualiza un usuario existente por su ID '''
@router.put("/{usuario_id}", response_model=schema.Usuario)
def actualizar_usuario(usuario_id: int, data: schema.UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = crud.update_usuario(db, usuario_id, data)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


''' Endpoint DELETE /usuarios/{usuario_id} - Elimina un usuario específico por su ID '''
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.delete_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}
