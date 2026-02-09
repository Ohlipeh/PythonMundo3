# Crie um programa que leia 5 valores e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor na posição {cont}: ")))
print(f"Você digitou os valores {valores}")

print(f"O maior valor digitado foi {max(valores)} e ele está na posição ", end="")
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(pos, end=" ")

print(f"\nO menor valor digitado foi {min(valores)} e ele está na posição ", end="")
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(pos, end=" ")
