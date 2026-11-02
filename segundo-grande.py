"""Enunciado
Desarrolla una función en Python llamada segundo_mayor(numeros) que reciba una lista de números
enteros y devuelva el segundo número más grande, sin contar valores repetidos.
Este ejercicio es representativo de los problemas de lógica y algoritmos que pueden aparecer en
 entrevistas técnicas para desarrolladores junior.
Requisitos
1. La función debe recibir una lista de números enteros.
2. Debe devolver el segundo número más grande distinto.
3. Si la lista contiene menos de dos valores diferentes, debe devolver None.
4. Debe funcionar con números positivos, negativos y repetidos.
5. No está permitido utilizar sort(), sorted() ni set().
"""
n = [12, 5, 8, 21, 17, 17, 10, 6, 122, 9]

def segundo_mayor(numeros):
    numeroG = 0
    numeroP = 0
    for i in numeros:
        if i > numeroG:
            numeroP = numeroG
            numeroG = i
        elif i > numeroP and i != numeroG:
            numeroP = i
    return numeroP

print(segundo_mayor(n))