# # Dicionarios
# # Dicionarios são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, o que significa que você pode alterar seus valores após a criação.

# pessoas = {"nome": "João", "idade": 30, "sexo": "M"}
# # print(f"O nome da pessoa é {pessoas['nome']} e ele tem {pessoas['idade']} anos.")
# # del pessoas["sexo"]  # Remove a chave "sexo" do dicionário
# pessoas["nome"] = "Maria"  # Altera o valor da chave "nome" para "Maria"
# pessoas["altura"] = 1.75  # Adiciona uma nova chave "altura" com o valor 1.75
# for k, v in pessoas.items(): # Itera sobre os pares chave-valor do dicionário
#     print(f"{k}: {v}") # Imprime a chave e o valor de cada item do dicionário

brasil = []
estado1 = {}
for c in range(0, 3):
    estado1["uf"] = str(input("Unidade Federativa: "))
    estado1["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado1.copy()) # Adiciona uma cópia do dicionário estado1 à lista brasil
for e in brasil: # Itera sobre os dicionários na lista brasil
    for k, v in e.items(): # Itera sobre os pares chave-valor de cada dicionário
        print(f"{k}: {v}") # Imprime a chave e o valor de cada item do dicionário
