# teste = list() # ou teste = []  # outra forma de criar uma lista
# teste.append("André") # append() é usado para adicionar elementos a uma lista
# teste.append(32) # adiciona o número 32 à lista teste
# galera = list() # ou galera = []  # outra forma de criar uma lista
# galera.append(teste[:])  # [:] é usado para criar uma cópia da lista
# teste[0] = "Maria" # altera o primeiro elemento da lista teste para "Maria"
# teste[1] = 22 # altera o segundo elemento da lista teste para 22
# galera.append(teste[:]) # adiciona a cópia da lista teste à lista galera
# print(galera) # imprime a lista galera, que contém duas sublistas: [['André', 32], ['Maria', 22]]

galera = list()  # ou galera = []  # outra forma de criar uma lista

dado = list()  # ou dado = []  # outra forma de criar uma lista

total_maiores = total_menores = (
    0  # inicializa as variáveis total_maiores e total_menores com o valor 0
)

for c in range(0, 3):  # loop que se repete 3 vezes

    dado.append(
        str(input("Nome: "))
    )  # adiciona o nome digitado pelo usuário à lista dado

    dado.append(
        int(input("Idade: "))
    )  # adiciona a idade digitada pelo usuário à lista dado

    galera.append(dado[:])  # adiciona uma cópia da lista dado à lista galera

    dado.clear()  # limpa a lista dado para a próxima iteração do loop

for p in galera:  # loop que percorre cada elemento da lista galera

    if (
        p[1] >= 21
    ):  # verifica se a idade (segundo elemento da sublista) é maior ou igual a 21

        print(
            f"{p[0]} é maior de idade."
        )  # imprime o nome (primeiro elemento da sublista) e a mensagem "é maior de idade."

        total_maiores += 1  # incrementa o contador total_maiores

    else:  # caso contrário, se a idade for menor que 21

        print(
            f"{p[0]} é menor de idade."
        )  # imprime o nome e a mensagem "é menor de idade."

        total_menores += 1  # incrementa o contador total_menores

print(
    f"Temos {total_maiores} maiores e {total_menores} menores de idade."
)  # imprime o total de maiores e menores de idade
