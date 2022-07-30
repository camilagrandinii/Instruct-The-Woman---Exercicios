#Encapsulamento

class Pessoa:
    def __init__(self,nome,profissao,identidade):
        self._nome=nome
        self.profissao=profissao
        self.__identidade=identidade
    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa("Ana", "Estudante", 123456)

pessoa1.profissao="Estudante"
pessoa1.__identidade=1234567 #NAO VAI FAZER EFEITO, pois a variável identidade não está visível para todo mundo

print(pessoa1)

pessoa1._nome="Julia" #VAI FAZER EFEITO

print(pessoa1)
print(pessoa1._nome)
