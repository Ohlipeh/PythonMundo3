# Exercício Python 082: Crie um programa onde o usuário digite vários números e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
pares = []
impares = []

while True:

    numeros.append(int(input("Digite um número: ")))
    resposta = input("Deseja continuar? [S/N] ").strip().upper()
    if resposta in "N":
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print("-=" * 20)
print(f"Os números digitados foram {sorted(numeros)}.")
print(f"Os números pares digitados foram {sorted(pares)}.")
print(f"Os números ímpares digitados foram {sorted(impares)}.")
