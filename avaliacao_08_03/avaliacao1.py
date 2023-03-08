import pickle 
import csv
         
def extrair_chaves_dicionario(cidades):
    return list(cidades.keys())

def concatenar_listas(lista1, lista2):
    pass

def quebrar_string_em_listas(string_maior, string_quebra):
    pass

def gerar_lista_codigos(cidades):
    pass

def gerar_lista_cidades(cidades):
    pass

if __name__ == "__main__":
    with open('dados.bin', 'rb') as file:
        dados = pickle.load(file)
'''
    estados = extrair_chaves_dicionario(dados)
    lista_codigos_cidades = []
    lista_cidades = []
    for estado in estados:
        lista1 = gerar_lista_cidades(dados[estado])
        lista2 = gerar_lista_codigos(dados[estado])
        lista_cidades = concatenar_listas(lista_cidades, lista1)
        lista_codigos_cidades = concatenar_listas(lista_codigos_cidades, lista2)
'''
