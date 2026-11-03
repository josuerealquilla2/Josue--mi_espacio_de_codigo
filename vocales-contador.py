"""""Crea una función llamada `contarVocales` que reciba una cadena
de texto y devuelva cuántas vocales contiene.

Debes contar las vocales `a`, `e`, `i`, `o`, `u`,
 tanto mayúsculas como minúsculas."""
palabra=input("diga una palabra")


def contadorVocales(palabras):
    vocales=["a","e","i","o","u"]
    contador=0
    for i in palabra.lower():
        if i in vocales:
            contador=contador+1
    print(contador)
    return contador
contadorVocales(palabra)