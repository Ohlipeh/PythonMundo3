# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    cont = maior = 0
    print("-=" * 20)
    print("Analisando os valores passados...")
    for valor in num:
        print(f"{valor} ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram analisados {cont} valores.")
    print(f"O maior valor analisado foi {maior}.")


# Programa principal
maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(99, 100, 200, 300)
maior(888, 999)
maior(1)
