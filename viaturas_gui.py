import tkinter as tk
from tkinter import font, ttk, Scrollbar
import winreg
from op_ficheiros import *

class janela_inicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.carros = ler_carros(FILEPATH)
        
        self.title("Catalogo de Automóveis")
        self.geometry("600x800+100+50")
        
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 0)
        self.rowconfigure(3, weight = 0)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        
        # fonts = font.families()
        title_font = ("Cascadia Mono", 16, "bold")
        button_font = ("Cascadia Mono", 12, "bold")
        result_titles_font = ("Cascadia Mono", 12, "bold")
        
        self.title_label = tk.Label(self, text = "Catálogo de Automóveis", font = title_font)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 30, sticky = "ew")
        
        self.buttons_layout(button_font)
        self.result_layout(result_titles_font)
        self.limpar_result_layout(result_titles_font)
        self.menu()
          
    def menu(self):
        self.menu_bar = tk.Menu(self)
        self.options = tk.Menu(self.menu_bar, tearoff = 0)
        # self.tipo_letra = tk.Menu(self.menu_bar, tearoff = 0)
        
        self.options.add_command(label = "Alterar Tipo de Letra", command = self.janela_tipo_letra)
        self.options.add_command(label = "Sair", command = self.quit)
        # for font in fonts:
        #     self.tipo_letra.add_command(label = font, command = lambda f = font: self.change_font(f))
            
        self.menu
        self.menu_bar.add_cascade(label = "Opções", menu = self.options)
        # self.menu_bar.add_cascade(label = "Alterar Tipo de Letra", menu = self.tipo_letra)
        
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
        self.listar_viaturas = tk.Button(self, text="Listar Viaturas", width = 12, height = 2 ,
                                         font = font, command = self.action_listar_viaturas)
        self.pes_viaturas = tk.Button(self, text="Pesquisar Viaturas", width = 12, height = 2,
                                      font = font, command=lambda: print("click"))
        self.add_viatura = tk.Button(self, text="Adicionar Viatura",  width = 12, height = 2,
                                     font = font, command=lambda: print("click"))
        self.rem_viatura = tk.Button(self, text="Remover Viatura",  width = 12, height = 2,
                                     font = font, command=lambda: print("click"))
        self.gravar_catalogo = tk.Button(self, text="Gravar Catalogo",  width = 12, height = 2,
                                         font = font, command=lambda: print("click"))
        self.recarregar_catalogo = tk.Button(self, text="Recarregar Catalogo",  width = 12, height = 2,
                                             font = font, command=lambda: print("click"))
        
        self.listar_viaturas.grid(row = 1, column = 0, padx = 40, pady = 10, sticky = "ew")
        self.pes_viaturas.grid(row = 1, column = 1, padx = 40, pady = 10, sticky = "ew")
        self.add_viatura.grid(row = 2, column = 0, padx = 40, pady = 10, sticky = "ew")
        self.rem_viatura.grid(row = 2, column = 1, padx = 40, pady = 10, sticky = "ew")
        self.gravar_catalogo.grid(row = 3, column = 0, padx = 40, pady = 10, sticky = "ew")
        self.recarregar_catalogo.grid(row = 3, column = 1, padx = 40, pady = 10, sticky = "ew")
        
    def result_layout(self, font):
        self.result_layout_canvas = tk.Canvas(self)
        self.result_layout_canvas.grid(row = 4, column = 0, columnspan = 2, padx = 0, pady = (80, 10), sticky = "ew")
        
        self.marca_titulo = tk.Label(self.result_layout_canvas, text = "Marca", font = font)
        self.modelo_titulo = tk.Label(self.result_layout_canvas, text = "Modelo", font = font)
        self.data_titulo = tk.Label(self.result_layout_canvas, text = "Data", font = font)
        self.matricula_titulo = tk.Label(self.result_layout_canvas, text = "Matricula", font = font)
        
        self.marca_titulo.grid(row = 0, column = 0, padx =  40, pady = 0, sticky = "ew")
        self.modelo_titulo.grid(row = 0, column = 1, padx = 40, pady = 0, sticky = "ew")
        self.data_titulo.grid(row = 0, column = 2, padx = 40, pady = 0, sticky = "ew")
        self.matricula_titulo.grid(row = 0, column = 3, padx = 40, pady = 0, sticky = "ew")
        
        for col in range(4):
            self.result_layout_canvas.grid_columnconfigure(col, weight=1)
        
    def limpar_result_layout(self, font):
        self.limpar_canvas = tk.Canvas(self)
        self.limpar_canvas.grid(row = 5, column = 0, columnspan = 2, padx = 200, pady = 10, sticky = "ew")
        
        self.limpar_res_lay = tk.Button(self.limpar_canvas, text="Limpar", width = 8, height = 1,
                                        font = font, command=lambda: print("clean"))
        self.limpar_res_lay.grid(row = 0, column = 0, padx =  40, pady = 0)
        self.limpar_canvas.grid_columnconfigure(0, weight=1)
          
    def action_listar_viaturas(self):
        x = 1      
        for car in self.carros:
            tk.Label(self.result_layout_canvas, text = f"{car.marca}").grid(row = x, column = 0, padx =  40, pady = 0, sticky = "ew")
            tk.Label(self.result_layout_canvas, text = f"{car.modelo}").grid(row = x, column = 1, padx =  40, pady = 0, sticky = "ew")
            tk.Label(self.result_layout_canvas, text = f"{car.data}").grid(row = x, column = 2, padx =  40, pady = 0, sticky = "ew")
            tk.Label(self.result_layout_canvas, text = f"{car.matricula}").grid(row = x, column = 3, padx =  40, pady = 0, sticky = "ew")
            x += 1
                  
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



janela = janela_inicial()
janela.mainloop()

