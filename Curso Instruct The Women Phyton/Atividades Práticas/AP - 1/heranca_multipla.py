class Logavel:
    def __init__(self):
        self.nome_da_classe=""

    def logar(self, mensagem):
        print("Mensagem da classe "+self.nome_da_classe+": "+mensagem)

class Conexao:
    def __init__(self):
        self.servidor=""
    def conectar(self):
        print("Conectando ao banco de dados no servidor "+self.servidor)
        #Logica para realizar a conexao com o BD

class MySqlDataBase(Conexao, Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = "MySQLDataBase"
        self.servidor = "Meu Servidor"

def Framework(item):
    if isinstance(item, Conexao):
        item.conectar()
    if isinstance(item, Logavel):
        mensagem = 'Boa noite, minhas queridas'
        item.logar(mensagem)
conexao_mysql = MySqlDataBase()
Framework(conexao_mysql)
    