import sys
import subprocess
from op_ficheiros import *
from viaturas_validacoes import *

DEFAULT_INDENTATION = 5
            
def exibe_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent - 1), *args, **kargs)
    
def entrada(msg: str, indent = DEFAULT_INDENTATION):
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")
    
def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
        
def pause(msg: str="Pressione ENTER para continuar...", indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")

def menu(carros: CatalogoCarros):
    while True:
        cls()
        exibe_msg("***********************************")
        exibe_msg("* MENU:                           *")
        exibe_msg("* 1 - Listar Viaturas             *")             
        exibe_msg("* 2 - Pesquisar Viaturas          *")
        exibe_msg("* 3 - Adicionar Viatura           *")
        exibe_msg("* 4 - Remover Viatura             *")
        exibe_msg("* 5 - Gravar Catalogo             *")
        exibe_msg("* 6 - Recarregar Catalogo         *")
        exibe_msg("* T - Terminar                    *")
        exibe_msg("***********************************")
        print()
        esc = entrada("Opção: ").strip().upper()
        match esc:    
            case '1':
                lis_viaturas(carros.ordenar_carros())
            case '2':
                pes_viaturas(carros.ordenar_carros())
            case '3':
                add_car(carros)
            case '4':
                rem_car(carros)
            case '5':
                gravar_calalogo(carros)
            case '6':
                carros = recarrega_cat(carros)
            case 'T':
                exibe_msg("A sair do programa.")
                break
            case other:
                exibe_msg("Opção inválida, escolha novamente.")
                print()
                pause()  

def lis_viaturas(carros: CatalogoCarros):
    titulos = f"|{'Marca':^16}|{'Modelo':^20}|{'Data':^12}|{'Matricula':^14}|"
    divisor = f"|{'-' * 16}+{'-' * 20}+{'-' * 12}+{'-' * 14}|"
    exibe_msg("Lista de Viaturas:\n")
    exibe_msg(titulos)
    exibe_msg(divisor)
    
    for car in carros:
        linha = f"|{car.marca:^16}|{car.modelo:^20}|{car.data:^12}|{car.matricula:^14}|"
        exibe_msg(linha)
    print()
    pause()
    
def pes_viaturas(carros: CatalogoCarros):
    try:
        pesquisa = crit_pesquisa()
        if pesquisa:
            resultado = carros.pesquisa(pesquisa[0], pesquisa[1])
            if resultado:
                lis_viaturas(resultado)
            else:
                exibe_msg("Não foram encontrados veiculos.")
                print()
                pause()  
    except AtributoInvalido as ai:
        exibe_msg(f"Erro de inserção: {ai}")    
        print()
        pause()  
               
def crit_pesquisa():
    procura = None
    while True:
        print()
        exibe_msg("++++++++++++++++++++++++++++++++++++++++++++")
        exibe_msg("+ Qual o criterior que deseja procurar:    +")
        exibe_msg("+ 1 - Maricula                             +")
        exibe_msg("+ 2 - Marca                                +")
        exibe_msg("+ 3 - Modelo                               +")
        exibe_msg("+ 4 - Data:                                +")
        exibe_msg("+ V - Voltar ao menu anterior              +")
        exibe_msg("++++++++++++++++++++++++++++++++++++++++++++")
        print()
        esc = entrada("Opção: ").strip().upper() 
        match esc:
            case '1':
                procura = entrada("Insira a matricula: ")
                val_mat(procura)
                tipo = "matricula"
                return procura, tipo
            case '2':
                procura = entrada("Insira a marca: ")
                val_marca(procura)
                tipo = "marca"
                return procura, tipo
            case '3':
                procura = entrada("Insira o modelo: ")
                val_modelo(procura)
                tipo = "modelo"
                return procura, tipo
            case '4':
                procura = entrada("Insira a data: ")
                val_data(procura)
                tipo = "data"
                return procura, tipo
            case 'V':
                exibe_msg("Voltando ao menu anterior...")
                break
            case other:
                exibe_msg("Opção inválida, escolha novamente...")
    
def add_car(carros: CatalogoCarros):
    try:   
        matricula = entrada("Insira a matricula: ")
        val_mat(matricula)
        val_mat_duplicada(carros, matricula)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    except ValorDuplicado as vd:
        exibe_msg(vd)
        print()
        pause()
        return
    try:
        marca = entrada("Insira a marca: ")
        val_marca(marca)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        modelo = entrada("Insira o modelo: ")
        val_modelo(modelo)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        data = entrada("Insira a data: ")
        val_data(data)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    try:
        val_data_de_mat(matricula, data)
    except AtributoInvalido as ai:
        exibe_msg(ai)
        print()
        pause()
        return
    
    carros.append(Carro(matricula, marca, modelo, data))
    exibe_msg("Veiculo Adicionado.")
    print()
    pause()
    
def rem_car(carros: CatalogoCarros):
    remover = entrada("Insira a matricula do veiculo a remover: ")
    try:    
        val_mat(remover)
        if remover in carros.valores_carros:
            carros.valores_carros.pop(remover)
            exibe_msg(f"Veiculo com a matricula {remover} removido.")
            pause()
            print() 
        else:
            exibe_msg(f"Não foi encontrado veiculo com matricula {remover}")
            pause()
            print()                
    except AtributoInvalido as ai:
        exibe_msg(f"Erro de formato: {ai}")
        pause()
        print() 

def gravar_calalogo(carros: CatalogoCarros):
    gravar_carros(carros, FILEPATH)
    exibe_msg("Catalogo Gravado no Ficheiro.")
    print()
    pause()
    
def recarrega_cat(carros: CatalogoCarros):
    carros = ler_carros(FILEPATH)
    exibe_msg("Catalogo Atualizado.")
    print()
    pause()
    return carros

    