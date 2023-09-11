import tkinter as tk
from tkinter import font

class janela_inicial(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Catalogo de Automóveis")
        self.geometry("600x800")
        
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 0)
        self.rowconfigure(3, weight = 0)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        
        fonts = font.families()
        title_font = ("Cascadia Mono", 16, "bold")
        button_font = ("Cascadia Mono", 12, "bold")
        
        self.title_label = tk.Label(self, text = "Catálogo de Automóveis", font = title_font)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 50, sticky = "ew")
        
        self.buttons(button_font)
        self.menu(fonts)
        
        
    def menu(self, fonts: tuple):
        self.menu_bar = tk.Menu(self)
        self.options = tk.Menu(self.menu_bar, tearoff = 0)
        self.tipo_letra = tk.Menu(self.menu_bar, tearoff = 0)
        
        self.options.add_command(label = "Sair", command = self.quit)
        
        for font in fonts:
            self.tipo_letra.add_command(label = font, command = lambda f = font: self.change_font(f))
        
        self.menu_bar.add_cascade(label = "Opções", menu = self.options)
        self.menu_bar.add_cascade(label = "Alterar Tipo de Letra", menu = self.tipo_letra)
        
        self.config(menu = self.menu_bar)
        
    def buttons(self, button_font): 
        self.listar_viaturas = tk.Button(self, text="Listar Viaturas", width = 15, height = 3,
                                    font = button_font, command=lambda: print("click"))
        self.pes_viaturas = tk.Button(self, text="Pesquisar Viaturas", width = 15, height = 3,
                                font = button_font, command=lambda: print("click"))
        self.add_viatura = tk.Button(self, text="Adicionar Viatura",  width = 15, height = 3,
                                font = button_font, command=lambda: print("click"))
        self.rem_viatura = tk.Button(self, text="Remover Viatura",  width = 15, height = 3,
                                font = button_font, command=lambda: print("click"))
        self.gravar_catalogo = tk.Button(self, text="Gravar Catalogo",  width = 15, height = 3,
                                    font = button_font, command=lambda: print("click"))
        self.recarregar_catalogo = tk.Button(self, text="Recarregar Catalogo",  width = 15, height = 3,
                                        font = button_font, command=lambda: print("click"))
        
        self.listar_viaturas.grid(row=1, column=0, padx = 40, pady = 10, sticky = "ew")
        self.pes_viaturas.grid(row=1, column=1, padx = 40, pady = 10, sticky = "ew")
        self.add_viatura.grid(row=2, column=0, padx = 40, pady = 10, sticky = "ew")
        self.rem_viatura.grid(row=2, column=1, padx = 40, pady = 10, sticky = "ew")
        self.gravar_catalogo.grid(row=3, column=0, padx = 40, pady = 10, sticky = "ew")
        self.recarregar_catalogo.grid(row=3, column=1, padx = 40, pady = 10, sticky = "ew")
        
    def change_font(self, font_type: str):
        self.title_label.config(font = (font_type, 16, "bold"))
        self.listar_viaturas.config(font = (font_type, 12, "bold"))
        self.pes_viaturas.config(font = (font_type, 12, "bold"))
        self.add_viatura.config(font = (font_type, 12, "bold"))
        self.rem_viatura.config(font = (font_type, 12, "bold"))
        self.gravar_catalogo.config(font = (font_type, 12, "bold"))
        self.recarregar_catalogo.config(font = (font_type, 12, "bold"))
    
janela = janela_inicial()
janela.mainloop()