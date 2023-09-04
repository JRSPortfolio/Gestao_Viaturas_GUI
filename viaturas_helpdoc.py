from viaturas_instrucoes import *
from docopt import docopt

class Viaturas_Arranque:
    def __init__(self):
        h_doc = '''
    Programa de armazenamento de dados de viaturas em ficheiro CSV
    Correr o programa irá exibir o seguinte menu:
        ***********************************
        * MENU:                           *
        * 1 - Listar Viaturas             *             
        * 2 - Pesquisar Viaturas          *
        * 3 - Adicionar Viatura           *
        * 4 - Remover Viatura             *
        * 5 - Gravar Catalogo             *
        * 6 - Recarregar Catalogo         *
        * T - Terminar                    *
        ***********************************
    Os veiculos irão ser armazenados em memória e poderá efetuar operações e gravar as actualizações no ficheiro quando achar conveniente.
    Se pretender desfazer as alterações poderá recarregar o ficheiro.
    Poderá fazer alterações diretamente no ficheiro utilizando as opções abaixo indicadas.    

    Usage:
        viaturas_main.py [-l] [-p | -p -v VALOR TIPO] [-a | -a -d MATRICULA MARCA MODELO DATA] [-r | -r -m MAT]
        
    Options:
        -l, --listar                                                            Listar as viaturas guardadas em ficheiro
        -p, --pesquisa                                                          Pesquisar viaturas gurdadas em ficheiro
        -v VALOR, --valorpes VALOR TIPO                                         Pesquisa uma matricula, marca, modelo ou data nos veiculos guardados, recebe o valor
                                                                                a pesquisar seguido do tipo (MATRICULA, MARCA, MODELO, DATA), usado com o comando -p
        -a, --adiciona                                                          Adiciona uma viaturas ao ficheiro
        -d MATRICULA MARCA MODELO DATA, --dados MATRICULA MARCA MODELO DATA     Recebe dados de uma viatura para ser inserido em ficheiro, usado com o comando -a 
        -r, --remover                                                           Remove uma viatura do ficheiro
        -m MAT, --rem-mat MAT                                                   Receve uma matricula para a viatura correspondente em ficheiro ser removida, usada com o comando -r
'''
        self.args = docopt(h_doc)
        self.listar = self.args['--listar']
        self.pesquisa = self.args['--pesquisa']
        self.valorpes = self.args['--valorpes']
        self.adiciona = self.args['--adiciona']
        self.add_dados = self.args['--dados']
        self.remover = self.args['--remover']
        self.rem_mat = self.args['--rem-mat']

    def __iter__(self):
        arg_list = [self.listar,
                    self.pesquisa,
                    self.valorpes,
                    self.adiciona,
                    self.add_dados,
                    self.remover,
                    self.rem_mat]
        for i in arg_list:
            yield i
    
    def arranque(self):
        carros = ler_carros(FILEPATH)
        
        if self.listar:
            lis_viaturas(carros.ordenar_carros())
        elif self.pesquisa:
            if not self.valorpes:
                pes_viaturas(carros.ordenar_carros())
            else:
                self.pesquisa_valor(carros.ordenar_carros())
        elif self.adiciona:
            if not self.add_dados:
                add_car(carros)
                gravar_carros(carros, FILEPATH)
            else:
                self.adiciona_valores(carros)
        elif self.remover:
            if not self.rem_mat:
                rem_car(carros)
                gravar_carros(carros, FILEPATH)
            else:
                self.remover_valor(carros)

    def pesquisa_valor(self, carros: CatalogoCarros):
        valor = self.args['--valorpes']
        tipo = self.args['TIPO'].lower()
        if tipo not in ['matricula', 'marca', 'modelo', 'data']:
            exibe_msg(f"{tipo} não é um tipo válido")
        else:
            pesquisa = carros.pesquisa(valor, tipo)
            if pesquisa:
                lis_viaturas(pesquisa)
            else:
                exibe_msg("Não foram encontrados veiculos.")
                print()
                pause()
            
    def adiciona_valores(self, carros: CatalogoCarros):
        matricula = self.args['--dados']
        marca = self.args['MARCA']
        modelo = self.args['MODELO']
        data = self.args['DATA']
        try:
            val_mat(matricula)
            val_mat_duplicada(carros, matricula)
            val_marca(marca)
            val_modelo(modelo)
            val_data(data)
            val_data_de_mat(matricula, data)
            carros.append(Carro(matricula, marca, modelo, data))
            gravar_calalogo(carros)
        except AtributoInvalido as ai:
            exibe_msg(ai)
            print()
            pause()
        except ValorDuplicado as vd:
            exibe_msg(vd)
            print()
            pause()          
        
    def remover_valor(self, carros: CatalogoCarros):
        matricula = self.args['--rem-mat']
        try:
            val_mat(matricula)
        except AtributoInvalido as ai:
            exibe_msg(ai)
            print()
            pause()
        if matricula in carros.valores_carros:
            remover_carro(carros, FILEPATH, matricula)
            exibe_msg(f"Veiculo com matricula {matricula} removido do ficheiro")
            print()
            pause()
        else:
            exibe_msg(f"Não existe veiculo com matricula {matricula} no ficheiro")
            print()
            pause()

        
                 
        
              

            
            
            
        