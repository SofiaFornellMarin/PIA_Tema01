#LIBRERIAS NECESARIAS
import re 
#PETICIÓN DE FRASE AL USUARIO
frase = input("Escribe una frase:   ")
print("-----------------------------------------------------------")
print("Frase introducida:   ", frase)
print("-----------------------------------------------------------")
#ELIMINACIÓN DE SIGNOS DE PUNTUACIÓN
texto = re.sub(r'[^\w\s]', '', frase) 
print("Frase sin signos de puntuación:  ", texto)
print("-----------------------------------------------------------")
#CONVERSIÓN A MINÚNCULAS
textoMinus = texto.lower()
print("Frase sin signos de puntuación y en minúsculas:  ", textoMinus)
print("-----------------------------------------------------------")
#SEPARACIÓN DEL TEXTO EN PALABRAS EN UNA LISTA
lista = textoMinus.split()
print("Lista:   ", lista)
print("-----------------------------------------------------------")
#ORDENACIÓN DE LA LISTA DE PALABRAS
listaOrdenada = lista.sort()
print("Lista ordenada:   ", listaOrdenada)
print("-----------------------------------------------------------")
#CÁLCULO DE LA FRECUENCIA DE CADA PALABRA
frecuenciaPalab = []
for frec in lista:
    frecuenciaPalab.append(lista.count(frec))
print("Frecuencia palabras:   ", frecuenciaPalab)
print("-----------------------------------------------------------")
#CREAMOS UN DICCIONARIO UNIENDO DOS LISTAS DE LA MISMA LONGITUD (ya no tiene duplicados)
diccionario = zip(lista, frecuenciaPalab)
dicc01 = dict(diccionario)          #Para mostrarlo bien se ha de convertir de zip a diccionario
print("Diccionario:   ", dicc01)     
print("-----------------------------------------------------------")


