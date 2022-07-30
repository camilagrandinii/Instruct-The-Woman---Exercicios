#PILHA = first in last out
#são implementadas como arranjos em que
#as inserções e remoções seguem protocolo
#específico

pilha = [1, 1, 2, 3, 5]
print("Pilha: ", pilha)

pilha.append(20)
print("Inserindo outro elemento: ", pilha)

pilha.pop()
print("Removendo um elemento: ", pilha)

pilha.pop()
print("Removendo outro elemento: ", pilha)


#FILA = first in first out
#são implementadas como uma lista

from collections import deque
 
q = deque()
 
q.append('a')
q.append('b')
q.append('c')
 
print("Fila inicial: ")
print(q)
 
print("\nElementos sendo desemfileirados:")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nFila após as mudanças:")
print(q)

#TUPLA = first in first out imutável
#podemos modificar o conteúdo da variável, MAS não a estrutura da tupla

# tupla com parênteses / declaração implícita
tupla_numeros = (10, 20, 30)
print("\nTupla com Parênteses:",tupla_numeros, "\n")

#tupla sem parênteses / declaração implícita
tupla_nova = 10, 20, 30
print("\nTupla sem Parênteses:",tupla_numeros, "\n")
print(tupla_nova, "\n")

# declaração explícita
nova_tupla = tuple("teste")
print("\nDupla com Declaração Explícita:",nova_tupla, "\n")

#podemos também nomear os elementos de uma tupla
from collections import namedtuple
Estados = namedtuple('Estados', ['sigla', 'nome'])
estado_sp = Estados('SP', 'São Paulo')

print(estado_sp)
print(estado_sp.sigla)
print(estado_sp.nome)

#podemos atribuir variáveis dessa forma
#cada uma vai ser atribuída na ordem em que as tuplas foram definidas
sigla, nomeEstado = estado_sp
print(sigla, nomeEstado)

siglas_estados = ('MG', 'SP', 'ES', 'RJ')
print('RJ' in siglas_estados)