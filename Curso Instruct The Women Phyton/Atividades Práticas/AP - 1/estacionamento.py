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
    def placa(self, placa):
        print("getter de placa")
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if not valor:
            raise ValueError()
        self.__medida = valor

    @property
    def estacionado(self):
        print("getter de estacionado")
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


class Moto(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)
        self._tipo = "Moto"


class Vaga:
    def __init__(self, id, tipo):
        self.__idVaga = id
        self.tipo = tipo
        self.livre = True
        self.placa = None

        if self.tipo != 'carro' and self.tipo != 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')

    def ocupar(self, placa, tipo):
        if self.livre:
            self.placa = placa
            self.tipo = tipo
            self.livre = False
            self.inicializar_vagas(self)
        else:
            raise ValueError(f'A vaga {self.identificador} já está ocupada')

    def desocupar(self):
        if self.livre:
            raise ValueError(f'A vaga {self.identificador} já está desocupada')
        else:
            self.placa = None
            self.tipo = ""
            self.livre = True


class Estacionamento():
    def __init__(self, vagasCarro, vagasMoto):
        self.vagas_de_carro = []
        self.vagas_de_moto = []
        self.total_vagas_livres_moto = 25
        self.total_vagas_livres_carro = 25
        self.inicializar_vagas(vagasCarro, vagasMoto)

    def __str__(self):
        return f'Vagas de Carro: {self.vagas_de_carro}, Vagas de Moto: {self.vagas_de_moto}, Carros para Vagas: {self.carro_para_vaga}, Motos para Vagas: {self.moto_para_vaga}, Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}'

    def estacionar_veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Carro):
            self.estacionar_carro(veiculo)
        elif isinstance(veiculo, Moto):
            self.estacionar_moto(veiculo)

    def estacionar_carro(self, carro: Carro):
        if self.total_vagas_livres_carro > 0:
            self.total_vagas_livres_carro -= 1
            self.vagas_de_carro[0].ocupar(
                carro.__placa, "carro")  # Teste para incluir carro na vaga
            print(self.vagas_de_carro[0]
                  )  # Teste para ver o que tem dentro de vagas_de_carro
            print("Carro estacionado")
        else:
            print("Não existem vagas disponíveis")

    def estacionar_moto(self, moto: Moto):
        if self.total_vagas_livres_moto > 0:
            self.total_vagas_livres_moto -= 1
            self.moto_para_vaga.append(moto)
        elif self.total_vagas_livres_carro > 0:
            self.total_vagas_livres_carro -= 1
            self.carro_para_vaga.append(moto)
            print("Moto estacionada")
        else:
            print("Não existem vagas disponíveis")

    def remover_carro(self, carro: Carro):
        self.carro_para_vaga.remove(carro.__placa)
        self.total_vagas_livres_carro += 1
        print("Carro removido")

    def remover_moto(self, moto: Moto):
        if moto in self.moto_para_vaga:
            self.moto_para_vaga.remove(moto.__placa)
            self.total_vagas_livres_moto += 1
        elif moto in self.carro_para_vaga:
            self.carro_para_vaga.remove(moto.__placa)
            self.total_vagas_livres_carro += 1
        print("Moto removida")

    def estado_do_estacionamento(self):
        return f'Vagas de Carro: {self.vagas_de_carro}, Vagas de Moto: {self.vagas_de_moto}, Carros para Vagas: {self.carro_para_vaga}, Motos para Vagas: {self.moto_para_vaga}, Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}'

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
    while opcao != 2:
        opcao = int(input("MENU\n1 - Cadastrar Veículo\n2 - Sair\n"))
        if opcao == 1:

            placa = input("Digite a placa do seu veículo: ")
            tipo = int(input("\nSeu veículo é: \n1 - Carro\n2 - Moto\n"))

            if tipo == 1:
                veiculo = Carro(placa, False)
            elif tipo == 2:
                veiculo = Moto(placa, False)

            opcao2 = int(
                input(
                    "\nVocê deseja estacionar seu veículo?\n1 - Sim\n2 - Não\n"
                ))
            if opcao2 == 1:
                estacionamento.estacionar_veiculo(veiculo)
            elif opcao2 == 2:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida!!!")

        elif opcao == 2:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!!!")

main()
