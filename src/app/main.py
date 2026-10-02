from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

"""
FastAPI define la API y dirige las peticiones HTTP a /hello o /health, devolviendo sus respuestas.
Pydantic valida el JSON de /hello con HelloRequest antes de que llegue a hello().
"""

app = FastAPI()
received_names: list[str] = []


class HelloRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1)

"""
POST /hello espera el campo `name` en el cuerpo JSON de la petición. Debe ser
una cadena con al menos un carácter no blanco, por ejemplo:
{"name": "Ana"}. El endpoint añade el nombre a `received_names` y responde
{"message": "Hello Ana"}. No requiere autenticación.

En Postman, selecciona POST y la URL terminada en /hello. En Body elige
raw y JSON, selecciona No Auth y envía {"name": "Ana"}.
"""
@app.post("/hello")
def hello(payload: HelloRequest) -> dict[str, str]:
    received_names.append(payload.name)
    return {"message": f"Hello {payload.name}"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
