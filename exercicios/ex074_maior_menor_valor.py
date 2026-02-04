# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
    randint(1, 100),
)
print("Números sorteados:", end=" ")
for numero in num:
    print(numero, end=" ")
print(f"\nO maior valor sorteado foi {max(num)}")
print(f"O menor valor sorteado foi {min(num)}")
