import copy


def criarJogo():
    jogo = []
    jogo.append(["2", "*", "4"])
    jogo.append(["3", "1", "6"])
    jogo.append(["7", "5", "8"])
    return jogo


def criarJogo2():
    jogo = []
    jogo.append(["1", "*", "2"])
    jogo.append(["4", "5", "3"])
    jogo.append(["7", "8", "6"])
    return jogo


def buscaInicio(jogo):
    for j, row in enumerate(jogo):
        for i, col in enumerate(row):
            if col == "*":
                startI = i
                startJ = j

    return startI, startJ


def printJogo(jogo):
    i, j = buscaInicio(jogo)

    print("—", "—", "—")
    for j, row in enumerate(jogo):
        for i, col in enumerate(row):
            print(col + " ", end="")
        print()
    print("—", "—", "—")


def printJogoPassoAPasso(jogo, path):
    i, j = buscaInicio(jogo)

    jogoAtual = copy.deepcopy(jogo)
    for step in path:
        printJogo(jogoAtual)
        print(" ||")
        print("\\  /")
        print(" \\/")
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

    printJogo(jogoAtual)


def movimentoValido(jogo, passo):
    if len(passo) > 1:
        ultimosPassos = passo[-2:]
        if (ultimosPassos[0] == 'L' and ultimosPassos[1] == 'R') or (
                ultimosPassos[0] == 'R' and ultimosPassos[1] == 'L') or (
                ultimosPassos[0] == 'U' and ultimosPassos[1] == 'D') or (
                ultimosPassos[0] == 'D' and ultimosPassos[1] == 'U'):
            return False

    i, j = buscaInicio(jogo)

    for step in passo:
        if step == "L":
            i = i - 1
        if step == "R":
            i = i + 1
        if step == "U":
            j = j - 1
        if step == "D":
            j = j + 1
    if not (0 <= i < (len(jogo[0])) and (0 <= j < (len(jogo)))):
        return False
    return True


def fimDeJogo(jogo, path):
    if path == '':
        return False

    i, j = buscaInicio(jogo)

    jogoAtual = copy.deepcopy(jogo)
    for step in path:
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
    print(len(path))
    printJogo(jogoAtual)
    if jogoAtual[0][0] == "1":
        if jogoAtual[0][1] == "2":
            if jogoAtual[0][2] == "3":
                if jogoAtual[1][0] == "4":
                    if jogoAtual[1][1] == "5":
                        if jogoAtual[1][2] == "6":
                            if jogoAtual[2][0] == "7":
                                if jogoAtual[2][1] == "8":
                                    if jogoAtual[2][2] == "*":
                                        print("******FIM DE JOGO*******")
                                        print(path)
                                        print(len(path))
                                        print("PASSO A PASSO")
                                        printJogoPassoAPasso(jogo, path)
                                        return True

    return False
