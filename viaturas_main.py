from viaturas_helpdoc import *
                    
def main():
    carros_ini = Viaturas_Arranque()
    if not carros_ini.listar and not carros_ini.pesquisa and not carros_ini.adiciona and not carros_ini.remover:    
        carros = ler_carros(FILEPATH)
        menu(carros)
    else:
        carros_ini.arranque()
    
if __name__ == "__main__":
    main()
