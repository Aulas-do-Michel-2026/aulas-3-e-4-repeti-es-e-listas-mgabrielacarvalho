"""
#### Exercício 1

Receba um número e calcule a soma de todos os números de 1 até ele.

Exemplo:

Digite um número:
5

A soma de 1 até 5 é 15.
--------
Digite um número:
3

A soma de 1 até 3 é 6.

Dica: Use o comando "for" junto com "range()" para percorrer os números,
e uma variável para ir acumulando a soma.
"""



numero = int(input("Digite um numero: "))

soma = 0

for i in range(1, numero + 1): #na função range, o número de término não é incluido. O +1 faz com que o número seja incluido
    soma = soma + i

print(soma)
