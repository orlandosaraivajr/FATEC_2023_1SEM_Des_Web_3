from avaliacao1 import extrair_chaves_dicionario
from avaliacao1 import concatenar_listas
from avaliacao1 import quebrar_string_em_listas
from avaliacao1 import gerar_lista_codigos
from avaliacao1 import gerar_lista_cidades
import pickle

def load_list():
    with open('dados.bin', 'rb') as file:
        cidades = pickle.load(file)
    return cidades
cidades = load_list()

chaves = extrair_chaves_dicionario(cidades)
assert isinstance(chaves, list)
assert isinstance(chaves[0], str)
assert len(chaves) == 7
chaves = extrair_chaves_dicionario({})
assert isinstance(chaves, list)
assert len(chaves) == 0

lista1 = extrair_chaves_dicionario(cidades)
lista = concatenar_listas(lista1, ['PA','AM'])
assert isinstance(lista, list)
assert len(lista) == 9
assert lista == ['MG', 'SP', 'RJ', 'ES', 'RS', 'SC', 'PR', 'PA','AM']
lista = concatenar_listas([1,2], ['3','4'])
assert isinstance(lista, list)
assert len(lista) == 4
assert lista == [1, 2,'3','4']

string_maior = 'Fatec_Araras'
lista = quebrar_string_em_listas(string_maior, '_')
assert isinstance(lista, list)
assert len(lista) == 2
assert lista == ['Fatec', 'Araras']
lista = quebrar_string_em_listas(string_maior, ':')
assert isinstance(lista, list)
assert len(lista) == 1
assert lista == ['Fatec_Araras']
string_maior = 'Fatec:Araras'
lista = quebrar_string_em_listas(string_maior, ':')
assert isinstance(lista, list)
assert len(lista) == 2
assert lista == ['Fatec', 'Araras']


lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO',
                        '3502002:ANALANDIA', '3502101:ANDRADINA']
lista_gerada = gerar_lista_codigos(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 4
assert lista_gerada == ['3501806', '3501905','3502002', '3502101']
lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO']
lista_gerada = gerar_lista_codigos(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 2
assert lista_gerada == ['3501806', '3501905']
lista = []
lista_gerada = gerar_lista_codigos(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 0
assert lista_gerada == []

lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO',
                '3502002:ANALANDIA', '3502101:ANDRADINA']
lista_gerada = gerar_lista_cidades(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 4
assert lista_gerada == ['AMERICO DE CAMPOS', 'AMPARO','ANALANDIA', 'ANDRADINA']
lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO']
lista_gerada = gerar_lista_cidades(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 2
assert lista_gerada == ['AMERICO DE CAMPOS', 'AMPARO']
lista = []
lista_gerada = gerar_lista_cidades(lista)
assert isinstance(lista_gerada, list)
assert len(lista_gerada) == 0
assert lista_gerada == []
