import tkinter as tk
from tkinter import font, ttk

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
        
        # fonts = font.families()
        title_font = ("Cascadia Mono", 16, "bold")
        button_font = ("Cascadia Mono", 12, "bold")
        
        self.title_label = tk.Label(self, text = "Catálogo de Automóveis", font = title_font)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 50, sticky = "ew")
        
        self.buttons(button_font)
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
        self.lista_fontes.geometry("700x500")
        self.canvas = tk.Canvas(self.lista_fontes)
        self.canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
        
        fonte_selecionada = tk.StringVar()
        fonts = font.families()
        
        x = 0
        y = 0
        
        for tipo in fonts:
            ttk.Radiobutton(self.lista_fontes, text = tipo, variable = fonte_selecionada, value = tipo).grid(row = x, column = y)
            y += 1
            if y > 2:
                y = 0
                x += 1
            
        def seleccao():
            escolha = fonte_selecionada.get()
            if escolha:
                self.change_font(self, escolha)
                
        ttk.Button(self.lista_fontes, text="Escolher", command = seleccao).pack()
        
        
        
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