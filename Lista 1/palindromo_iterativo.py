palavra = input("Digite um palíndromo: ")

ehPalindroma = True
contador = 0
tamanho = len(palavra)

while ehPalindroma and contador <= tamanho // 2:
    if (palavra[contador] != palavra[tamanho - contador - 1]):
        ehPalindroma = False

    print(palavra[contador])
    print(palavra[tamanho - contador - 1])
    print()
    
    contador += 1

exibir = "É palíndroma" if ehPalindroma else "Não é palíndroma"

print(exibir)