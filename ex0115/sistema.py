from ex0115.lib.interface import *
from ex0115.lib.arquivo import *
from time import sleep

arq = "python.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ["Ver pessoas cadastrada", "Cadastrar novas pessoas", "Sair do Sistema"]
    )
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do sistem... Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(2)
