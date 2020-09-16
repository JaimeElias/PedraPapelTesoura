import getpass

print("\nEscolha 1 para pedra, 2 para papel e 3 para tesoura.")

nick1 = input("\nJogador 1 informe seu nick:")
nick2 = input("\nJogador 2 informe seu nick:")

Jogada1 =  getpass.getpass("\n" + nick1 + " faça a sua jogada:")
Jogada2 =  getpass.getpass("\n" + nick2 + " faça a sua jogada:")

def definirJogada(jogada):
    if jogada == "1":
        return "pedra"
    elif jogada == "2":
        return "Papel"
    elif jogada == "3":
        return "Tesoura" 

if (Jogada1 == "2" and Jogada2 == "1") or (Jogada1 == "1" and Jogada2 == "3") or (Jogada1 == "3" and Jogada2 == "2"):
    print("\n Parabens,",nick1,"ganhou colocando",definirJogada(Jogada1))
   
elif (Jogada2 == "2" and Jogada1 == "1") or (Jogada2 == "1" and Jogada1 == "3") or (Jogada2 == "3" and Jogada1 == "2"):
    print("\n Parabens,",nick2,"ganhou colocando",definirJogada(Jogada2))

elif (Jogada1 == "1" and Jogada2 == "1") or (Jogada1 == "3" and Jogada2 == "3") or (Jogada1 == "2" and Jogada2 == "2"):
    print("\n Houve um empate,",nick1,"e",nick2, "colocaram",definirJogada(Jogada2))

else:
    print("\nVoce inseriu um valor invalido")
