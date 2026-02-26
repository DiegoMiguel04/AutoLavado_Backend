from fastapi import FastAPI, Depends
from routes.routes_rol import rol
from routes.routes_usuario import usuario
from routes.routes_servicio import servicio
from routes.routes_vehiculo import vehiculo
from routes.routes_usuario_vehiculo_servicio import usuario_vehiculo_servicio
from config.security import get_current_user

app = FastAPI(
    title="Proyecto Autolavado 230260",
    description="API segura de almacenamiento de informacion para administrar un autolavado Diego Miguel Rivera Chávez"

)

app.include_router(rol)
app.include_router(usuario)
app.include_router(vehiculo, dependencies=[Depends(get_current_user)])
app.include_router(servicio, dependencies=[Depends(get_current_user)])
app.include_router(usuario_vehiculo_servicio, dependencies=[Depends(get_current_user)])

