from spanlp.palabrota import Palabrota
from spanlp.domain.countries import Country
import csv

def leer_archivo(nombre_archivo:str='', separador_datos:str='', columna:str=''):
    tweets = []
    with open(nombre_archivo, encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=separador_datos)
        for fila in reader:
            tweets.append(fila[columna])
    return tweets


def validar_vulgaridades(data:list=None, pais:list=None, incluir:list=None, excluir:list=None):
    if data is None or len(data) == 0:
        raise Exception("Oiga! para validar vulgaridades debe enviar datos. esta enviando datos nulos o vacios.")
    
    contador_palabrotas = 0
    validador = Palabrota(countries=pais, include=incluir, exclude=excluir)
    
    for texto in data:
        if isinstance(texto, str):
            es_palabrota = validador.contains_palabrota(texto)
            if es_palabrota:
                contador_palabrotas += 1
    return (contador_palabrotas>0,contador_palabrotas)


def pedir_pais():
    print(""" Paises disponibles para el análisis: 
            1 Colombia
            2 Venezuela
            3 Mexico
            4 Argentina
            5 Todos""")
    pais_seleccionado = int(input("Ingrese:"))
    return {
        1: [Country.COLOMBIA],
        2: [Country.VENEZUELA],
        3: [Country.MEXICO],
        4: [Country.ARGENTINA],
        5: [Country.COLOMBIA, Country.VENEZUELA, Country.MEXICO, Country.ARGENTINA]
    }.get(pais_seleccionado, None)


def pedir_palabras_incluir_excluir():
    print("¿Desea incluir o excluir palabras en la busqueda? (SI/NO):")
    quiere_incluir_excluir = input("Respuesta (SI/NO) :")
    if len(quiere_incluir_excluir) > 0 and quiere_incluir_excluir.lower() == "si":
        print("Ingrese la palabras a INCLUIR (separadas por coma (,)) :")
        palabras_a_incluir = input("Incluir:")
        print("Ingrese la palabras a EXCLUIR (separadas por coma (,)) :")
        palabras_a_excluir = input("Excluir:")
        return (palabras_a_incluir.split(","), palabras_a_excluir.split(","))
    else:
        return (None,None)


comments = leer_archivo(nombre_archivo='data/tweets.csv', separador_datos='|', columna='comment_1')
print(comments)
pais = pedir_pais()
palabras_a_incluir, palabras_a_excluir = pedir_palabras_incluir_excluir()
contiene, cantidad = validar_vulgaridades(comments, pais, palabras_a_incluir, palabras_a_excluir)

print(f"Los datos contienen {cantidad} vulgaridades para {pais}." if contiene else "Los datos no contienen vulgaridades.")

