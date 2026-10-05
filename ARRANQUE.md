# David s-0
Prueba de pipeline CI
## s-1 arranque

La aplicación está en `src/app/main.py`, los tests en `tests/` y las dependencias en `requirements.txt`, todo desde la raíz del repositorio. Los nombres recibidos se guardan en memoria.

Esta aplicación no requiere credenciales ni variables de entorno. `POST /hello`
es público: en Postman usa **Authorization → No Auth** y envía el nombre como
JSON, por ejemplo `{"name": "Ana"}`. Un nombre vacío o compuesto solo por
espacios, o un campo `name` omitido, devuelve `422`. Si recibes `401`, revisa
que la petición apunte a esta app (`http://127.0.0.1:8000/hello`) y que no haya
una autenticación heredada en Postman o un proxy/middleware delante de Uvicorn;
esta ruta no comprueba credenciales.

Desde la raíz del repositorio, prepara el entorno e instala las dependencias:
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt

Ejecuta los tests:
python -m pytest -q tests/

Para iniciar la aplicación:
python -m uvicorn src.app.main:app --reload

La API estará disponible en http://127.0.0.1:8000; puedes comprobar /health en http://127.0.0.1:8000/health.

Para construir la imagen con BuildKit y ejecutarla:
docker buildx build --load -t laboratorio-aoe-agenticdev .
docker images para ver las imágenes creadas.
docker run --rm -p 8000:8000 laboratorio-aoe-agenticdev
