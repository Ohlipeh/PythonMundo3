# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


# Definição de função
def ficha(jog="desconhecido", gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


# Programa principal
n = input("Nome do Jogador: ")
g = input("Quantos Gols: ")
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)
