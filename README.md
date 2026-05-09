# Gestión de Usuarios (Universidad Católica de Colombia)

API en **FastAPI** con **SQLModel** (SQLite) y página de ejemplo con **Bootstrap** y **Tailwind**.

## Requisitos

- Python 3.10+

## Instalación y ejecución local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Documentación interactiva: `http://127.0.0.1:8000/docs`
- Página HTML: `http://127.0.0.1:8000/`

## GitHub y Codespace

1. Crea un repositorio vacío en GitHub.
2. En esta carpeta del proyecto:

```bash
git init
git add .
git commit -m "Proyecto inicial: FastAPI, SQLModel y frontend"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

3. En GitHub: **Code → Codespaces → Create codespace on main**.
4. En el Codespace, tras abrir la terminal:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Cuando VS Code/Codespaces pregunte por el puerto **8000**, ábrelo en el navegador.

## Nota sobre rutas

En el material aparece `GET /usuarios/{nombre}` y también `GET /usuarios/{id}` con `id` entero. En FastAPI ambas rutas chocan. Aquí el saludo por nombre está en **`GET /usuarios/saludo/{nombre}`**; el acceso por clave primaria sigue siendo **`GET /usuarios/{user_id}`**.
