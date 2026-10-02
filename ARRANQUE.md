# David s-0
Prueba de pipeline CI
## s-1 arranque

Creé la app mínima en main.py, los tests en test_api.py y las dependencias en requirements.txt. Los nombres se guardan en una lista en memoria. No añadí Docker, CI ni despliegue.

Verificación: pasaron los 12 tests de Proyecto/tests/, incluidos los existentes. El entorno disponible para ejecutarlos usa Python 3.14; los comandos de abajo crean el entorno solicitado con Python 3.11.

Desde la raíz del repositorio, prepara el entorno e instala las dependencias:
cd Proyecto
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

Ejecuta los tests:
python -m pytest -q tests/

Para iniciar la aplicación:
python -m uvicorn src.app.main:app --reload

La API estará disponible en http://127.0.0.1:8000; puedes comprobar /health en http://127.0.0.1:8000/health.
