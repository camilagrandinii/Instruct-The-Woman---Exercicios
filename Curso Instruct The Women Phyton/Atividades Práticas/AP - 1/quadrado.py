class Quadrado:
    def __init__(self, medida):
        self.altura=medida
        self.largura=medida

    def __str__(self):
        return f'Altura: {self.altura}, Largura: {self.largura}'

    #colocamos o property para conseguir o comportamento dos nossos getters e setters
    @property
    def altura(self): #esse método vai pegar o comportamento daquele objeto
        print("getter de altura")
        return self.__medida #alteramos a visibilidade do atributo após ele passar pelo método

    @altura.setter
    def altura(self, valor):
        print("setter de altura")

        if valor<0:
            raise ValueError()
        self.__medida=valor

    @property
    def largura(self):
        print("getter de largura")
        return self.__medida

    @largura.setter
    def largura(self, valor):
        print("setter de largura")

        if valor<0:
            raise ValueError()
        self.__medida=valor

    def area(self):
        return self.largura * self.altura

quadrado = Quadrado(2)