# Sequencia
print('Primeiro comando')
print('Segundo comando')
print('Terceiro comando')

### Seleção 
condicao = False
if condicao:
    print('passou por aqui 1')
condicao = True
if condicao:
    print('passou por aqui 2')


lista = list(range(1,10))
for numero in lista:
    print(numero)


def caixinha_magica(numero1, numero2):
    numero3 = numero1 + numero2
    return numero3

print(caixinha_magica(2,5))
print(caixinha_magica('oi ','mundo'))

print('Testes')
assert caixinha_magica(2,5) == 7
assert caixinha_magica('oi ','mundo') == 'oi mundo'

print('Primeiro experimento com TDD')

def caixinha_magica2(parametro1, parametro2):
    return parametro1 - parametro2

assert caixinha_magica2(10, 4) == 6
assert caixinha_magica2(10, 5) == 5
assert caixinha_magica2(10, 15) == -5

# Strings ( Objetos String)
nome = 'Fatec Araras'
nome = 'Fatec Araras 2'
print(nome)
print(id(nome))
print(nome.upper())

# Lista

lista = []
lista.append('Pão')
lista.append('Queijo')
lista.append('Bacon')

for comida in lista:
    print(comida)


tupla1 = ('Pão','Bacon','Leite','Chocolate')
print(tupla1.count('Pão'))
# Range
r = range(1,15)
print(list(r))

r = range(1,15, 2)
print(list(r))