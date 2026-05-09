from collections.abc import Generator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, SQLModel, create_engine, select

from models import Usuario

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = "sqlite:///./usuarios.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(_: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Gestión de Usuarios", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/usuarios", response_model=list[Usuario])
def listar_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(Usuario)).all()


@app.get("/usuarios/saludo/{nombre}")
def obtener_usuario_por_nombre(nombre: str):
    """Equivalente al ejemplo con path `/usuarios/{nombre}` del material (ruta separada para no chocar con el id numérico)."""
    return {"mensaje": f"Hola {nombre}"}


@app.get("/usuarios/{user_id}", response_model=Usuario)
def obtener(user_id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    return usuario


@app.post("/usuarios", response_model=Usuario)
def crear(usuario: Usuario, session: Session = Depends(get_session)):
    existe = session.exec(select(Usuario).where(Usuario.email == usuario.email)).first()
    if existe:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un usuario registrado con ese correo electrónico",
        )
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@app.post("/crear")
def crear_usuario_legacy():
    return {"mensaje": "Usuario creado"}


app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
