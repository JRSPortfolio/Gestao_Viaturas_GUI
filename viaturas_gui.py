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
        self.result_layout()
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
        listar_viaturas = tk.Button(self, text="Listar Viaturas", width = 30, height = 2 ,
                                         font = font, command = self.action_listar_viaturas)
        pes_viaturas = tk.Button(self, text="Pesquisar Viaturas", width = 30, height = 2,
                                      font = font, command = self.janela_pesquisa)
        add_viatura = tk.Button(self, text="Adicionar Viatura",  width = 30, height = 2,
                                     font = font, command = self.janela_add_veiculo)
        self.rem_viatura = tk.Button(self, text="Remover Viatura",  width = 30, height = 2,
                                     font = font, command = self.janela_rem_veiculo)
        gravar_catalogo = tk.Button(self, text="Gravar Catalogo",  width = 30, height = 2,
                                         font = font, command=lambda: print("click"))
        recarregar_catalogo = tk.Button(self, text="Recarregar Catalogo",  width = 30, height = 2,
                                             font = font, command=lambda: print("click"))
        
        listar_viaturas.grid(row = 1, column = 0, padx = 40, pady = 10)
        pes_viaturas.grid(row = 1, column = 1, padx = 40, pady = 10)
        add_viatura.grid(row = 2, column = 0, padx = 40, pady = 10)
        self.rem_viatura.grid(row = 2, column = 1, padx = 40, pady = 10)
        gravar_catalogo.grid(row = 3, column = 0, padx = 40, pady = 10)
        recarregar_catalogo.grid(row = 3, column = 1, padx = 40, pady = 10)
        
    def result_layout(self):
        self.result_layout_canvas = tk.Canvas(self)
        self.result_layout_canvas.grid(row = 4, column = 0, columnspan = 2, padx = 0, pady = (80, 10))
                                            
    def limpar_result_layout(self, font):
        self.limpar_canvas = tk.Canvas(self)
        self.limpar_canvas.grid(row = 5, column = 0, columnspan = 2, padx = 200, pady = 10)
                
        self.limpar_res_lay = tk.Button(self.limpar_canvas, text="Limpar", width = 8, height = 1,
                                        font = font, command = self.clean_list)
        self.limpar_res_lay.grid(row = 0, column = 0, padx = 40, pady = 0)
        self.limpar_canvas.grid_columnconfigure(0, weight=1)
        
    def clean_list(self):
        for group in self.detail_labels:
            for label in group:
                label.destroy()
        self.detail_labels.clear
        try:
            # self.list_scrollbar.destroy()
            self.treeview_lista.destroy()
            self.result_layout_canvas.destroy()
            self.result_layout()
        except:
            pass

    def action_listar_viaturas(self):
        self.clean_list()
        self.listar_resultados(self.carros)
        
    def limpar_sel(self, event):
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        try:
            if widget != self.treeview_lista and widget != self.rem_viatura:
                self.treeview_lista.selection_remove(self.treeview_lista.selection())
        except:
            pass
                  
    def listar_resultados(self, carros: CatalogoCarros):
        cols = ("marca", "modelo", "data", "matricula")
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("Cascadia Mono", 12, "bold"))
        style.configure("Treeview", font=("Cascadia Mono", 10))
        
        self.treeview_lista = ttk.Treeview(self.result_layout_canvas, columns = cols, show = 'headings', style = "Treeview")
        self.treeview_lista.grid(row = 0, column = 0, sticky = 'ew')
        
        for col in cols:
            self.treeview_lista.column(col, width = 130, anchor = tk.CENTER)
        
        self.treeview_lista.heading("marca", text = "Marca", anchor = tk.CENTER)
        self.treeview_lista.heading("modelo", text = "Modelo", anchor = tk.CENTER)
        self.treeview_lista.heading("data", text = "Data", anchor = tk.CENTER)
        self.treeview_lista.heading("matricula", text = "Matricula", anchor = tk.CENTER)
        
        i = 1
        for car in carros:
            self.treeview_lista.insert('', tk.END, values = (car.marca, car.modelo, car.data, car.matricula))
            i += 1
        
        if i > 12:
            self.treeview_lista.config(height = 12)
            scrollbar = ttk.Scrollbar(self.result_layout_canvas, orient=tk.VERTICAL, command = self.treeview_lista.yview)
            self.treeview_lista.configure(yscroll=scrollbar.set)
            scrollbar.grid(row = 0, column = 1, sticky = 'ns')
        else:
            self.treeview_lista.config(height = i)

        self.bind("<Button-1>", self.limpar_sel)
        
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
        try:
            procura, tipo = self.val_pes_options()
            resultado = self.carros.pesquisa(procura, tipo)
            if resultado:
                self.clean_list()
                self.listar_resultados(resultado)
                self.pesquisa_menu.destroy()
            else:
                self.show_error_message('Não foram encontrados veiculos')
                self.pes_menu_entry.delete(0, tk.END)
        except:
            pass

    def val_pes_options(self):
        tipo = self.cbox_pes_menu.get().lower()
        procura = self.pes_menu_entry.get()
        match tipo:
            case 'matricula':
                erro = val_mat(procura)
            case 'marca':
                erro = val_marca(procura)
            case 'modelo':
                erro = val_modelo(procura)
            case 'data':
                erro = val_data(procura)
        if erro:
            self.show_error_message(erro)
            self.pes_menu_entry.delete(0, tk.END)
        else:
            return procura, tipo
        
    def janela_add_veiculo(self):
        self.jan_add_veiculo = tk.Toplevel(self)
        self.jan_add_veiculo.title("Adicionar Veículo")
        self.jan_add_veiculo.geometry("470x350+250+50")
        
        font = ("Cascadia Mono", 12, "bold")
        
        self.marca_add_label = tk.Label(self.jan_add_veiculo, text = 'Marca', font = font)
        self.modelo_add_label = tk.Label(self.jan_add_veiculo, text = 'Modelo', font = font)
        self.matricula_add_label = tk.Label(self.jan_add_veiculo, text = 'Matricula', font = font)
        self.data_add_label = tk.Label(self.jan_add_veiculo, text = 'Data', font = font)
    
        self.marca_add_entry = tk.Entry(self.jan_add_veiculo, font = font)
        self.modelo_add_entry = tk.Entry(self.jan_add_veiculo, font = font)
        self.matricula_add_entry = tk.Entry(self.jan_add_veiculo, font = font)
        self.data_add_entry = tk.Entry(self.jan_add_veiculo, font = font)
        
        self.marca_add_label.grid(row = 0, column = 0, padx =  20, pady = (30, 5))
        self.modelo_add_label.grid(row = 1, column = 0, padx = 20, pady = 5)
        self.matricula_add_label.grid(row = 2, column = 0, padx = 20, pady = 5)
        self.data_add_label.grid(row = 3, column = 0, padx = 20, pady = 5)
        
        self.marca_add_entry.grid(row = 0, column = 1, padx =  10, pady = (30, 5))
        self.modelo_add_entry.grid(row = 1, column = 1, padx =  10, pady = 5)
        self.matricula_add_entry.grid(row = 2, column = 1, padx =  10, pady = 5)
        self.data_add_entry.grid(row = 3, column = 1, padx =  10, pady = 5)
        
        def fechar_button():
            self.jan_add_veiculo.destroy()
            
        close_button = tk.Button(self.jan_add_veiculo, text="Adicionar", font = font, height = 10, command = self.adicionar_veiculo)
        close_button.grid(row = 0, column = 2, rowspan = 4, padx = 10, pady = (40,0))

        close_button = tk.Button(self.jan_add_veiculo, text="Fechar", font = font, width = 15, command = fechar_button)
        close_button.grid(row = 4, column = 0, columnspan = 3, pady=10)
        
        for i in range(4):
            self.jan_add_veiculo.grid_columnconfigure(i, weight = 1)
            
    def val_add_veiculo(self):
        matricula = self.matricula_add_entry.get().strip()
        marca = self.marca_add_entry.get().strip()
        modelo = self.modelo_add_entry.get().strip()
        data = self.data_add_entry.get().strip()
        
        erro_mat = val_mat(matricula)
        erro_marca = val_marca(marca)
        erro_modelo = val_modelo(modelo)
        erro_data = val_data(data)
        
        erros = []
        
        if erro_mat:
            erros.append(erro_mat)
            self.matricula_add_entry.delete(0, tk.END)
        if erro_marca:
            erros.append(erro_marca)
            self.marca_add_entry.delete(0, tk.END)
        if erro_modelo:
            erros.append(erro_modelo)
            self.modelo_add_entry.delete(0, tk.END)
        if erro_data:
            erros.append(erro_data)
            self.data_add_entry.delete(0, tk.END)
            
        if not erro_mat:
            erro_mat_dup = val_mat_duplicada(self.carros, matricula)
            if erro_mat_dup:
                erros.append(erro_mat_dup)
                self.matricula_add_entry.delete(0, tk.END)
        
        if not erro_data:
            erro_data_mat = val_data_de_mat(matricula, data)
            if erro_data_mat:
                erros.append(erro_data_mat)
                self.matricula_add_entry.delete(0, tk.END)
                self.data_add_entry.delete(0, tk.END)
                
        return erros
        
    def adicionar_veiculo(self):
        erros = self.val_add_veiculo()
        if erros:
            self.show_error_message(erros)
        else:
            matricula = self.matricula_add_entry.get().strip()
            marca = self.marca_add_entry.get().strip()
            modelo = self.modelo_add_entry.get().strip()
            data = self.data_add_entry.get().strip()
            car = Carro(matricula, marca, modelo, data)
            self.carros.append(car)
            self.veiculo_adicionado_message(matricula, marca, modelo, data)
            self.jan_add_veiculo.destroy()
            self.listar_resultados(self.carros)
            
    def janela_rem_veiculo(self):
        self.jan_rem_veiculo = tk.Toplevel(self)
        self.jan_rem_veiculo.title("Remover Veículo")
        self.jan_rem_veiculo.geometry("470x400+250+50")
        
        font = ("Cascadia Mono", 12, "bold")
        
        self.matricula_rem_label = tk.Label(self.jan_rem_veiculo, text = 'Matricula', font = font)
        self.matricula_rem_entry = tk.Entry(self.jan_rem_veiculo, font = font)
        
        self.matricula_rem_label.grid(row = 0, column = 0, padx = 20, pady = 5)
        self.matricula_rem_entry.grid(row = 0, column = 1, padx =  10, pady = 5)
        
        try:
            sel_values = self.treeview_lista.item(self.treeview_lista.selection(), "values")
            matricula = sel_values[3]
            self.matricula_rem_entry.insert(0, matricula)
            self.rem_veiculo_proc(matricula = matricula)
        except:
            pass
        
        def fechar_button():
            self.jan_rem_veiculo.destroy()
            
        proc_rem_button = tk.Button(self.jan_rem_veiculo, text="Procurar Veiculo", width = 15 ,font = font, command = self.rem_veiculo_proc)
        proc_rem_button.grid(row = 1, column = 0, columnspan = 2, padx = 10)

        close_button = tk.Button(self.jan_rem_veiculo, text="Fechar", font = font, width = 15, command = fechar_button)
        close_button.grid(row = 2, column = 0, columnspan = 2, pady=10)
        
        self.jan_rem_veiculo.grid_columnconfigure(0, weight = 1)
        self.jan_rem_veiculo.grid_columnconfigure(1, weight = 1)
        
    def rem_veiculo_proc(self, **kwargs):
        matricula = self.matricula_rem_entry.get().strip()
        erro = val_mat(matricula)
        font = ("Cascadia Mono", 12, "bold")
        self.rem_msg_label = tk.Label(self.jan_rem_veiculo, text = '', font = font, width = 200)
        self.rem_msg_label.grid(row = 3, column = 0,columnspan = 2, padx = 20, pady = 5)
        
        def rem_button():
            self.rem_msg_label.config(text = "Veiculo Removido", width = 150)
            self.carros.valores_carros.pop(matricula)
            remover_button.destroy()
            self.matricula_rem_entry.delete(0, tk.END)
            self.listar_resultados(self.carros)
            
        if erro:
            self.show_error_message(erro)
            
        elif matricula not in self.carros.valores_carros:
            self.rem_msg_label.config(text = f"Não foi encontrada matricula {matricula}", width = 200)

        else:
            carro = self.carros.valores_carros.get(matricula)
            message = f"Veiculo a remover:\nMatricula: {carro.matricula}\nMarca: {carro.marca}\nModelo: {carro.modelo}\nData: {carro.data}"
            self.rem_msg_label.config(text = message, width = 150)
            remover_button = tk.Button(self.jan_rem_veiculo, text="Remover", font = font, width = 15, command = rem_button)
            remover_button.grid(row = 4, column = 0, columnspan = 2, pady=10)
                                                                                    
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
        
    def show_error_message(self, erro: str | list):    
            self.error_window = tk.Toplevel(self)
            self.error_window.title("Error de Introdução de Dados")

            if isinstance(erro, str):
                error_label = tk.Label(self.error_window, text = erro, font = ("Cascadia Mono", 12, "bold"))
                error_label.pack(padx = 20, pady = 10)
            
            else:
                for i in erro:
                    error_label = tk.Label(self.error_window, text = i, font = ("Cascadia Mono", 12, "bold"))
                    error_label.pack(padx = 20, pady = 10)
                    
            def fechar_button():
                self.error_window.destroy()

            close_button = tk.Button(self.error_window, text="Fechar", font = ("Cascadia Mono", 12, "bold"),command = fechar_button)
            close_button.pack(pady=10)
            
    def veiculo_adicionado_message(self, matricula, marca, modelo, data):    
            self.veiculo_add = tk.Toplevel(self)
            self.veiculo_add.title("Inserção Correcta")

            message = f"Veiculo adicionado com os seguintes dados: \nmarca: {marca}\nmodelo: {modelo}\nmatricula: {matricula}\ndata: {data}"        
            
            msg_label = tk.Label(self.veiculo_add, text = message, font = ("Cascadia Mono", 12, "bold"))
            msg_label.pack(padx = 20, pady = 10)
                    
            def ok_button():
                self.veiculo_add.destroy()

            close_button = tk.Button(self.veiculo_add, text="OK", font = ("Cascadia Mono", 14, "bold"), width = 12, command = ok_button)
            close_button.pack(pady=10)

janela = janela_inicial()
janela.mainloop()

