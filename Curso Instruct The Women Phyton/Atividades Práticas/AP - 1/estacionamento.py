class Estacionamento:
    def __init__(self):
        self._vagas_de_carro=25
        self._vagas_de_moto=25
        self.carro_para_vaga=0
        self.moto_para_vaga=0
        self.total_vagas_livres_moto=25
        self.total_vagas_livres_carro=25

    def __str__(self):
        return f'Vagas de Carro: {self.vagas_de_carro}, Vagas de Moto: {self.vagas_de_moto}, Carros para Vagas: {self.carro_para_vaga}, Motos para Vagas: {self.moto_para_vaga}, Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}'

    def estacionar_carro(self, carro):
        self.total_vagas_livre_carro-=1
        print("Carro estacionado")
    
    def estacionar_moto(self, moto):
        self.total_vagas_livre_moto-=1
        print("Moto estacionada")

    def remover_carro(self, carro):
        print("Carro removido")
    
    def remover_moto(self, moto):
        print("Moto removida")

    def estado_do_estacionamento(self):
        return f'Vagas de Carro: {self.vagas_de_carro}, Vagas de Moto: {self.vagas_de_moto}, Carros para Vagas: {self.carro_para_vaga}, Motos para Vagas: {self.moto_para_vaga}, Total de Vagas Livres Moto: {self.total_vagas_livres_moto} e Total Vagas Livres Carro: {self.total_vagas_livres_carro}'


class Veiculo:
    def __init__(self, placa, estacionado):
        self.__placa=placa
        self.estacionado=estacionado
        self.tipo=""
    
    def estacionar():
        print("estacionar")
    
    def sair_da_vaga():
        print("sair da vaga")
class Carro(Veiculo):
    def __init__(self, placa, estacionado):
        self._tipo = "Carro"
        super().__init__(placa, estacionado)
        
class Moto(Veiculo):
    def __init__(self, placa, estacionado):
        self._tipo = "Moto"
        super().__init__(placa, estacionado)
class Vaga:
    def __init__(self):
        self.id=0
        self.tipo
        self.livre
        self.placa

    def ocupar():
        print("ocupad")
    
    def desocupar():
        print("desocupar")
