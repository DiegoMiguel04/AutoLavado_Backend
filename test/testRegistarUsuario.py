import pytest
from fastapi.testclient import TestClient
from main import app # Ajusta la importación a tu archivo principal

client = TestClient(app)

def test_crear_usuario_exitoso():
    # Datos exactos de tu endpoint
    payload = {
        "rol_Id": 1,
        "nombre": "Test",
        "primer_apellido": "Test",
        "segundo_apellido": "Test",
        "direccion": "Tes",
        "correo_electronico": "test@test.com",
        "numero_telefono": "0000000000",
        "contrasena": "test",
        "estado": True,
        "fecha_registro": "2026-02-24T20:05:05.948Z",
        "fecha_actualizacion": "2026-02-24T20:05:05.948Z"
    }

    # Petición POST al endpoint /usuario
    response = client.post("/usuario", json=payload)

    # Validaciones (Aserciones)
    assert response.status_code == 201 or response.status_code == 200
    
    data = response.json()
    assert data["correo_electronico"] == payload["correo_electronico"]
    assert data["nombre"] == "Test"
    
    # Verificación de seguridad: la contraseña no debe devolverse en el JSON
    assert "contrasena" not in data

def test_crear_usuario_datos_invalidos():
    # Prueba enviando un tipo de dato incorrecto (ej. rol_Id como string)
    payload_invalido = {"rol_Id": "no-es-un-numero", "nombre": "Error"}
    
    response = client.post("/usuario", json=payload_invalido)
    
    # FastAPI/Pydantic deben retornar 422 Unprocessable Entity automáticamente
    assert response.status_code == 422