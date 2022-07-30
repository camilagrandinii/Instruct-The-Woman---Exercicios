class Pessoa:
    def __init__(self, nome):
        self._nome=nome
        self._tipo="Pessoa"
    def __str__(self, nome):
        return f'Nome: {self._nome}'
    def falar_oi(self):
        print("Oi, meu nome é {}".format(self._nome))
    def falar_tipo(self):
        print("Meu tipo é {}".format(self._tipo))
    
pessoa = Pessoa("Maria")
pessoa.falar_oi()
pessoa.falar_tipo()

#a classe estudante herda a classe pessoa
#todos os atributos não privados vao poder ser acessados
class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome) #chama o construtor da classe base
        #dentro do parametro falamos o que queremos herdar = no caso o (nome)
        self._curso=curso

    def __str__(self):
        return f'Nome: {self._nome}, Curso: {self._curso}'

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso "{self._curso}"')
    
    def falar_tipo(self):
        self._tipo = "Estudante"
        return super().falar_tipo()

estudante = Estudante("Camila", "Ciencia da Computacao")
estudante.falar_curso()
estudante.falar_tipo()
estudante.falar_oi()
    
