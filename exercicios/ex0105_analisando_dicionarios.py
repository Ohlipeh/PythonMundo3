# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidades de notas, A maior nota, A menor nota, A média da turma e A situação(opcional).


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situacao"] = "BOA"
        elif r["media"] >= 5:
            r["situacao"] = "RAZOAVEL"
        else:
            r["situacao"] = "RUIM"
    return r


# Programa Principal
resp = notas(5.5, 7.0, 2.6, sit=True)
print(resp)
help(notas)
