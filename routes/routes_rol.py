from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

import schemas.schema_rol
import crud.crud_rol
import config.db
import models.model_rol

rol = APIRouter()

models.model_rol.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol.get(
    "/roles/",
    response_model=List[schemas.schema_rol.Rol],
    tags=["Roles"]
)
async def read_roles(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    db_rol = crud.crud_rol.get_rol(db=db, skip=skip, limit=limit)
    return db_rol