# Repetições em Tuplas

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("-" * 40)

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("-" * 40)

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("-" * 40)

print("Comi pra caramba!")
