def EhPalindromo(palavra):
    if(len(palavra) <= 1):
        return True

    if palavra[0] != palavra[-1]:
        return False

    return EhPalindromo(palavra[1:-1])
    

palavra = input("Digite um palíndromo: ")

ehPalindroma = EhPalindromo(palavra)

exibir = "É palíndroma" if ehPalindroma else "Não é palíndroma"

print(exibir)