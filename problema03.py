#IMPORTACIONES DE MÓDULOS NECESARIOS
import re

#PATRÓN PARA CONTROL DE ENTRADA
patron = re.compile("^[xX]$|^[-?\d+$]")

#CONJUNTOS DE DATOS UTILIZADOS
conjuntoAux = set()
conjunto1 = set()
conjunto2 = set()
interseccion = set()
union = set()
diferenciaSimetrica = set()

#FUNCIÓN DE COMPROBACIÓN DE LOS DATOS INTRODUCIDOS Y AÑADIDOS A LOS CONJUNTOS
def comprobar():
    while True:
        entrada = input()
        if re.match(patron, entrada):
            if (entrada == "x" or entrada == "X"):
                print("Se cierra el conjunto")
                print("Conjunto auxiliar cerrado:\t", conjuntoAux)
                print("-----------------------------------------------------------------------------")
                break
            else:
                conjuntoAux.add(entrada)
        else:
            print("** EL VALOR INTRODUCIDO NO ES VÁLIDO **")
            print("** Por favor introduzca un número entero o 'x' para cerrar el conjunto **")
            continue

#PETICIÓN DE NÚMEROS PARA EL CONJUNTO 1
print("Introduce los números enteros para formar el conjunto 1 ('x' para finalizar)")
comprobar()
conjunto1 = conjuntoAux.copy()
conjuntoAux.clear()

#PETICIÓN DE NÚMEROS PARA EL CONJUNTO 2
print("Introduce los números enteros para formar el conjunto 2 ('x' para finalizar)")
comprobar()
conjunto2 = conjuntoAux.copy()
conjuntoAux.clear()

#SALIDA DE AMBOS CONJUNTOS POR PANTALLA
print("Conjunto 1:\t", conjunto1)
print("-----------------------------------------------------------------------------")
print("Conjunto 2:\t", conjunto2)
print("-----------------------------------------------------------------------------")

#INTERSECCIÓN DE AMBOS CONJUNTOS
interseccion = conjunto1.intersection(conjunto2)
print("Intersección de ambos conjuntos:\t", interseccion)
print("-----------------------------------------------------------------------------")

#UNIÓN DE AMBOS CONJUNTOS
union = conjunto1.union(conjunto2)
print("Unión de ambos conjuntos:\t", union)
print("-----------------------------------------------------------------------------")

#DIFERENCIA SIMÉTRICA DE AMBOS CONJUNTOS
diferenciaSimetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica de ambos conjuntos:\t", diferenciaSimetrica)
print("-----------------------------------------------------------------------------")
