# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule a idade e em quantos anos a pessoa vai se aposentar.

from datetime import date

# 1. Guarda o ano atual em uma variável para não chamar a função várias vezes
ano_atual = date.today().year

pessoa = {
    # 2. input() já retorna texto, então o str() aqui é desnecessário
    "Nome": input("Nome: "),
    "Ano de nascimento": int(input("Ano de nascimento: ")),
    "Carteira de trabalho": int(input("Carteira de trabalho (0 não tem): ")),
}

# 3. Calcula a idade FORA do if/else, pois todo mundo tem idade (evita repetição)
pessoa["Idade"] = ano_atual - pessoa["Ano de nascimento"]

if pessoa["Carteira de trabalho"] != 0:
    pessoa["Ano de contratação"] = int(input("Ano de contratação: "))
    pessoa["Salário"] = float(input("Salário: "))

    # 4. Matemática simplificada para a idade de aposentadoria
    ano_aposentadoria = pessoa["Ano de contratação"] + 35
    pessoa["Aposentadoria"] = ano_aposentadoria - pessoa["Ano de nascimento"]

print("-=" * 15)
for k, v in pessoa.items():
    print(f"  - {k} tem o valor {v}.")
