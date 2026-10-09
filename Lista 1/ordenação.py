def Ordenar(array: []):
    arrayOrdenado = []

    for item in range(len(array)):
        menorItem = array[0]
        for item in array:
            menorItem = min(menorItem, item)
        arrayOrdenado.append(menorItem)
        array.remove(menorItem)

    return arrayOrdenado

array = [42, 17, 8, 99, 23, 4, 15, 88, 3, 11]

array = Ordenar(array)

print(array)