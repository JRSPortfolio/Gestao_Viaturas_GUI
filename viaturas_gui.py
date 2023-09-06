import tkinter as tk
from tkinter import font

def janela():
    janela = tk.Tk()
    janela.title("Catalogo de Automóveis")
    janela.geometry("600x800")
    
    janela.rowconfigure(0, weight = 0)
    janela.rowconfigure(1, weight = 0)
    janela.rowconfigure(2, weight = 0)
    janela.rowconfigure(3, weight = 0)
    janela.columnconfigure(0, weight = 1)
    janela.columnconfigure(1, weight = 1)
    
    button_font = font.Font(family="Cascadia Mono", size=12, weight="bold")
    title_font = ("Cascadia Mono", 16,"bold")
    
    title = tk.Label(janela, text = "Catálogo de Automóveis", font = title_font)

    listar_viaturas = tk.Button(janela, text="Listar Viaturas", width = 15, height = 3,
                                font = button_font, command=lambda: print("click"))
    pes_viaturas = tk.Button(janela, text="Pesquisar Viaturas", width = 15, height = 3,
                             font = button_font, command=lambda: print("click"))
    add_viatura = tk.Button(janela, text="Adicionar Viatura",  width = 15, height = 3,
                            font = button_font, command=lambda: print("click"))
    rem_viatura = tk.Button(janela, text="Remover Viatura",  width = 15, height = 3,
                            font = button_font, command=lambda: print("click"))
    gravar_catalogo = tk.Button(janela, text="Gravar Catalogo",  width = 15, height = 3,
                                font = button_font, command=lambda: print("click"))
    recarregar_catalogo = tk.Button(janela, text="Recarregar Catalogo",  width = 15, height = 3,
                                    font = button_font, command=lambda: print("click"))
    
    title.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 50, sticky = "ew")
    listar_viaturas.grid(row=1, column=0, padx = 40, pady = 10, sticky = "ew")
    pes_viaturas.grid(row=1, column=1, padx = 40, pady = 10, sticky = "ew")
    add_viatura.grid(row=2, column=0, padx = 40, pady = 10, sticky = "ew")
    rem_viatura.grid(row=2, column=1, padx = 40, pady = 10, sticky = "ew")
    gravar_catalogo.grid(row=3, column=0, padx = 40, pady = 10, sticky = "ew")
    recarregar_catalogo.grid(row=3, column=1, padx = 40, pady = 10, sticky = "ew")
    
    # listar_viaturas.place(x=50, y=50)
    # pes_viaturas.place(x=300, y=50)
    # add_viatura.place(x=50, y=200)
    # rem_viatura.place(x=300, y=200)
    # gravar_catalogo.place(x=50, y=350)
    # recarregar_catalogo.place(x=300, y=350)
    
    # janela.rowconfigure(0, weight=1)
    # janela.rowconfigure(1, weight=1)
    # janela.columnconfigure(0, weight=1)
    # janela.columnconfigure(1, weight=1)
    print(font.families())
    janela.mainloop()
    
janela()