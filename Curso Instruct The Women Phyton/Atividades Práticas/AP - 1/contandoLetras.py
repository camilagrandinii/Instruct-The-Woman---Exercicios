#
 #   >>> freq{"banana"}
 #   {'b': 1, 'a': 3, 'n': 2}
 #   >>> freq{"aha"}
 #   {'a': 2, 'h': 1}  
#

from collections import Counter

def freq(s):
    return dict(Counter(s).items())

# OU

# Complexidade linear em tempo de execução e memória
def freq2(s):
    r={}
    for c in s:
        r[c] = r.get(c, 0) + 1 # Procura o c no dicionário, SE achar retorna o valor dele, SENAO retorna 0
    return r