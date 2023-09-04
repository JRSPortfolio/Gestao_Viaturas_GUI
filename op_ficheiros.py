from viaturas_classes import *
from typing import TextIO

FILEPATH = "viaturas.csv"

def ler_carros(caminho_fich: str, delim = CSV_DEFAULT_DELIM):
    carros = CatalogoCarros()
    
    with open(caminho_fich, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            carros.append(Carro.from_csv(linha, delim))
    return carros

def linhas_relevantes(fich: TextIO):
    for linha in fich:
        linha = linha.strip()
        if len(linha) == 0 or linha[0] == '#':
            continue
        yield linha

def gravar_carros(carros: CatalogoCarros, caminho_fich: str):
    with open(caminho_fich, "wt") as fich:   
        for car in carros:
            fich.write(f"{car.matricula},{car.marca},{car.modelo},{car.data}\n")
    
def remover_carro(carros: CatalogoCarros, caminho_fich: str, matricula: str):
    if matricula in carros.valores_carros:
        carros.valores_carros.pop(matricula)
    with open(caminho_fich, "wt") as fich:
        for car in carros:
            fich.write(f"{car.matricula},{car.marca},{car.modelo},{car.data}\n")
