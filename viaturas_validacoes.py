import re
from datetime import date
from viaturas_classes import *    

def val_mat(matricula: str):
    vmat1 = r"^\d\d-[A-Z]{2}-\d\d$"
    vmat2 = r"^[A-Z]{2}-\d\d-\d\d$"
    vmat3 = r"^\d\d-\d\d-[A-Z]{2}$"
    vmat4 = r"^[A-Z]{2}-\d\d-[A-Z]{2}$"
    vmat = re.search(f"{vmat1}|{vmat2}|{vmat3}|{vmat4}", matricula)
    if not vmat:
        return f"{matricula=} em formato inválido"

def val_mat_duplicada(carros: CatalogoCarros, matricula: str):
    if matricula in carros.valores_carros:
        return f"{matricula=} já se encontra registada no catalogo."
                             
def val_data(data: str):
    try:
        date.fromisoformat(data)
    except:
       return f"{data=} não é uma data válida"
 
def val_marca (marca: str):    
    if not marca:
        return 'O campo "marca" deve ser preechido.'
                
def val_modelo(modelo: str):
    if not modelo:
        return 'O campo "modelo" deve ser preechido.'
    
def val_data_de_mat(matricula: str, data: str):
    vmat1 = re.search(r"^[A-Z]{2}-\d\d-\d\d$", matricula)
    vmat2 = re.search(r"^\d\d-\d\d-[A-Z]{2}$", matricula)
    vmat3 = re.search(r"^\d\d-[A-Z]{2}-\d\d$", matricula)
    
    if vmat1 and date.fromisoformat(data) > date.fromisoformat('1992-06-31'):
        return f'Um veiculo com data {data} não pode ter uma matricula {matricula}'
    if vmat2 and date.fromisoformat(data) > date.fromisoformat('2005-06-31'):
        return f'Um veiculo com data {data} não pode ter uma matricula {matricula}'
    if vmat3 and date.fromisoformat(data) > date.fromisoformat('2020-03-01'):
        return f'Um veiculo com data {data} não pode ter uma matricula {matricula}'
