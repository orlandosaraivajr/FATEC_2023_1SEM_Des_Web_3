from avaliacao1 import extrair_chaves_dicionario
from avaliacao1 import concatenar_listas
from avaliacao1 import quebrar_string_em_listas
from avaliacao1 import gerar_lista_codigos
from avaliacao1 import gerar_lista_cidades
import pickle
import pytest

class LoadData:
    def load_list(self):
        with open('dados.bin', 'rb') as file:
            self.cidades = pickle.load(file)


class Test_extrair_chaves_dicionario(LoadData):
    def test_01(self):
        self.load_list()
        chaves = extrair_chaves_dicionario(self.cidades)
        assert isinstance(chaves, list)
        assert isinstance(chaves[0], str)
        assert len(chaves) == 7

    def test_02(self):
        chaves = extrair_chaves_dicionario({})
        assert isinstance(chaves, list)
        assert len(chaves) == 0

    def test_03(self):
        msg_erro = "'list' object has no attribute 'keys'"
        with pytest.raises(AttributeError) as error:
            extrair_chaves_dicionario([0,1,2])
        assert str(error.value) == msg_erro


class Test_concatenar_lista(LoadData):
    def test_01(self):
        self.load_list()
        lista1 = extrair_chaves_dicionario(self.cidades)
        lista = concatenar_listas(lista1, ['PA','AM'])
        assert isinstance(lista, list)
        assert len(lista) == 9
        assert lista == ['MG', 'SP', 'RJ', 'ES', 'RS', 'SC', 'PR', 'PA','AM']

    def test_02(self):
        lista = concatenar_listas([1,2], ['3','4'])
        assert isinstance(lista, list)
        assert len(lista) == 4
        assert lista == [1, 2,'3','4']

    def test_03(self):
        msg_erro = 'can only concatenate list (not "int") to list'
        with pytest.raises(TypeError) as error:
            concatenar_listas([1,2], 3)
        assert str(error.value) == msg_erro


class Test_quebrar_string_em_listas:
    def test_01(self):
        string_maior = 'Fatec_Araras'
        lista = quebrar_string_em_listas(string_maior, '_')
        assert isinstance(lista, list)
        assert len(lista) == 2
        assert lista == ['Fatec', 'Araras']

    def test_02(self):
        string_maior = 'Fatec_Araras'
        lista = quebrar_string_em_listas(string_maior, ':')
        assert isinstance(lista, list)
        assert len(lista) == 1
        assert lista == ['Fatec_Araras']

    def test_03(self):
        string_maior = 'Fatec:Araras'
        lista = quebrar_string_em_listas(string_maior, ':')
        assert isinstance(lista, list)
        assert len(lista) == 2
        assert lista == ['Fatec', 'Araras']


class Test_gerar_lista_codigos:
    def test_01(self):
        lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO',
                        '3502002:ANALANDIA', '3502101:ANDRADINA']

        lista_gerada = gerar_lista_codigos(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 4
        assert lista_gerada == ['3501806', '3501905','3502002', '3502101']

    def test_02(self):
        lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO']
        lista_gerada = gerar_lista_codigos(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 2
        assert lista_gerada == ['3501806', '3501905']

    def test_03(self):
        lista = []
        lista_gerada = gerar_lista_codigos(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 0
        assert lista_gerada == []


class Test_gerar_lista_cidades:
    def test_01(self):
        lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO',
                        '3502002:ANALANDIA', '3502101:ANDRADINA']

        lista_gerada = gerar_lista_cidades(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 4
        assert lista_gerada == ['AMERICO DE CAMPOS', 'AMPARO','ANALANDIA', 'ANDRADINA']

    def test_02(self):
        lista = ['3501806:AMERICO DE CAMPOS', '3501905:AMPARO']
        lista_gerada = gerar_lista_cidades(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 2
        assert lista_gerada == ['AMERICO DE CAMPOS', 'AMPARO']

    def test_03(self):
        lista = []
        lista_gerada = gerar_lista_cidades(lista)
        assert isinstance(lista_gerada, list)
        assert len(lista_gerada) == 0
        assert lista_gerada == []