"""""Crea una función llamada `eliminarDuplicados` que reciba un array de números enteros.

La función debe devolver un nuevo array que contenga únicamente los números diferentes,
manteniendo el orden de su primera aparición.
"""
numeros=[11, 2, 2, 3, 24, 4, 5,1, 12, 3, 4, 5]
def eliminarDuplicados(array):
    nuevoArray=[]
    for i in array:
        if i not in nuevoArray:
            nuevoArray.append(i)
    return nuevoArray

print(eliminarDuplicados(numeros))

