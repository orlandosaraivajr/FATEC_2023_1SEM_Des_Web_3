def caixinha_magica3(numero1, numero2):
    if numero2 <= numero1:
        return numero1 - numero2
    return 0

assert caixinha_magica3(20, 15) == 5
assert caixinha_magica3(20, 10) == 10
assert caixinha_magica3(10, 10) == 0
assert caixinha_magica3(10, 15) == 0
assert caixinha_magica3(30, 45) == 0


#### Aula 01/03/2023
# Conjuntos (set)

conjunto1 = set(range(1,15)) 
conjunto2 = set(range(10,20)) 
conjunto3 = set(range(14,25)) 

conjunto1.difference(conjunto2)
conjunto1.intersection(conjunto2)

# Remover elemento repetidos de uma lista
lista_repetida = list(range(1,10))
lista_repetida += list(range(1,10))
lista_repetida += list(range(1,15))

lista = list(set(lista_repetida))

# Dicionários
agenda = {}
type(agenda)
agenda['orlando'] = ['Eng. Sof1', 'Des. Web 2', 'Des. Web 3']
agenda['nilton'] = ['Algoritmo'] 
agenda['jose'] = '199999-9999' 
agenda['maria'] = '1988888888'
agenda['joaquim'] = ('1988888888','Rua 10, 1')

# Fazer uso do dicionário
agenda['orlando'] # Retorna uma lista
agenda['Orlando'] # Retorna KeyError

try:
    agenda['Orlando']
except KeyError:
    print('Não Encontrado')

agenda.get('orlando','Não Encontrado')
agenda.get('Orlando','Não Encontrado')

for chave in agenda.keys(): 
    print('Chave =>' + chave)
    print(agenda[chave])

