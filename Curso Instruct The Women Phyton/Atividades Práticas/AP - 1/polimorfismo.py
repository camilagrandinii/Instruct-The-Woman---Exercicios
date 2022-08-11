#
 # Polimorfismo com Herança - Instruct The Woman
 # @author - Camila Lacerda Grandini
 # 2022/2
#

class Animal:
    def __init__(self):
        self.__numero_patas = 0
        self.__tem_asas = False
    
    @property
    def numero_patas(self):
        return self.__numero_patas
    
    @property
    def tem_asas(self):
        return self.__tem_asas

    def emitir_som(self):
        print('...')

class Cachorro(Animal):
    def __init__(self):
        self.__numero_patas = 4
        self.__tem_asas = False
    
    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas

    def fazer_truque(self):
        print("Sento e deito")

class Gato(Animal):
    def __init__(self):
        self.__numero_patas = 4
        self.__tem_asas = False

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas
    
    def emitir_som(self):
        print("Miau")

class Calopsita(Animal):
    def __init__(self):
        self.__numero_patas = 2
        self.__tem_asas = True

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas
    
    def emitir_som(self):
        print("piuuu")
    
    def voar(self):
        print("Estou voando")

def processar_animal(animal: Animal):
    print(f"este animal tem {animal.numero_patas} patas")
    print(f"Este animal tem {animal.tem_asas} asas")
    animal.emitir_som()
    if isinstance(animal, Calopsita):
        animal.voar()
    if isinstance(animal, Cachorro):
        animal.fazer_truque()

cachorro = Cachorro()
gato = Gato()
calopsita = Calopsita()

processar_animal(cachorro)
processar_animal(gato)
processar_animal(calopsita)


