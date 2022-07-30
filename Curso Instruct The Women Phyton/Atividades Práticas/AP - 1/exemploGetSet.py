class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._atualizacoes = 0
    # getter
    @property
    def nome1(self):
        return self._nome
    # setter de name
    @nome1.setter
    def nome1(self, nome):
        self._atualizacoes += 1
        self._nome = nome

    # getter de atualizacoes
    @property
    def atualizacoes(self):
        return self._atualizacoes
    def dizer_oi(self):
        print(f'Oi,{self.nome1}')
        print(f'{self.nome1} teve seu nome alterado {self.atualizacoes} vezes')

maria = Pessoa('Maria')
maria.dizer_oi()
maria.nome1 = 'Alessandra'
maria.dizer_oi()
maria.nome1 = 'Beatriz'
maria.dizer_oi()