# Exercício 073: Times de Futebol em Tupla
# Crie uma tupla com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, # na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição está o time .....

times = (
    "Palmeiras",
    "Flamengo",
    "Atlético-MG",
    "Corinthians",
    "Fluminense",
    "São Paulo",
    "Santos",
    "Grêmio",
    "Vasco da Gama",
    "Botafogo",
    "Internacional",
    "Cruzeiro",
    "Bahia",
    "Athletico-PR",
    "Ceará SC",
    "Fortaleza",
    "Goiás",
    "Coritiba",
    "Atlético-GO",
    "Bragantino",
)

print("-" * 40)
print("Lista de times do Brasileirão Série A:")
for time in times:
    print(time)

print("-" * 40)
print("\nOs 5 primeiros times são: ")
for time in times[:5]:
    print(time)

print("-" * 40)
print("\nOs 4 últimos times são: ")
for time in times[-4:]:
    print(time)

print("-" * 40)
print("\nTimes em ordem alfabética:")
for time in sorted(times):
    print(time)

print("-" * 40)
posicao_flamengo = times.index("Flamengo") + 1
print(f"\nO Flamengo está na {posicao_flamengo}ª posição.")
