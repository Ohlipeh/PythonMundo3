# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


# Definição de função
def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


# Programa  Principal
escreva("My World")
escreva("Praticando Python todos os DIAS!!")
escreva("Assinado: Andre F. I. L.")
