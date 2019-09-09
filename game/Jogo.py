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


def movimentoValido(jogo, passo):
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
                                        printJogo(jogo)
                                        printJogo(jogoAtual)
                                        return True

    return False
