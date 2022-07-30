#definição da classe

class Televisao:
    def __init__(self):
        self.ligada=False
        self.canal=3 #canal atual
        self.canal_min=1
        self.canal_max=99
        self.volume=30
        self.volume_min=0
        self.volume_max=100
    
    def ligar(self):
        self.ligada=True
    
    def desligar(self):
        self.ligada=False
    
    def mudar_canal_para_cima(self):
        if not self.ligada:
            return 
        if self.canal<self.canal_max:
            self.canal+=1

    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return 
        if self.canal>self.canal_min:
            self.canal-=1

    def aumentar_volume(self):
        if not self.ligada:
            return
        if self.volume<self.volume_max:
            self.volume+=1

    def diminuir_volume(self):
        if not self.ligada:
            return
        if self.volume>self.volume_min:
            self.volume-=1
    
    def __str__(self) -> str:
        return f'Televisao ligada: {self.ligada} - Canal: {self.canal} - Volume: {self.volume}'
    #esse f antes da string funciona para podermos usar variável junto com string

#Criando instâncias da classe televisão

tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada))

print('tv_sala está ligada? ', tv_sala.ligada)

for _ in range(3):
    tv_sala.aumentar_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_sala volume:', tv_sala.volume)
print('tv_quarto volume: {}'.format(tv_quarto.volume))

#imprimir o conteúdo do objeto
print(f'tv_sala: {tv_sala}',)
print(f'tv_quarto: {tv_quarto}',)