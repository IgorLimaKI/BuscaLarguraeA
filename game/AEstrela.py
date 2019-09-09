import queue
from math import fabs
from game.Jogo import *


def funcaoHeuristica(passo, jogo):
    i, j = buscaInicio(jogo)

    jogoAtual = copy.deepcopy(jogo)
    for step in passo:
        if step == "L":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j][i - 1]
            jogoAtual[j][i - 1] = aux
            i = i - 1
        if step == "R":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j][i + 1]
            jogoAtual[j][i + 1] = aux
            i = i + 1
        if step == "U":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j - 1][i]
            jogoAtual[j - 1][i] = aux
            j = j - 1
        if step == "D":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j + 1][i]
            jogoAtual[j + 1][i] = aux
            j = j + 1

    notaTabuleiro = 0
    for j, row in enumerate(jogoAtual):
        for i, col in enumerate(row):
            if col == '1':
                notaTabuleiro = notaTabuleiro + fabs((i - 0) + (j - 0)) * 10
            if col == '2':
                notaTabuleiro = notaTabuleiro + fabs((i - 0) + (j - 1)) * 9
            if col == '3':
                notaTabuleiro = notaTabuleiro + fabs((i - 0) + (j - 2)) * 8
            if col == '4':
                notaTabuleiro = notaTabuleiro + fabs((i - 1) + (j - 0)) * 7
            if col == '5':
                notaTabuleiro = notaTabuleiro + fabs((i - 1) + (j - 1)) * 6
            if col == '6':
                notaTabuleiro = notaTabuleiro + fabs((i - 1) + (j - 2)) * 5
            if col == '7':
                notaTabuleiro = notaTabuleiro + fabs((i - 2) + (j - 0)) * 4
            if col == '8':
                notaTabuleiro = notaTabuleiro + fabs((i - 2) + (j - 1)) * 3
            if col == '*':
                notaTabuleiro = notaTabuleiro + fabs((i - 2) + (j - 2))
    return notaTabuleiro


def funcaoHeuristica2(passo, jogo):
    i, j = buscaInicio(jogo)

    jogoAtual = copy.deepcopy(jogo)
    for step in passo:
        if step == "L":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j][i - 1]
            jogoAtual[j][i - 1] = aux
            i = i - 1
        if step == "R":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j][i + 1]
            jogoAtual[j][i + 1] = aux
            i = i + 1
        if step == "U":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j - 1][i]
            jogoAtual[j - 1][i] = aux
            j = j - 1
        if step == "D":
            aux = jogoAtual[j][i]
            jogoAtual[j][i] = jogoAtual[j + 1][i]
            jogoAtual[j + 1][i] = aux
            j = j + 1

    notaTabuleiro = 0
    for j, row in enumerate(jogoAtual):
        for i, col in enumerate(row):
            if col == '1' and j != 0 or i != 0:
                notaTabuleiro = notaTabuleiro + 1
            if col == '2' and j != 0 or i != 1:
                notaTabuleiro = notaTabuleiro + 1
            if col == '3' and j != 0 or i != 2:
                notaTabuleiro = notaTabuleiro + 1
            if col == '4' and j != 1 or i != 0:
                notaTabuleiro = notaTabuleiro + 1
            if col == '5' and j != 1 or i != 1:
                notaTabuleiro = notaTabuleiro + 1
            if col == '6' and j != 1 or i != 2:
                notaTabuleiro = notaTabuleiro + 1
            if col == '7' and j != 2 or i != 0:
                notaTabuleiro = notaTabuleiro + 1
            if col == '8' and j != 2 or i != 1:
                notaTabuleiro = notaTabuleiro + 1
            if col == '*' and j != 2 or i != 2:
                notaTabuleiro = notaTabuleiro + 1


def buscaAEstrela(jogo):
    nums = queue.Queue()
    nums.put("")
    add = ""
    numNós = 0
    while not fimDeJogo(jogo, add):
        print("Numero de nós verificados: ", numNós)
        print()
        add = nums.get()
        print(add)
        heuristica = []
        for k in ["L", "R", "U", "D"]:
            passo = add + k
            if movimentoValido(jogo, passo):
                numNós = numNós + 1
                heuristica.append((funcaoHeuristica2(passo, jogo), passo))
        heuristica.sort()
        for heu in heuristica:
            if heu[0] == heuristica[0][0]:
                nums.put(heu[1])
