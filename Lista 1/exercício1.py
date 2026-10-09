def busca(vetor, elemento_buscado):
    if len(vetor) == 1:
        return elemento_buscado == vetor[0]

    if len(vetor) == 0:
        return False

    print(vetor)
    print(elemento_buscado)

    meio = len(vetor) // 2

    return busca(vetor[0 : meio], elemento_buscado) or busca(
        vetor[meio :], elemento_buscado
    )


vetor = [1,2,3,4,5,6]

tem = busca(vetor, 1)

print(tem)