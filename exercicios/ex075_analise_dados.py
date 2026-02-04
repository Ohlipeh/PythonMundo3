valor = (
    int(input("Digite um valor inteiro: ")),
    int(input("Digite outro valor inteiro: ")),
    int(input("Digite mais um valor inteiro: ")),
    int(input("Digite o último valor inteiro: ")),
)

print(f"\nVocê digitou os valores: {valor}")
print(f"O valor 9 apareceu {valor.count(9)} vezes.")
if 3 in valor:
    print(f"O valor 3 apareceu pela primeira vez na posição {valor.index(3)+1}.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
if valor[3] % 2 == 0:
    print(f"Os valores pares digitados foram: ", end="")
    for n in valor:
        if n % 2 == 0:
            print(n, end=" ")
else:
    print("Nenhum valor par foi digitado.")
