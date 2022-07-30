class Carro2:
    def __init__(self, ligado, cor, modelo, velocidade):
        self._ligado = ligado
        self._cor=cor
        self.__modelo=modelo
        self._velocidade = velocidade

    def __str__(self):
        return f'Ligado: {self._ligado}, Cor: {self._cor}, Modelo: {self.__modelo} e Velocidade: {self._velocidade}'
    
    #colocamos o property para conseguir o comportamento dos nossos getters e setters
    @property
    def ligado(self): #esse método vai pegar o comportamento daquele objeto
        print("getter de ligado")
        return self._ligado #alteramos a visibilidade do atributo após ele passar pelo método

    @ligado.setter
    def ligado(self, valor):
        print("setter de ligado")
        self._ligado=valor

    @property
    def cor(self):
        print("getter de cor")
        return self._cor

    @cor.setter
    def cor(self, valor):
        print("setter de cor")
        self._cor=valor

    @property
    def modelo(self):
        print("getter de modelo")
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        print("setter de modelo")
        self.__modelo=valor

    @property
    def velocidade(self):
        print("getter de velocidade")
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        print("setter de velocidade")
        self._velocidade=valor

carro = Carro2(True, "Azul", "Honda Fit", 200)
print(carro)