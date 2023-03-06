import random
def jogar():
    print("______________________________________")
    print("Este é o JOGO de Avivinhação em python")
    print("--------------------------------------")
    print("Feito por Fabrício")

    rodada = 1
    tentativas = 0
    numero_secreto = int(random.randrange(1, 101))
    pontos = 1000

    print("Insira a dificuldade...")
    print("[1] Modo de Teste [2] Fácil [3] Médio [4] Difícil")
    tent = input("Insira o total de Tentativas....")
    tent = int(tent)

    if (tent == 1):
        tentativas = 10
        print("__________________________________________________")
        print("____________________DEBUGMODE_____________________")
        print("____________Numero secreto___________", numero_secreto, "_________")
    elif (tent == 2):
        tentativas = 25
    elif (tent == 3):
        tentativas = 13
    elif (tent == 4):
        tentativas = 7
    else:
        tentativas = 1000

    for rodada in range(1, tentativas + 1):
        print("__________________________________________________")
        print("tentativa....{} de {}".format(rodada, tentativas))
        chute_str = input("Digite o seu número....")
        chute = int(chute_str)
        acertou     = chute == numero_secreto
        numeromaior = chute > numero_secreto
        numeromenor = chute < numero_secreto

        print("Voce digitou....", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        if (acertou):
            print("Voce acertou e fez {}".format(pontos))
            break
        else:
            if (numeromaior):
                print("Ih ala meno, errou dms")
                print("O número e menor jubileu")
            elif (numeromenor):
                print("Ih ala meno, errou dms")
                print("O número e maior jubileu")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos
        print("________________________________________")

    print("Fim de Jogo")

if (__name__ == "__main__"):
    jogar()