
CSV_DEFAULT_DELIM = ','

class Carro:
    def __init__ (self, matricula: str, marca: str, modelo: str, data: str):
        
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data

    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM):
        attrs = linha.split(delim)
        return Carro(
            matricula = str(attrs[0]),
            marca = str(attrs[1]),
            modelo = str(attrs[2]),
            data = str(attrs[3])
        )    

class CatalogoCarros:
    def __init__(self):
        self._carros = {}
        
    def append(self, car: Carro):
        self._carros[car.matricula] = car    
                              
    def pesquisa(self, procura: str, tipo: str):
        encontrados = CatalogoCarros()
        match tipo:
            case 'matricula':
                for car in self._carros.values():
                    if car.matricula == procura:
                        encontrados.append(car)
            case 'marca':
                for car in self._carros.values():
                    if car.marca == procura:
                        encontrados.append(car)
            case 'modelo':
                for car in self._carros.values():
                    if car.modelo == procura:
                        encontrados.append(car)
            case 'data':
                for car in self._carros.values():
                    if car.data == procura:
                        encontrados.append(car)
        if encontrados:
            return encontrados
                    
    def ordenar_carros_marca(self):
        carros_ordenados = CatalogoCarros()
        lista_ordenada = sorted(self._carros.values(), key=lambda Carro: (Carro.marca, Carro.modelo, Carro.data))
        for i in range(len(lista_ordenada)):
            carros_ordenados.append(lista_ordenada[i])
        return carros_ordenados
    
    def ordenar_carros_modelo(self):
        carros_ordenados = CatalogoCarros()
        lista_ordenada = sorted(self._carros.values(), key=lambda Carro: (Carro.modelo, Carro.marca, Carro.data))
        for i in range(len(lista_ordenada)):
            carros_ordenados.append(lista_ordenada[i])
        return carros_ordenados
    
    def ordenar_carros_data(self):
        carros_ordenados = CatalogoCarros()
        lista_ordenada = sorted(self._carros.values(), key=lambda Carro: (Carro.data, Carro.marca, Carro.modelo))
        for i in range(len(lista_ordenada)):
            carros_ordenados.append(lista_ordenada[i])
        return carros_ordenados
    
    def ordenar_carros_matricula(self):
        carros_ordenados = CatalogoCarros()
        lista_ordenada = sorted(self._carros.values(), key=lambda Carro: (Carro.matricula, Carro.marca, Carro.modelo, Carro.data))
        for i in range(len(lista_ordenada)):
            carros_ordenados.append(lista_ordenada[i])
        return carros_ordenados
                               
    def __len__(self):
        return len(self._carros)
    
    def __iter__(self):
        for car in self._carros.values():
            yield car
    
    @property
    def valores_carros(self):
        return self._carros  
    