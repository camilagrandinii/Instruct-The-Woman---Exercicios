#definição da classe
class Carro:
    def __init__(self):
        self.ligado=False
        self.cor=0
        self.modelo=0
        self.velocidade=0
        self.velocidade_max=300
        self.velocidade_min=0
    
    def ligar(self):
        self.ligado=True
    
    def desligar(self):
        self.ligado=False
    
    def acelerar(self):
        if not self.ligado:
            return 
        if self.velocidade<self.velocidade_max:
            self.velocidade+=1

    def desacelerar(self):
        if not self.ligado:
            return 
        if self.velocidade>self.velocidade_min:
            self.velocidade-=1
    
    def __str__(self) -> str:
        return f'Ligado: {self.ligado} - Cor: {self.cor} - Modelo: {self.modelo} - Velocidade: {self.velocidade}'

#Criando instância da classe carro
carro1 = Carro()
carro1.cor='turquesa'
carro1.modelo='Honda Fit'
print(f'INSTÂNCIA CRIADA:\n{carro1}',)

carro1.ligar()

print(f'CARRO 1 APÓS LIGAR:\n{carro1}',)

#Acelerando o carro
for _ in range(60):
    carro1.acelerar()

print(f'CARRO 1 ACELERADO PARA 60:\n{carro1}',)

#Desacelerando o carro
for _ in range(60):
    carro1.desacelerar()

print(f'CARRO 1 PARADO:\n{carro1}',)
