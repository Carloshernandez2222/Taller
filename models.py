from sqlmodel import Field, SQLModel
from pydantic import field_validator


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    email: str
    edad: int

    @field_validator("nombre")
    @classmethod
    def nombre_no_solo_numeros(cls, v: str) -> str:
        s = v.strip()
        if not s:
            raise ValueError("El nombre no puede estar vacío")
        if s.isdigit():
            raise ValueError("El nombre no puede ser solo números")
        return s

    @field_validator("email")
    @classmethod
    def email_con_formato_basico(cls, v: str) -> str:
        s = v.strip().lower()
        if "@" not in s or not s.split("@")[0] or "." not in s.split("@")[-1]:
            raise ValueError("El correo electrónico no es válido")
        return s

    @field_validator("edad")
    @classmethod
    def edad_en_rango(cls, v: int) -> int:
        if v < 0:
            raise ValueError("La edad no puede ser negativa")
        if v > 130:
            raise ValueError("La edad no es válida")
        return v
