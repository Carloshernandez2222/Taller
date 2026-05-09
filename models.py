from sqlmodel import SQLModel, Field


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    email: str
    edad: int
