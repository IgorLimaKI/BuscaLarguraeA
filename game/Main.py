from game.BuscaLargura import *
from game.AEstrela import *


dificuldade = 0
resposta = 0
while dificuldade != '1' and dificuldade != '2':
    print('Escolha o tipo de jogo:')
    print('1 - Fácil')
    print('2 - Difícil')
    dificuldade = input()
    print()

while resposta != '1' and resposta != '2':
    print('Escolha o método de resolução:')
    print('1 - Busca em Largura')
    print('2 - A*')
    resposta = input()
    print()

if dificuldade == '1':
    newJogo = criarJogo2()
else:
    newJogo = criarJogo()

if resposta == '1':
    buscaLargura(newJogo)
else:
    buscaAEstrela(newJogo)

