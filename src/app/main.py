from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()
received_names: list[str] = []


class HelloRequest(BaseModel):
    name: str = Field(min_length=1)


@app.post("/hello")
def hello(payload: HelloRequest) -> dict[str, str]:
    received_names.append(payload.name)
    return {"message": f"Hello {payload.name}"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
