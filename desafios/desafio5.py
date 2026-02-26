# Definição de função

# def soma(a, b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(f"A soma A + B = {s}")

# Programa principal
# soma(4, 5)


## Função de Desacopamento (*)
##     Definição de função

# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f"Somando os valores {valores} temos {s}")


# #     Programa principal

# soma(5, 2)
# soma(2, 9, 4)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 4, 7, 8, 0]
dobra(valores)
print(valores)
