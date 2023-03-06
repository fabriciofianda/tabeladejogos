import forca
import adivinhacao
print("______________________________________")
print("Escolha o seu jogo")
print("--------------------------------------")
print("Feito por Fabrício")

print("Jogo da Forca [1] Jogo da Adivinhação [2]")
jogo = int(input("Qual o Jogo? "))
def escolhe_jogo():
    if(jogo == 1):
        print("Jogando adivinhacao")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()