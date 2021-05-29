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


def validar_vulgaridades(data:list=None, pais:list=None):
    if data is None or len(data) == 0:
        raise Exception("Oiga! para validar vulgaridades debe enviar datos. esta enviando datos nulos o vacios.")
    
    contador_palabrotas = 0
    validador = Palabrota(countries=pais)
    
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


comments = leer_archivo(nombre_archivo='data/tweets.csv', separador_datos='|', columna='comment_1')
pais = pedir_pais()
contiene, cantidad = validar_vulgaridades(comments, pais)

print(f"Los datos contienen {cantidad} vulgaridades para {pais}." if contiene else "Los datos no contienen vulgaridades.")

