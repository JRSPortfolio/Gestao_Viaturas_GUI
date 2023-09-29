import tkinter as tk
from tkinter import font, ttk, Scrollbar
import winreg
from op_ficheiros import *
from viaturas_validacoes import *

class janela_inicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.carros = ler_carros(FILEPATH)
        
        self.title("Catalogo de Automóveis")
        self.geometry("600x800+100+50")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        
        # fonts = font.families()
        title_font = ("Cascadia Mono", 16, "bold")
        button_font = ("Cascadia Mono", 12, "bold")
        self.result_titles_font = ("Cascadia Mono", 12, "bold")
        self.detail_labels = []
        
        self.title_label = tk.Label(self, text = "Catálogo de Automóveis", font = title_font)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 30, sticky = "ew")
        
        self.buttons_layout(button_font)
        self.result_layout(self.result_titles_font)
        self.limpar_result_layout(self.result_titles_font)
        self.menu()
          
    def menu(self):
        self.menu_bar = tk.Menu(self)
        self.options = tk.Menu(self.menu_bar, tearoff = 0)
        
        self.options.add_command(label = "Alterar Tipo de Letra", command = self.janela_tipo_letra)
        self.options.add_command(label = "Sair", command = self.quit)
            
        self.menu
        self.menu_bar.add_cascade(label = "Opções", menu = self.options)
        
        self.config(menu = self.menu_bar)
        
    def janela_tipo_letra(self):
        self.lista_fontes = tk.Toplevel(self)
        self.lista_fontes.title("Alterar Tipo de Letra")
        self.lista_fontes.geometry("300x500+750+50")
        
        self.lista_fontes_canvas = tk.Canvas(self.lista_fontes)
        self.lista_fontes_canvas.grid(row=0, column=0, sticky="nsew")
        
        self.fonts_frame = ttk.Frame(self.lista_fontes_canvas)
        self.lista_fontes_canvas.create_window((0, 0), window = self.fonts_frame, anchor=tk.NW)
        self.font_escolha_frame = ttk.Frame(self.lista_fontes)
        self.font_escolha_frame.grid(row=1, column=0, sticky="nsew")
        
        scrollbar = Scrollbar(self.lista_fontes, orient=tk.VERTICAL, command=self.lista_fontes_canvas.yview)
        scrollbar.grid(row=0, column=1, rowspan=2, sticky="ns")
        self.lista_fontes_canvas.configure(yscrollcommand=scrollbar.set)
        
        fonte_selecionada = tk.StringVar()
        self.get_font_list()
        
        def seleccao():
            escolha = fonte_selecionada.get()
            if escolha:
                self.change_font(escolha)
                self.lista_fontes.destroy()
                
        y = 0
        
        for i in self.font_list:
            ttk.Radiobutton(self.fonts_frame, text=i, variable = fonte_selecionada, value=i).grid(row=y, column=0, sticky="nsew")
            y += 1
                
        ttk.Button(self.lista_fontes, text="Escolher", command = seleccao).grid(row = 1, column = 0, pady=20)
        
        self.fonts_frame.update_idletasks()
        self.lista_fontes_canvas.config(scrollregion=self.lista_fontes_canvas.bbox("all"))
        
        self.lista_fontes.grid_rowconfigure(0, weight = 1)
        self.lista_fontes.grid_rowconfigure(1, weight = 0)
        self.lista_fontes.grid_columnconfigure(0, weight = 1)
        self.lista_fontes.grid_columnconfigure(1, weight = 0)
        
        def on_mousewheel(event):
            self.lista_fontes_canvas.yview_scroll(-1 * (event.delta // 120), "units")
        self.lista_fontes_canvas.bind_all("<MouseWheel>", on_mousewheel)
                    
    def buttons_layout(self, font): 
        self.listar_viaturas = tk.Button(self, text="Listar Viaturas", width = 30, height = 2 ,
                                         font = font, command = self.action_listar_viaturas)
        self.pes_viaturas = tk.Button(self, text="Pesquisar Viaturas", width = 30, height = 2,
                                      font = font, command = self.janela_pesquisa)
        self.add_viatura = tk.Button(self, text="Adicionar Viatura",  width = 30, height = 2,
                                     font = font, command=lambda: print("click"))
        self.rem_viatura = tk.Button(self, text="Remover Viatura",  width = 30, height = 2,
                                     font = font, command=lambda: print("click"))
        self.gravar_catalogo = tk.Button(self, text="Gravar Catalogo",  width = 30, height = 2,
                                         font = font, command=lambda: print("click"))
        self.recarregar_catalogo = tk.Button(self, text="Recarregar Catalogo",  width = 30, height = 2,
                                             font = font, command=lambda: print("click"))
        
        self.listar_viaturas.grid(row = 1, column = 0, padx = 40, pady = 10)
        self.pes_viaturas.grid(row = 1, column = 1, padx = 40, pady = 10)
        self.add_viatura.grid(row = 2, column = 0, padx = 40, pady = 10)
        self.rem_viatura.grid(row = 2, column = 1, padx = 40, pady = 10)
        self.gravar_catalogo.grid(row = 3, column = 0, padx = 40, pady = 10)
        self.recarregar_catalogo.grid(row = 3, column = 1, padx = 40, pady = 10)
        
    def result_layout(self, font):
        self.result_layout_canvas = tk.Canvas(self)
        self.result_layout_canvas.grid(row = 4, column = 0, columnspan = 2, padx = 0, pady = (80, 10))
        
        self.marca_titulo = tk.Label(self.result_layout_canvas, text = "Marca", font = font)
        self.modelo_titulo = tk.Label(self.result_layout_canvas, text = "Modelo", font = font)
        self.data_titulo = tk.Label(self.result_layout_canvas, text = "Data", font = font)
        self.matricula_titulo = tk.Label(self.result_layout_canvas, text = "Matricula", font = font)
        
        self.marca_titulo.grid(row = 0, column = 0, padx =  40, pady = 0)
        self.modelo_titulo.grid(row = 0, column = 1, padx = 40, pady = 0)
        self.data_titulo.grid(row = 0, column = 2, padx = 40, pady = 0)
        self.matricula_titulo.grid(row = 0, column = 3, padx = 40, pady = 0)
                                            
    def limpar_result_layout(self, font):
        self.limpar_canvas = tk.Canvas(self)
        self.limpar_canvas.grid(row = 5, column = 0, columnspan = 2, padx = 200, pady = 10)
                
        self.limpar_res_lay = tk.Button(self.limpar_canvas, text="Limpar", width = 8, height = 1,
                                        font = font, command = self.clean_list)
        self.limpar_res_lay.grid(row = 0, column = 0, padx =  40, pady = 0)
        self.limpar_canvas.grid_columnconfigure(0, weight=1)
        
    def clean_list(self):
        for group in self.detail_labels:
            for label in group:
                label.destroy()
        self.detail_labels.clear
        try:
            self.list_scrollbar.destroy()
            self.result_data_canvas.destroy()
        except:
            pass

    def action_listar_viaturas(self):
        self.clean_list()
        self.listar_resultados(self.carros)
          
    def listar_resultados(self, carros: CatalogoCarros):        
        self.result_data_canvas = tk.Canvas(self.result_layout_canvas)
        self.result_data_canvas.grid(row = 1, column = 0, columnspan = 4, sticky = 'ew')
        self.result_layout_frame = tk.Frame(self.result_data_canvas)
        # self.result_layout_frame = ScrolledText(self.result_data_canvas)
        self.result_data_canvas.create_window((0, 0), window=self.result_layout_frame, anchor='nw')
         
        self.detail_labels.clear
        x = 0
        for car in carros:
            label_marca = tk.Label(self.result_layout_frame, text = f"{car.marca}")
            label_modelo = tk.Label(self.result_layout_frame, text = f"{car.modelo}")
            label_data = tk.Label(self.result_layout_frame, text = f"{car.data}")
            label_matricula = tk.Label(self.result_layout_frame, text = f"{car.matricula}")
            
            label_marca.grid(row = x, column = 0, padx =  40, pady = 0)
            label_modelo.grid(row = x, column = 1, padx =  40, pady = 0)
            label_data.grid(row = x, column = 2, padx =  40, pady = 0)
            label_matricula.grid(row = x, column = 3, padx =  40, pady = 0)
            
            self.detail_labels.append((label_marca, label_modelo, label_data, label_matricula))
            x += 1
                        
        self.list_scrollbar = Scrollbar(self, orient = tk.VERTICAL, command = self.result_data_canvas.yview)
        self.list_scrollbar.grid(row = 4, column = 2, pady = (110, 0), sticky="ns")
        self.result_data_canvas.configure(yscrollcommand = self.list_scrollbar.set)
        self.result_data_canvas.update_idletasks()
        self.result_data_canvas.config(scrollregion=self.result_data_canvas.bbox("all"))
                                                    
        def on_mousewheel(event):
            self.result_data_canvas.yview_scroll(-1 * (event.delta // 120), "units") 
            
        self.result_data_canvas.bind_all("<MouseWheel>", on_mousewheel)
        
    def janela_pesquisa(self):
        self.pesquisa_menu = tk.Toplevel(self)
        self.pesquisa_menu.title("Pesquisar Veículo")
        self.pesquisa_menu.geometry("450x150+250+50")
        
        options = ['Matricula', 'Marca', 'Modelo', 'Data']
        font = ("Cascadia Mono", 12)
                
        self.cbox_pes_menu = ttk.Combobox(self.pesquisa_menu, values = options, font = font)
        self.cbox_pes_menu.set(options[0])
        self.cbox_pes_menu.grid(row = 0, column = 0, padx = 20, pady = 30)
        
        self.pes_menu_entry = tk.Entry(self.pesquisa_menu, font = font)
        self.pes_menu_entry.grid(row = 0, column = 1, padx = (0,20), pady = 30)
        
        self.pes_menu_button = tk.Button(self.pesquisa_menu, text="Pesquisar", width = 12, height = 1,
                                        font = font, command = self.pesquisa_veiculos)
        self.pes_menu_button.grid(row = 1, column = 0,columnspan = 2 , padx = 20, pady = 10)
        
        self.pesquisa_menu.grid_columnconfigure(0, weight = 1)
        self.pesquisa_menu.grid_columnconfigure(1, weight = 1)
        
    def pesquisa_veiculos(self):
        tipo = self.cbox_pes_menu.get().lower()
        procura = self.pes_menu_entry.get()
        resultado = self.carros.pesquisa(procura, tipo)
        self.clean_list()
        self.listar_resultados(resultado)
        self.pesquisa_menu.destroy()
                                                                              
    def change_font(self, font_type: str):
        self.title_label.config(font = (font_type, 16, "bold"))
        self.listar_viaturas.config(font = (font_type, 12, "bold"))
        self.pes_viaturas.config(font = (font_type, 12, "bold"))
        self.add_viatura.config(font = (font_type, 12, "bold"))
        self.rem_viatura.config(font = (font_type, 12, "bold"))
        self.gravar_catalogo.config(font = (font_type, 12, "bold"))
        self.recarregar_catalogo.config(font = (font_type, 12, "bold"))
        
    def get_font_list(self):
        key_path = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"
        self.font_list = []
        font_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
        for i in range(winreg.QueryInfoKey(font_key)[1]):
            font_name, n, _ = winreg.EnumValue(font_key, i)
            if font_name[:-11] in font.families():
                self.font_list.append(font_name[:-11])   
        winreg.CloseKey(font_key)
        
    def show__error_message(self, erro: str):
        self.error_window = tk.Toplevel(self)
        self.error_window.title("Error de Introdução de Dados")

        error_label = tk.Label(self.error_window, text = erro)
        error_label.pack(pady=10)

        close_button = tk.Button(self.error_window, text="Fechar", command = self.error_window.destroy)
        close_button.pack(pady=10)



janela = janela_inicial()
janela.mainloop()

