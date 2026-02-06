# num = [2, 5, 8, 10, 12]

# num[1] = 6  # Modifica o segundo elemento da lista para 6

# num.append(15)  # Adiciona o número 15 ao final da lista

# num.insert(2, 7)  # Insere o número 7 na posição de índice 2 (entre 6 e 8)

# num.sort()  # Ordena a lista em ordem crescente

# num.reverse()  # Inverte a ordem da lista para que fique em ordem decrescente
# num.pop(0)  # Remove o primeiro elemento da lista

# if 1 in num:
#     num.remove(1)  # Remove o número 12 da lista, se estiver presente
# else:
#     print(
#         "O número 1 não está na lista."
#     )  # Imprime uma mensagem caso o número 12 não esteja na lista

# num.remove(10)  # Remove o número 10 da lista

# print(num)  # Imprime a lista modificada e ordenada

# print(num[1])  # Imprime o segundo elemento da lista (agora é 6)

# print(num[2])  # Imprime o terceiro elemento da lista (agora é 7)

# print(num[-1])  # Imprime o último elemento da lista (agora é 15)

# print(f"Quantidade de elementos na lista: {len(num)}")  # Qnt de elementos list

valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
for chave, valor in enumerate(valores):
    print(f"Na posição {chave} encontrei o valor {valor}!")
print("Cheguei ao final da lista.")
