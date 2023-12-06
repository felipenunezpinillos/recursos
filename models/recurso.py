from pydantic import BaseModel
from typing import Optional

class Recurso(BaseModel):

    id: int

    tipo: str

    estado: bool