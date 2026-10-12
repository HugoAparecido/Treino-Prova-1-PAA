**Universidade Federal de São Carlos - UFSCar**

**Departamento de Computação - DC** **Projeto e Análise de Algoritmos** **Prof. Dr. Alan Demétrius Baria Valejo** **Lista 1 - [[Recursão]] e [[Análise Assintótica]]**1

---

## **Exercício 1 ([[Algoritmo]]s: Teoria e prática (adaptado)):** 
Considere o problema de buscar um elemento $v$ em um [[vetor]] $A$. Escreva um **[[código recursivo]]** que retorne o [[índice]] do elemento $v$ caso ele pertença ao [[vetor]], ou `NULL` caso contrário. Utilizando a **[[notação Big-O]]**, calcule a [[complexidade]] do seu [[algoritmo]].
## **Exercício 2 (Rosetta Code (Adaptado)):** 
- Por definição, uma frase (ou número) é **palíndromo** se é igual lida de trás para frente, como por exemplo: “ovo”, “arara”, “234432”, etc2. Escreva um **[[código iterativo]]** e um **[[Código Recursivo]]** para verificar se dada palavra é palíndromo. É possível escrever esse código em uma **única linha usando o Python**?
## **Exercício 3:** 
- Considere o seguinte problema: **Ordenar** $n$ **elementos de um [[vetor]]** $A$, localizando primeiro o menor elemento de $A$, e permutando esse elemento com o elemento contido em $A$. Em seguida, determinar o segundo menor elemento de $A$ e permutá-lo com o elemento $A$, e assim por diante até o elemento $n - 1$. Escreva o **código desse [[algoritmo]]** e indique qual a **[[complexidade]]**.
## **Exercício 4:** 
- Escreva um [[algoritmo]] para determinar se uma **string com caracteres ASCII possui valores duplicados**. Utilizando a **[[notação Big-O]]**, qual a [[complexidade]] do seu [[algoritmo]]?
## **Exercício 5:** 
- Considere o script em Python a seguir, em que a [[função]] `fn1()` possui [[complexidade]] $O(1)$, a [[função]] `fn2()` possui [[complexidade]] $O(n)$ e a [[função]] `fn3()` possui [[complexidade]] $O(n^2)$. Qual é a **[[complexidade]] do [[algoritmo]]**?

````
for i in range(n):
    fn1(i)
    for j in range(n):
        fn2(j)
        for k in range(n):
            fn3(k)
``` [6]

````

## **Exercício 6 (Google Interview Exercises (adaptado)):** 
Usando seus conhecimentos no curso até o momento, escreva um [[algoritmo]] que dado um [[array]] $A$ e um valor $s$, retorna `True` se existe pelo menos um **par de inteiros** $a_1, a_2 \in A$ **que somados resultam em** $s$, e `False` caso contrário6. Qual a **[[complexidade]] do [[algoritmo]]**? _Exemplos:_
    - $A =3 + 5 + 7, s = 6 \rightarrow$ `False` (Não existe um par com soma 6)
    - $A =$3+5+7+8, s = 5 \rightarrow$ `True` (Existe pelo menos um par com soma 5)
## **Exercício 7 (Elements of Programming Interviews (adaptado)):** 
Suponha dois retângulos desenhados no plano paralelos aos eixos x e y. Escreva um código que retorna `True` se os dois retângulos são **sobrepostos**, e `False` caso contrário. Qual a **[[complexidade]] do [[algoritmo]]**? _Exemplos:_
    - Entrada: $0 \le x \le 2, 0 \le y \le 2 \mid 2 \le x \le 4, 2 \le y \le 4 \rightarrow$ Saída: `True`
    - Entrada: $0 \le x \le 1, 0 \le y \le 1 \mid 2 \le x \le 3, 2 \le y \le 5 \rightarrow$ Saída: `False`
## **Exercício 8:** 
Usando **[[recursão]]**, escreva uma [[função]] que determine se um **número é ou não primo**. Qual a **[[complexidade]] do algoritmo**?