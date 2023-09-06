import tkinter as tk

def janela():
    janela = tk.Tk()
    janela.title("Catalogo de Automóveis")

    listar_viaturas = tk.Button(janela, text="Listar Viaturas", command=lambda: print("click"))
    pes_viaturas = tk.Button(janela, text="Pesquisar Viaturas", command=lambda: print("click"))
    add_viatura = tk.Button(janela, text="Adicionar Viatura", command=lambda: print("click"))
    rem_viatura = tk.Button(janela, text="Remover Viatura", command=lambda: print("click"))
    gravar_catalogo = tk.Button(janela, text="Gravar Catalogo", command=lambda: print("click"))
    recarregar_catalogo = tk.Button(janela, text="Recarregar Catalogo", command=lambda: print("click"))

    # listar_viaturas.pack()
    # pes_viaturas.pack()
    # add_viatura.pack()
    # rem_viatura.pack()
    # gravar_catalogo.pack()
    # recarregar_catalogo.pack()
    
    listar_viaturas.grid()
    pes_viaturas.grid()
    add_viatura.grid()
    rem_viatura.grid()
    gravar_catalogo.grid()
    recarregar_catalogo.grid()
    
    # listar_viaturas.place()
    # pes_viaturas.place()
    # add_viatura.place()
    # rem_viatura.place()
    # gravar_catalogo.place()
    # recarregar_catalogo.place()

    janela.mainloop()
    
janela()