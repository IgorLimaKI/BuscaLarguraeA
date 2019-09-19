from game.BuscaLargura import *
from game.AEstrela import *

tipoDeJogo = 0
resposta = 0
heuristica = 0
while tipoDeJogo != '1' and tipoDeJogo != '2':
    print('Escolha o tipo de jogo:')
    print('1 - Exemplo')
    print('2 - Escrever')
    tipoDeJogo = input()
    print()
if tipoDeJogo == '1':
    newJogo = criarJogo()
else:
    newJogo = []
    print('Não será checado se o jogo é válido!')
    print('Escreva a primeira linha do jogo(exemplo: *, 2, 3):')
    newJogo.append(input().split(','))
    print('Escreva a segunda linha do jogo(exemplo: *, 2, 3):')
    newJogo.append(input().split(','))
    print('Escreva a terceira linha do jogo(exemplo: *, 2, 3):')
    newJogo.append(input().split(','))

while resposta != '1' and resposta != '2':
    print('Escolha o método de resolução:')
    print('1 - Busca em Largura')
    print('2 - A*')
    resposta = input()
    print()

if resposta == '1':
    buscaLargura(newJogo)
else:
    while heuristica != '1' and heuristica != '2':
        print('Escolha a Heurística:')
        print('1 - Nº de posições erradas')
        print('2 - Distancia Manhattan')
        heuristica = input()
        print()
    if heuristica == '1':
        buscaAEstrela(newJogo, 1)
    else:
        buscaAEstrela(newJogo, 2)
