from fastapi import Fastapi
app = Fastapi()

@app.get("/")
async def read_root() -> dict[str, str]:
    """Devuelve un mensaje de bienvenida simple."""
    
    return {"mensaje":"Hola FastAPI 8A IDGS"}
    