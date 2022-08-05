#
 # Exercício Estacionamento - Instruct The Woman
 # @author - Camila Lacerda Grandini
 # 2022/2
#
class Veiculo:
    def __init__(self, placa, estacionado):
        self.placa = placa
        self.estacionado = estacionado
        self.tipo = ""

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not valor:
            raise ValueError()
        self.__placa = valor

    @property
    def estacionado(self):
        return self._estacionado

    @estacionado.setter
    def estacionado(self, valor):
        self._estacionado = valor

    def estacionar(self):
        if self.estacionado:
            raise ValueError(
                f'O carro {self.placa} já está no estacionamento.')

    def sair_da_vaga():
        print("sair da vaga")


class Carro(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)
        self._tipo = "Carro"
    
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not valor:
            raise ValueError()
        self.__placa = valor


class Moto(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)
        self._tipo = "Moto"
    
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not valor:
            raise ValueError()
        self.__placa = valor


class Vaga:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.livre = True
        self.placa = None

        if self.tipo != 'carro' and self.tipo != 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')
    def __str__(self):
        return f'ID: {self.__id}, Tipo: {self.tipo}, Livre: {self._livre} e Placa: {self._placa}'

    def ocupar(self, placa, tipo):
        if self.livre:
            self.placa = placa
            self.tipo = tipo
            self.livre = False
        else:
            raise ValueError(f'A vaga {self.__id} já está ocupada')

    def desocupar(self):
        if self.livre:
            raise ValueError(f'A vaga {self.__id} já está desocupada')
        else:
            self.placa = None
            self.tipo = ""
            self.livre = True
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if not valor:
            raise ValueError()
        self.__id = valor
    
    @property
    def livre(self):
        return self._livre

    @livre.setter
    def livre(self, valor):
        self._livre= valor
    
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, valor):
        self._placa= valor

class Estacionamento():
    def __init__(self, vagasCarro, vagasMoto):
        self.vagas_de_carro = []
        self.vagas_de_moto = []
        self.total_vagas_livres_moto = vagasMoto
        self.total_vagas_livres_carro = vagasCarro
        self.inicializar_vagas(vagasCarro, vagasMoto)

    def __str__(self):
        return f'Vagas de Carro: {self.vagas_de_carro}, Vagas de Moto: {self.vagas_de_moto}, Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}'

    def estacionar_veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Carro):
            self.estacionar_carro(veiculo)
        elif isinstance(veiculo, Moto):
            self.estacionar_moto(veiculo)

    def retirar_veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Carro):
            self.remover_carro(veiculo)
        elif isinstance(veiculo, Moto):
            self.remover_moto(veiculo)

    def estacionar_carro(self, carro: Carro):
        vagaLivre=0
        if self.total_vagas_livres_carro > 0:
            self.total_vagas_livres_carro -= 1
            for v in self.vagas_de_carro:
                if v.livre:
                    vagaLivre = v.id
                    vagaLivre = int(vagaLivre[1:])-1
                    break
            self.vagas_de_carro[vagaLivre].ocupar(
                carro.placa, "carro")  # Teste para incluir carro na vaga
            print("Carro estacionado")
        else:
            print("Não existem vagas disponíveis")
    
    def estacionar_moto(self, moto: Moto):
        if self.total_vagas_livres_moto > 0:
            self.total_vagas_livres_moto -= 1
            for v in self.vagas_de_moto:
                if v.livre:
                    vagaLivre = v.id
                    vagaLivre = int(vagaLivre[1:])-1
                    break
            self.vagas_de_moto[vagaLivre].ocupar(
                moto.placa, "moto")
            print("Moto estacionada")

        elif self.total_vagas_livres_carro > 0:
            self.total_vagas_livres_carro -= 1
            for v in self.vagas_de_carro:
                if v.livre:
                    vagaLivre = v.id
                    vagaLivre = int(vagaLivre[1:])-1
                    break
            self.vagas_de_carro[vagaLivre].ocupar(
                moto.placa, "carro")
            print("Moto estacionada")
        else:
            print("Não existem vagas disponíveis")
    
    def placa_no_estacionamento_carro(self, placa):
        for v in self.vagas_de_carro:
            if placa==v.placa:
                return True
        return False
    def placa_no_estacionamento_moto(self, placa):
        for v in self.vagas_de_moto:
            if placa==v.placa:
                return True
        return False
        
    def remover_carro(self, carro: Carro):
        if self.placa_no_estacionamento_carro(carro.placa):
            for v in self.vagas_de_carro:
                if v.placa==carro.placa:
                    v.desocupar()
        else:
            print("O carro em questão não está no estacionamento")
        self.total_vagas_livres_carro += 1
        print("Carro removido")

    def remover_moto(self, moto: Moto):
        if self.placa_no_estacionamento_moto(moto.placa):
            for v in self.vagas_de_moto:
                if v.placa==moto.placa:
                    v.desocupar()
            self.total_vagas_livres_moto += 1
            print("Moto removida")
        elif self.placa_no_estacionamento_carro(moto.placa):
            for v in self.vagas_de_carro:
                if v.placa==moto.placa:
                    v.desocupar()
            self.total_vagas_livres_carro += 1
            print("Moto removida")
        else:
            print("A moto em questão não está no estacionamento")

    def estado_do_estacionamento(self):
        for v in self.vagas_de_carro:
            print(v)
        for v in self.vagas_de_moto:
            print(v)
        print(f'Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}')

    def inicializar_vagas(self, vagasCarro, vagasMoto):
        self.vagas_de_carro = [
            Vaga(id=f"C{n}", tipo="carro") for n in range(1, vagasCarro + 1)
        ]
        self.vagas_de_moto = [
            Vaga(id=f"M{n}", tipo="moto") for n in range(1, vagasMoto + 1)
        ]


def main():
    opcao = 0
    estacionamento = Estacionamento(25, 25)
    while opcao != 4:
        opcao = int(
        input(
            "\nMENU:\n1 - Estacionar Veículo\n2 - Remover Veículo\n3 - Estado do Estacionamento\n4 - Sair\n"
        ))
        if opcao == 1 or opcao == 2:

            placa = input("Digite a placa do seu veículo: ")

            tipo = int(input("\nSeu veículo é: \n1 - Carro\n2 - Moto\n"))

            if tipo == 1:
                veiculo = Carro(placa, False)
            elif tipo == 2:
                veiculo = Moto(placa, False)
            else:
                print("Tipo inválido!!!")

            if opcao == 1:
                estacionamento.estacionar_veiculo(veiculo)
            elif opcao == 2:
                estacionamento.retirar_veiculo(veiculo)

        elif opcao == 3:
            estacionamento.estado_do_estacionamento()
            
        elif opcao == 4:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida!!!")

main()
