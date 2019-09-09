import queue
from game.Jogo import *


def buscaLargura(jogo):
    nums = queue.Queue()
    nums.put("")
    add = ""
    numNós = 0
    while not fimDeJogo(jogo, add):
        print("Numero de nós verificados: ", numNós)
        print()
        numNós = numNós + 1
        add = nums.get()
        print(add)
        for k in ["L", "R", "U", "D"]:
            passo = add + k
            if movimentoValido(jogo, passo):
                nums.put(passo)