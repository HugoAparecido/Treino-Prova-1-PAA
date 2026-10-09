palavra = input("Digite um palíndromo: ")

verificar_palindromo = lambda p: len(p) <= 1 or (p[0] == p[-1] and verificar_palindromo)

ehPalindroma = verificar_palindromo(palavra)

exibir = "É palíndroma" if ehPalindroma else "Não é palíndroma"

print(exibir)