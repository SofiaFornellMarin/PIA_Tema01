# LISTA INICIAL CON UNOS NÚMEROS Y DOS VACÍAS EN LAS QUE SE GUARDARN LOS POSITIVOS Y LOS NEGATIVOS 
numeros = [0, 58, -94, 21, -66, -3, 0, 7, 33, 42, -3, -11, -87, 66, 23, 96]
positivos = []
negativos = []

# FUNCIÓN PARA SEPARA LOS ELEMENTOS NUMÉRICOS DE LA LISTA (el 0 no es positivo ni negativo)
def separarNumeros(lista):    
    for elemento in lista:
        if elemento == 0:
            print("Se ha encontrado el 0, no es ni positivo ni negativo")
            print("------------------------------------------------")
        elif elemento > 0:
            positivos.append(elemento)
        else:
            negativos.append(elemento)
            
#MOSTRAMOS LA LISTA INICIAL
print("Lista completa de números: ")
print(numeros)
print("------------------------------------------------")

#LLAMAMOS A LA FUNCIÓN PASÁNDOLE LA LISTA COMO PARÁMETRO
separarNumeros(numeros)

#MOSTRAMOS LAS DOS LISTAS FINALES
print("Lista de números positivos: ")
print(positivos)
print("------------------------------------------------")
print("Lista de números negativos: ")
print(negativos)
print("------------------------------------------------")


