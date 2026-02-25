#  Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = input("Nome: ")

    while True:
        pessoa["sexo"] = input("Sexo: [M/F] ").upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())

    while True:
        resp = input("Deseja continuar? [S/N] ").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite apenas S ou N.")
    if resp in "N":
        break

print("=-" * 30)
print(f"A) Ao total foram {len(galera)} pessoas cadastradas.")
print("=-" * 30)

media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos.")
print("=-" * 30)

print("C) As mulheres cadastradas foram ", end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"{p["nome"]} ", end="")
print()
print("=-" * 30)


print("D) Lista das pessoas que estão acima da média:")
for p in galera:
    if p["idade"] >= media:
        print("   ", end="")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("  << ENCERRANDO >>")
