from random import sample
from time import sleep

print("-" * 30)
print("MEGA SENA".center(30))
print("-" * 30)

quant = int(input("Quantos jogos você quer que eu sorteie? "))
print("-" * 30)

print("-=" * 3, f"SORTEANDO {quant} JOGOS", "-=" * 3)
for i in range(quant):
    numeros = sample(range(1, 61), 6)
    print(f"Jogo {i + 1}: {sorted(numeros)}")
    sleep(1)
print("-=" * 4, "BOA SORTE!", "-=" * 4)
