def quebra_substring(string_maior, string_quebra=':'):
    return string_maior.split(string_quebra)

quebra_substring('oi mundo',' ') # Funciona
quebra_substring('oi:mundo:teste',' ')  # Funciona
quebra_substring('oi:mundo:teste') # Funciona

def soma_tudo(*numeros):
    resultado = 0
    for numero in numeros:
        if isinstance(numero, int):
            resultado += numero
    return resultado

def soma_tudo(*numeros):
    lista = []
    for n in numeros: 
        if type(n) == int: 
            lista.append(n)
    return sum(lista)

def mostra_parametros(**kwargs):
    print(kwargs)

def mostra_parametros2(**blz):
    print(blz)

## Orientação a Objetos 
class PrimeiraClasse:
    pass

objeto1 = PrimeiraClasse()
objeto1.__dict__

class SegundaClasse:
    def imprime_1(self, parametro1):
        print(parametro1)

objeto2 = SegundaClasse()
objeto2.__dict__
objeto2.imprime_1('Fatec Araras')
objeto2.imprime_1([1,2,3])

class TerceiraClasse:
    def __init__(self, *args,**kwargs):
        self.param1 = args
        self.param2 = kwargs 


objeto3 = TerceiraClasse()
objeto3.__dict__
objeto4 = TerceiraClasse(1,2,3,4,nome='Fatec Araras') 
objeto4.__dict__

