import tkinter as tk
from tkinter import font, ttk, Scrollbar
import winreg
from op_ficheiros import *
from viaturas_validacoes import *

class janela_inicial(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.carros = ler_carros(FILEPATH)
        self.adds_mod = CatalogoCarros()
        self.rems_mod = CatalogoCarros()
        
        self.treeview_font_h = ("Cascadia Mono", 12, "bold")
        self.treeview_font_l = ("Cascadia Mono", 10)
        self.subs_font = ("Cascadia Mono", 12, "bold")
        self.comon_font = ("Cascadia Mono", 12, "bold")
        
        self.title("Catalogo de Automóveis")
        self.geometry("600x800+100+50")
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(4, weight = 1)
        
        self.subs_font = ("Cascadia Mono", 12, "bold")
        self.comon_font = ("Cascadia Mono", 12, "bold")
        
        self.set_title()
        self.buttons_layout()
        self.result_layout()
        self.limpar_result_layout()
        self.menu()
        
    def set_title(self):
        font = ("Cascadia Mono", 16, "bold")
        self.title_label = tk.Label(self, text = "Catálogo de Automóveis", font = font)
        self.title_label.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 30, sticky = "ew")
       
    def menu(self):
        menu_bar = tk.Menu(self)
        options = tk.Menu(menu_bar, tearoff = 0)
        
        options.add_command(label = "Alterar Tipo de Letra", command = self.janela_tipo_letra)
        options.add_command(label = "Sair", command = self.quit)
            
        # menu
        menu_bar.add_cascade(label = "Opções", menu = options)
        
        self.config(menu = menu_bar)
        
    def janela_tipo_letra(self):
        def get_font_list():
            key_path = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"
            font_list = []
            font_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
            for i in range(winreg.QueryInfoKey(font_key)[1]):
                font_name, n, _ = winreg.EnumValue(font_key, i)
                if font_name[:-11] in font.families():
                    font_list.append(font_name[:-11])   
            winreg.CloseKey(font_key)
            return font_list
        
        def change_font(font_type: str):            
            for key in fonts_selection.keys():
                if fonts_selection[key] == True:
                    print (fonts_selection[key])
                    if key == "titulo":
                        self.title_label.config(font = (font_type, 16, "bold"))
                    elif key == "opcoes":
                        for widget in (self.listar_viaturas, self.pes_viaturas, self.add_viatura, self.rem_viatura, self.gravar_catalogo,
                                       self.recarregar_catalogo, self.limpar_res_lay):
                            widget.config(font = (font_type, 12, "bold"))
                    elif key == "listing":
                        try:
                            self.treeview_font_h = (font_type, 12, "bold")
                            self.treeview_font_l = (font_type, 10)   
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font = (font_type, 12, "bold"))
                            style.configure("Treeview", font = (font_type, 10))
                            self.treeview_lista.config(style = "Treeview")
                        except AttributeError:
                            self.treeview_font_h = (font_type, 12, "bold")
                            self.treeview_font_l = (font_type, 10)                      
                        except tk.TclError:
                            self.treeview_font_h = (font_type, 12, "bold")
                            self.treeview_font_l = (font_type, 10)
                    elif key == "subs":
                        try:
                            self.subs_font = (font_type, 12, "bold")
                            for widget in (self.marca_add_label, self.modelo_add_label, self.matricula_add_label, self.data_add_label,
                                           self.marca_add_entry, self.modelo_add_entry, self.matricula_add_entry, self.data_add_entry,
                                           self.add_add_button, self.add_close_button):
                                widget.config(font = (font_type, 12, "bold"))
                        except tk.TclError:
                            self.subs_font = (font_type, 12, "bold")
                        except AttributeError:
                            self.subs_font = (font_type, 12, "bold")
                            
                        try:
                            self.subs_font = (font_type, 12, "bold")
                            for widget in (self.matricula_rem_label, self.matricula_rem_entry, self.proc_rem_button, self.rem_close_button):
                                widget.config(font = (font_type, 12, "bold"))
                        except tk.TclError:
                            self.subs_font = (font_type, 12, "bold")
                        except AttributeError:
                            self.subs_font = (font_type, 12, "bold")
                            
                        try:
                            self.subs_font = (font_type, 12, "bold")
                            for widget in (self.gravar_cat_label,  self.gravar_ok_button, self.gravar_no_button):
                                widget.config(font = (font_type, 12, "bold"))
                        except tk.TclError:
                            self.subs_font = (font_type, 12, "bold")
                        except AttributeError:
                            self.subs_font = (font_type, 12, "bold")
                            
                        try:
                            self.subs_font = (font_type, 12, "bold")
                            for widget in ( self.rec_cat_label, self.rec_ok_button, self.rec_no_button):
                                widget.config(font = (font_type, 12, "bold"))
                        except tk.TclError:
                            self.subs_font = (font_type, 12, "bold")
                        except AttributeError:
                            self.subs_font = (font_type, 12, "bold")

        def on_mousewheel(event):
            widget = event.widget.winfo_containing(event.x_root, event.y_root)
            try:
                if widget == fonts_listbox:
                    fonts_listbox.yview_scroll(-1 * (event.delta // 120), "units")
            except:
                pass
            
        def seleccao():
            sel_indices = fonts_listbox.curselection()
            if sel_indices:
                index = sel_indices[0]
                escolha = fonts_listbox.get(index)
                change_font(escolha)
                
        def sections_selection():
            reset_fonts_selection()            
            if check_titulo.get():
                fonts_selection["titulo"] = True
            else:
                fonts_selection["titulo"] = False
                              
            if check_opcoes.get():
                fonts_selection["opcoes"] = True
            else:
                fonts_selection["opcoes"] = False
                
            if check_list.get():
                fonts_selection["listing"] = True
            else:
                fonts_selection["listing"] = False
                
            if check_subs.get():
                fonts_selection["subs"] = True
            else:
                fonts_selection["subs"] = False
                            
        def reset_fonts_selection():
            for key in fonts_selection.keys():
                fonts_selection[key] = False
           
        lista_fontes_window = tk.Toplevel(self)
        lista_fontes_window.title("Alterar Tipo de Letra")
        lista_fontes_window.geometry("400x500+750+50")
        
        font_type = ("Cascadia Mono", 12, "bold")
        
        font_options = tk.Canvas(lista_fontes_window)
        font_options.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = "nsew")
        fonts_listbox = tk.Listbox(lista_fontes_window)
        fonts_listbox.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 20, sticky = "nsew")
        
        check_titulo = tk.BooleanVar()
        check_opcoes = tk.BooleanVar()
        check_list =  tk.BooleanVar()
        check_subs = tk.BooleanVar()
        fonts_selection = {'titulo': False, 'opcoes': False, 'listing': False, 'subs': False}
                
        titulo_button = ttk.Checkbutton(font_options, text = "Cabeçalho", variable = check_titulo, onvalue = True, offvalue = False, command = sections_selection)
        titulo_button.grid(row = 0, column = 0, padx = (10, 5))
        opcoes_button = ttk.Checkbutton(font_options, text = "Opções", variable = check_opcoes, onvalue = True, offvalue = False,  command = sections_selection)
        opcoes_button.grid(row = 0, column = 1, padx = 5)
        list_button = ttk.Checkbutton(font_options, text = "Resultados", variable = check_list, onvalue = True, offvalue = False,  command = sections_selection)
        list_button.grid(row = 0, column = 2, padx = 5)
        subs_button = ttk.Checkbutton(font_options, text = "Sub-Janelas", variable = check_subs, onvalue = True, offvalue = False,  command = sections_selection)
        subs_button.grid(row = 0, column = 3, padx = (5, 10))
        
        sair_button = tk.Button(lista_fontes_window, text = "Sair", font = font_type, command = lista_fontes_window.destroy)
        sair_button.grid(row = 2, column = 0, pady = 20)
        escolher_button = tk.Button(lista_fontes_window, text = "Escolher", font = font_type, command = seleccao)
        escolher_button.grid(row = 2, column = 1, pady = 20)
        
        font_list = get_font_list()
                
        y = 0
        for i in font_list:
            fonts_listbox.insert(y, i)
            y += 1
        
        scrollbar = Scrollbar(fonts_listbox, orient=tk.VERTICAL, command = fonts_listbox.yview)
        scrollbar.grid(row = 1, column = 1, sticky = "ns")
        fonts_listbox.configure(yscrollcommand = scrollbar.set)
        
        lista_fontes_window.grid_columnconfigure(0, weight = 1)
        lista_fontes_window.grid_columnconfigure(1, weight = 1)
        lista_fontes_window.grid_rowconfigure(1, weight = 1)
        
        font_options.grid_columnconfigure(0, weight = 1)
        font_options.grid_columnconfigure(1, weight = 1)
        font_options.grid_columnconfigure(2, weight = 1)
        font_options.grid_columnconfigure(3, weight = 1)
        
        fonts_listbox.grid_columnconfigure(0, weight = 1)
        fonts_listbox.grid_columnconfigure(1, weight = 0)
        fonts_listbox.grid_rowconfigure(1, weight = 1)
        
        fonts_listbox.bind_all("<MouseWheel>", on_mousewheel)
                                    
    def buttons_layout(self):
        self.listar_viaturas = tk.Button(self, text="Listar Viaturas", width = 30, height = 2 ,
                                         font = self.comon_font, command = self.action_listar_viaturas)
        self.pes_viaturas = tk.Button(self, text="Pesquisar Viaturas", width = 30, height = 2,
                                      font = self.comon_font, command = self.janela_pesquisa)
        self.add_viatura = tk.Button(self, text="Adicionar Viatura",  width = 30, height = 2,
                                     font = self.comon_font, command = self.janela_add_veiculo)
        self.rem_viatura = tk.Button(self, text="Remover Viatura",  width = 30, height = 2,
                                     font = self.comon_font, command = self.janela_rem_veiculo)
        self.gravar_catalogo = tk.Button(self, text="Gravar Catalogo",  width = 30, height = 2,
                                         font = self.comon_font, command = self.gravar_catalogo)
        self.recarregar_catalogo = tk.Button(self, text="Recarregar Catalogo",  width = 30, height = 2,
                                             font = self.comon_font, command = self.recarregar_catalogo)
        
        self.listar_viaturas.grid(row = 1, column = 0, padx = 40, pady = 10)
        self.pes_viaturas.grid(row = 1, column = 1, padx = 40, pady = 10)
        self.add_viatura.grid(row = 2, column = 0, padx = 40, pady = 10)
        self.rem_viatura.grid(row = 2, column = 1, padx = 40, pady = 10)
        self.gravar_catalogo.grid(row = 3, column = 0, padx = 40, pady = 10)
        self.recarregar_catalogo.grid(row = 3, column = 1, padx = 40, pady = 10)
        
    def result_layout(self):
        self.result_layout_canvas = tk.Canvas(self)
        self.result_layout_canvas.grid(row = 4, column = 0, columnspan = 2, padx = 0, pady = (80, 10), sticky = 'nsew')
        self.result_layout_canvas.grid_rowconfigure(0, weight = 1)
                                            
    def limpar_result_layout(self):
        self.limpar_canvas = tk.Canvas(self)
        self.limpar_canvas.grid(row = 5, column = 0, columnspan = 2, padx = 200, pady = 10)
                
        self.limpar_res_lay = tk.Button(self.limpar_canvas, text="Limpar", width = 8, height = 1,
                                        font = self.comon_font, command = self.clean_list)
        self.limpar_res_lay.grid(row = 0, column = 0, padx = 40, pady = 0)
        self.limpar_canvas.grid_columnconfigure(0, weight = 1)
        
    def clean_list(self):
        try:
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
        def listar():
            if self.treeview_lista.get_children():
                self.treeview_lista.delete(*self.treeview_lista.get_children())
                
            for car in carros_ordenados:
                self.treeview_lista.insert('', tk.END, values = (car.marca, car.modelo, car.data, car.matricula), tags = "cor")
                            
            scrollbar = ttk.Scrollbar(self.result_layout_canvas, orient=tk.VERTICAL, command = self.treeview_lista.yview)
            self.treeview_lista.configure(yscroll=scrollbar.set)
            scrollbar.grid(row = 0, column = 1, sticky = 'ns')
                        
        def ord_marca():
            nonlocal carros_ordenados
            carros_ordenados = carros.ordenar_carros_marca()
            listar()

        def ord_modelo():
            nonlocal carros_ordenados
            carros_ordenados = carros.ordenar_carros_modelo()
            listar()
            
        def ord_data():
            nonlocal carros_ordenados
            carros_ordenados = carros.ordenar_carros_data()
            listar()
            
        def ord_matricula():
            nonlocal carros_ordenados
            carros_ordenados = carros.ordenar_carros_matricula()
            listar()
        
        cols = ("marca", "modelo", "data", "matricula")
        
        carros_ordenados = carros
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font = self.treeview_font_h)
        style.configure("Treeview", font = self.treeview_font_l)
        
        self.treeview_lista = ttk.Treeview(self.result_layout_canvas, columns = cols, show = 'headings', style = "Treeview")
        self.treeview_lista.grid(row = 0, column = 0, sticky = 'nsew', padx = 30)
        self.treeview_lista.tag_configure("cor", background = "whitesmoke")
        
        for col in cols:
            self.treeview_lista.column(col, width = 130, anchor = tk.CENTER)
        
        self.treeview_lista.heading("marca", text = "Marca", anchor = tk.CENTER, command = ord_marca)
        self.treeview_lista.heading("modelo", text = "Modelo", anchor = tk.CENTER, command = ord_modelo)
        self.treeview_lista.heading("data", text = "Data", anchor = tk.CENTER, command = ord_data)
        self.treeview_lista.heading("matricula", text = "Matricula", anchor = tk.CENTER, command = ord_matricula)
        
        listar()

        self.bind("<Button-1>", self.limpar_sel)
        self.result_layout_canvas.columnconfigure(0, weight = 1)
        
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
                
        self.marca_add_label = tk.Label(self.jan_add_veiculo, text = 'Marca', font = self.subs_font)
        self.modelo_add_label = tk.Label(self.jan_add_veiculo, text = 'Modelo', font = self.subs_font)
        self.matricula_add_label = tk.Label(self.jan_add_veiculo, text = 'Matricula', font = self.subs_font)
        self.data_add_label = tk.Label(self.jan_add_veiculo, text = 'Data', font = self.subs_font)
    
        self.marca_add_entry = tk.Entry(self.jan_add_veiculo, font = self.subs_font)
        self.modelo_add_entry = tk.Entry(self.jan_add_veiculo, font = self.subs_font)
        self.matricula_add_entry = tk.Entry(self.jan_add_veiculo, font = self.subs_font)
        self.data_add_entry = tk.Entry(self.jan_add_veiculo, font = self.subs_font)
        
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
            
        self.add_add_button = tk.Button(self.jan_add_veiculo, text="Adicionar", font = self.subs_font, height = 10, command = self.adicionar_veiculo)
        self.add_add_button.grid(row = 0, column = 2, rowspan = 4, padx = 10, pady = (40,0))

        self.add_close_button = tk.Button(self.jan_add_veiculo, text="Fechar", font = self.subs_font, width = 15, command = fechar_button)
        self.add_close_button.grid(row = 4, column = 0, columnspan = 3, pady=10)
        
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
            self.adds_mod.append(car)
            self.veiculo_adicionado_message(matricula, marca, modelo, data)
            self.jan_add_veiculo.destroy()
            try:
                if self.treeview_lista.get_children():
                    self.listar_resultados(self.carros_ordenados)
            except:
                pass
            
    def janela_rem_veiculo(self):
        self.jan_rem_veiculo = tk.Toplevel(self)
        self.jan_rem_veiculo.title("Remover Veículo")
        self.jan_rem_veiculo.geometry("470x400+250+50")
            
        self.matricula_rem_label = tk.Label(self.jan_rem_veiculo, text = 'Matricula', font = self.subs_font)
        self.matricula_rem_entry = tk.Entry(self.jan_rem_veiculo, font = self.subs_font)
        
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
            
        self.proc_rem_button = tk.Button(self.jan_rem_veiculo, text="Procurar Veiculo", width = 15 ,font = self.subs_font, command = self.rem_veiculo_proc)
        self.proc_rem_button.grid(row = 1, column = 0, columnspan = 2, padx = 10)

        self.rem_close_button = tk.Button(self.jan_rem_veiculo, text="Fechar", font = self.subs_font, width = 15, command = fechar_button)
        self.rem_close_button.grid(row = 2, column = 0, columnspan = 2, pady=10)
        
        self.jan_rem_veiculo.grid_columnconfigure(0, weight = 1)
        self.jan_rem_veiculo.grid_columnconfigure(1, weight = 1)
        
    def rem_veiculo_proc(self, **kwargs):
        matricula = self.matricula_rem_entry.get().strip()
        erro = val_mat(matricula)

        self.rem_msg_label = tk.Label(self.jan_rem_veiculo, text = '', font = self.subs_font, width = 200)
        self.rem_msg_label.grid(row = 3, column = 0,columnspan = 2, padx = 20, pady = 5)
        
        def rem_button():
            self.rem_msg_label.config(text = "Veiculo Removido", width = 150)
            if carro not in self.adds_mod:
                self.rems_mod.append(carro)
            else:
                self.adds_mod.valores_carros.pop(matricula)
            self.carros.valores_carros.pop(matricula)
            remover_button.destroy()
            self.matricula_rem_entry.delete(0, tk.END)
            try:
                if self.treeview_lista.get_children():
                    self.listar_resultados(self.carros)
            except:
                pass
            
        if erro:
            self.show_error_message(erro)
            
        elif matricula not in self.carros.valores_carros:
            self.rem_msg_label.config(text = f"Não foi encontrada matricula {matricula}", width = 200)

        else:
            carro = self.carros.valores_carros.get(matricula)
            message = f"Veiculo a remover:\nMatricula: {carro.matricula}\nMarca: {carro.marca}\nModelo: {carro.modelo}\nData: {carro.data}"
            self.rem_msg_label.config(text = message, width = 150)
            remover_button = tk.Button(self.jan_rem_veiculo, text="Remover", font = self.subs_font, width = 15, command = rem_button)
            remover_button.grid(row = 4, column = 0, columnspan = 2, pady=10)
                        
    def gravar_catalogo(self):
        self.jan_gravar_cat = tk.Toplevel(self)
        self.jan_gravar_cat.title("Gravar Catalogo")
        self.jan_gravar_cat.geometry("500x200+250+50")
        
        mensagem = f"Foram adicionados {len(self.adds_mod)} veiculos e removidos {len(self.rems_mod)} veiculos\nGravar Catálogo em Ficheiro?"
        self.gravar_cat_label = tk.Label(self.jan_gravar_cat, text = mensagem, font = self.subs_font)
        self.gravar_cat_label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 30)
        
        def ok_action():            
            self.gravar_cat_label.config(text = "Catalogo Gravado")
            self.gravar_ok_button.destroy()
            self.gravar_no_button.grid(row = 1, column = 0, columnspan = 2 ,padx = 20, pady = 20)
            self.adds_mod.clear()
            self.rems_mod.clear()
            gravar_carros(self.carros, FILEPATH)
            
        def no_action():
            self.jan_gravar_cat.destroy()
            
        self.gravar_ok_button = tk.Button(self.jan_gravar_cat, text = "Gravar", font = self.subs_font, width = 15, command = ok_action)
        self.gravar_ok_button.grid(row = 1, column = 0, padx = 20, pady = 20)
        
        self.gravar_no_button = tk.Button(self.jan_gravar_cat, text = "Fechar", font = self.subs_font, width = 15, command = no_action)
        self.gravar_no_button.grid(row = 1, column = 1, padx = 20, pady = 20)
        
        self.jan_gravar_cat.columnconfigure(0, weight = 1)
        self.jan_gravar_cat.columnconfigure(1, weight = 1)
        
    def recarregar_catalogo(self):
        self.jan_recarregar_cat = tk.Toplevel(self)
        self.jan_recarregar_cat.title("Recarregar Catalogo")
        self.jan_recarregar_cat.geometry("550x200+250+50")
        
        mensagem = f"Foram adicionados {len(self.adds_mod)} veiculos e removidos {len(self.rems_mod)} veiculos\nDescartar Alterações e Recarregar Catálogo do Ficheiro?"
        self.rec_cat_label = tk.Label(self.jan_recarregar_cat, text = mensagem, font = self.subs_font)
        self.rec_cat_label.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 30)
        
        def ok_action():            
            self.rec_cat_label.config(text = "Catalogo Recarregado")
            self.rec_ok_button.destroy()
            self.rec_no_button.grid(row = 1, column = 0, columnspan = 2 ,padx = 20, pady = 20)
            self.adds_mod.valores_carros.clear()
            self.rems_mod.valores_carros.clear()
            self.carros = ler_carros(FILEPATH)
            
        def no_action():
            self.jan_recarregar_cat.destroy()
            
        self.rec_ok_button = tk.Button(self.jan_recarregar_cat, text = "Recarregar", font = self.subs_font, width = 15, command = ok_action)
        self.rec_ok_button.grid(row = 1, column = 0, padx = 20, pady = 20)
        
        self.rec_no_button = tk.Button(self.jan_recarregar_cat, text = "Fechar", font = self.subs_font, width = 15, command = no_action)
        self.rec_no_button.grid(row = 1, column = 1, padx = 20, pady = 20)
                                                                             
    
        self.jan_recarregar_cat.columnconfigure(0, weight = 1)
        self.jan_recarregar_cat.columnconfigure(1, weight = 1)
                      
    def show_error_message(self, erro: str | list):    
        self.error_window = tk.Toplevel(self)
        self.error_window.title("Error de Introdução de Dados")

        if isinstance(erro, str):
            error_label = tk.Label(self.error_window, text = erro, font = self.subs_font)
            error_label.pack(padx = 20, pady = 10)
        
        else:
            for i in erro:
                error_label = tk.Label(self.error_window, text = i, font = self.subs_font)
                error_label.pack(padx = 20, pady = 10)
                
        def fechar_button():
            self.error_window.destroy()

        close_button = tk.Button(self.error_window, text="Fechar", font = self.subs_font, command = fechar_button)
        close_button.pack(pady=10)
            
    def veiculo_adicionado_message(self, matricula, marca, modelo, data):    
        self.veiculo_add = tk.Toplevel(self)
        self.veiculo_add.title("Inserção Correcta")

        message = f"Veiculo adicionado com os seguintes dados: \nmarca: {marca}\nmodelo: {modelo}\nmatricula: {matricula}\ndata: {data}"        
        
        msg_label = tk.Label(self.veiculo_add, text = message, font = self.subs_font)
        msg_label.pack(padx = 20, pady = 10)
                
        def ok_button():
            self.veiculo_add.destroy()

        close_button = tk.Button(self.veiculo_add, text="OK", font = self.subs_font, width = 12, command = ok_button)
        close_button.pack(pady=10)

janela = janela_inicial()
janela.mainloop()

