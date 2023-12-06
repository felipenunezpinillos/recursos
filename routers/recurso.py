from fastapi import APIRouter
from fastapi import FastAPI

from models.recurso import Recurso

recursos = []

router = APIRouter()

@router.get('/recursos')

def get_recursos():

    return recursos

@router.get('/recursos/{id}')

def get_recurso(id: int):

    return list(filter(lambda item: item['id'] == id, recursos))

@router.get('/recursos/')
def get_recursos_by_tipo(tipo:str):
    if tipo == "Cama":
        return list(filter(lambda item: item['tipo'] == "cama", recursos))
    elif tipo == "Ubicacion":
        return list(filter(lambda item: item['tipo'] == "ubicacion", recursos))
    elif tipo == "Dispositivo":
        return list(filter(lambda item: item['tipo'] == "dispositivo", recursos))
    else:
        return "Tipo invalido, vuelva a intentarlo"
    
@router.post('/recursos')

def create_recurso(recurso : Recurso):
    
    recursos.append(recurso)
    return recursos

@router.delete('/recursos/{id}')
def delete_recurso(id: int):

    for item in recursos:
        if item["id"] == id:
            recursos.remove(item)

    return recursos