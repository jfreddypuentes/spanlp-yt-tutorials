from spanlp.palabrota import Palabrota
import csv

def leer_archivo(nombre_archivo:str='', separador_datos:str='', columna:str=''):
    tweets = []
    with open(nombre_archivo, encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=separador_datos)
        for fila in reader:
            tweets.append(fila[columna])
    return tweets


def validar_vulgaridades(data:list=None):
    if data is None or len(data) == 0:
        raise Exception("Oiga! para validar vulgaridades debe enviar datos. esta enviando datos nulos o vacios.")
    
    contador_palabrotas = 0
    validador = Palabrota()
    
    for texto in data:
        if isinstance(texto, str):
            es_palabrota = validador.contains_palabrota(texto)
            if es_palabrota:
                contador_palabrotas += 1
    return (contador_palabrotas>0,contador_palabrotas)


comments = leer_archivo(nombre_archivo='tweets.csv', separador_datos='|', columna='comment_1')
contiene, cantidad = validar_vulgaridades(comments)

print(f"Los datos contienen {cantidad} vulgaridades." if contiene else "Los datos no contienen vulgaridades.")
