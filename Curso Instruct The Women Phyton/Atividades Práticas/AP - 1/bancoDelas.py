#
 # Exercício Banco Delas - Instruct The Woman
 # @author - Camila Lacerda Grandini
 # 2022/2
#

from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone, rendaMensal):
        self._nome = nome
        self.__telefone = telefone
        self._rendaMensal=rendaMensal
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError()
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        if not telefone:
            raise ValueError()
        self._telefone = telefone
    
    @property
    def rendaMensal(self):
        return self._rendaMensal

    @rendaMensal.setter
    def rendaMensal(self, rendaMensal):
        if not rendaMensal or not isinstance(rendaMensal, int):
            raise ValueError()
        self._rendaMensal = rendaMensal
    
    def __str__(self):
        return f'Nome: {self._nome}, Telefone: {self.__telefone} e Renda Mensal: {self._rendaMensal}'

class Operacoes:
    def __init__(self, valor, data, hora, tipo):
        self.__valor = valor
        self._data = data
        self._hora = hora
        self._tipo = tipo

    def __str__(self):
        return f'Tipo: {self._tipo}, Valor: {self.__valor}, Data: {self._data} e Hora: {self._hora}'
        
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        if not valor:
            raise ValueError()
        self.__valor = valor
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if not data:
            raise ValueError()
        self._data = data
    
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        if not hora:
            raise ValueError()
        self._hora = hora
    
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if not tipo:
            raise ValueError()
        self._tipo = tipo

class ContaCorrente(Cliente):
    def __init__(self, nome, telefone, rendaMensal):
        super().__init__(nome, telefone, rendaMensal)
        self.__saldo = 0
        self._saques = []
        self._depositos = []
        self._chequeEpecial = rendaMensal

    def __str__(self):
        return f'Nome: {self._nome}, Saldo: {self.__saldo}, Valor Máximo do Cheque Especial: {self._chequeEpecial}'
    
    def realizarSaque(self, valor, data, hora):
        operacao = Operacoes(valor, data, hora, "Saque")
        self._saques.append(operacao)
        self.__saldo-=valor

    def realizarDeposito(self, valor, data, hora):
        operacao = Operacoes(valor, data, hora, "Depósito")
        self._depositos.append(operacao)
        self.__saldo+=valor
    
    def pegarChequeEspecial(self, valor, data, hora):
        operacao = Operacoes(valor, data, hora, "Cheque Especial")
        self._saques.append(operacao)
        self.__saldo-=valor
    
    def listarOperacoes(self):
        self.__str__()
        if not self._saques:
            print("A conta ainda não realizou nenhum saque!")
        else:
            for op in self._saques:
                print(op)
        if not self._depositos:
            print("A conta ainda não realizou nenhum depósito!")
        else:
            for op in self._depositos:
                print(op)

def contaBanco():
    nome = input("Bem Vindo ao Banco Delas! Por favor digite seu nome: ")
    print(f"Olá {nome}, é ótimo tê-la conosco.")
    opcao = 0

    while opcao!=7:
        opcao = int(input("\nDigite a opção desejada:\n1 - Abrir uma Conta\n2 - Realizar Saque\n3 - Realizar Depósito\n4 - Pedir Cheque Especial\n5 - Histórico de Operações da Conta\n6 - Consultar Infomações da Conta\n7 - Sair\n"))
        if opcao==1:
            print("Por favor digite seus dados para que possamos criar sua conta devidamente. ")
            nomeCompleto = input("Nome Completo: ")
            telefone = input("Telefone: ")
            rendaMensal = input("Renda Mensal: ")

            contaCorrente1 = ContaCorrente(nomeCompleto, telefone, rendaMensal)
        elif opcao==2:
            if contaCorrente1:
                valorSaque = int(input("Valor do Saque: "))
                contaCorrente1.realizarSaque(valorSaque, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%H:%M'))
        
        elif opcao==3:
            if contaCorrente1:
                valorDeposito = int(input("Valor do Depósito: "))
                contaCorrente1.realizarSaque(valorDeposito, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%H:%M'))
        
        elif opcao==4:
            if contaCorrente1:
                valorChequeEspecial = int(input("Valor do Cheque Especial: "))
                contaCorrente1.pegarChequeEspecial(valorChequeEspecial, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%H:%M'))   
        
        elif opcao==5:
            if contaCorrente1:
                contaCorrente1.listarOperacoes()
        
        elif opcao==6:
            if contaCorrente1:
                print(contaCorrente1)
        
        elif opcao==7:
            print("Saindo do programa...\nObrigada e tenha um ótimo dia!")
        
        else: 
            raise ValueError("Opção inválida!!!")

contaBanco()

