from ex0115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        with open(nome, "rt", encoding="utf-8") as a:
            cabecalho("PESSOAS CADASTRADAS")
            print(a.read())
    except:
        print("ERRO ao ler o arquivo")
