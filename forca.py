import random

def jogar():
    apresentacao()
    palavra_secreta = importapalavra()
    letras_acertou = inicializaletras(palavra_secreta)
    print(letras_acertou)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 8


    while(not enforcou and not acertou):
        chute = pedechute()

        if(chute in palavra_secreta):
            marca_chute(chute, letras_acertou, palavra_secreta, tentativas)
        else:
            print("Errou! voce possui {} tentativas".format(tentativas))
            desenha_forca(erros)
            erros += 1
            tentativas = tentativas - 1

        enforcou = erros == 8
        acertou = "_" not in letras_acertou
        print("Letras acertadas...", letras_acertou)

    fimdejogo(acertou, palavra_secreta)

def apresentacao():
    print("______________________________________")
    print("Este é o JOGO de Forca em python")
    print("--------------------------------------")
    print("Feito por Fabrício")

def importapalavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializaletras(palavra):
    return ["_" for letra in palavra]

def pedechute():
    chute = input("Qual Letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, letras_acertou, palavra_secreta, tentativas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("encontrei a letra {} na posicao {} voce possui {} tentativas ".format(chute.upper(), index,
                                                                                         tentativas))
            letras_acertou[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def fimdejogo(acertou, palavra_secreta):
    if (acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    print("Fim de Jogo")
    fimdejogo = input("Digite qualquer tecla para sair....")

if(__name__ == "__main__"):
    jogar()