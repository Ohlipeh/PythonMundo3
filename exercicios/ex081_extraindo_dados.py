# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

valores = []

while True:

    valores.append(int(input("Digite um valor: ")))
    resposta = input("Deseja continuar? [S/N] ").strip().upper()
    if resposta in "N":
        break

print("-=" * 20)
print(f"Você digitou os valores {len(valores)} vezes.")
print(f"Os valores em ordem descrescente são {sorted(valores, reverse=True)}.")

if 5 in valores:
    print("O valor 5 está presente na lista.")
else:
    print("O valor 5 não está presente na lista.")
