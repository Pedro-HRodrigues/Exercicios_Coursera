#Reboot jogo do nim

def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > n or jogada > m or jogada <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def computador_escolhe_jogada (n,m): 
    retirada = n % (m + 1) 
    if n <= m: 
        retirada = n 
        return retirada 
    else: 
        if retirada < m and retirada > 0 : 
            return retirada 
        else:
            retirada = m
            return retirada

def partida():
    n = int(input("Quantas peças ? "))
    m = int(input("Limite de peças por jogada ? "))
    if n % (m + 1) == 0:
        print("Voce começa!")
        
        joga = True
        
        while joga :
            
            jogada = usuario_escolhe_jogada(n,m)

            if jogada == 1 :
                print("Você tirou uma peça ")
            else:
                print("Você tirou", jogada, "Peças.")

            n = n - jogada
            if n <= 0 :
                joga = False

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam, ", n," peças no tabuleiro")

            retirada = computador_escolhe_jogada(n,m)

            if retirada == 1 :
                print("Computador tirou uma peça")
            if n > 1 :
                print("Computador tirou,", retirada, " peças.")

            n = n - retirada
            if n <= 0 :
                joga = False

            if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro")
            if n > 1 :
                    print("Agora restam, ", n," peças no tabuleiro")
                

            
            
    else:
        print("Computador começa")

        joga = True
        
        while joga :
            
            retirada = computador_escolhe_jogada(n,m)

            if retirada == 1 :
                print("Computador tirou uma peça")
            else:
                print("Computador tirou,", retirada, " peças.")

            n = n - retirada
            if n == 0 :
                joga = False

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro")
            if n > 1:
                print("Agora restam, ", n," peças no tabuleiro")


                jogada = usuario_escolhe_jogada(n,m)

                if jogada == 1 :
                    print("Você tirou uma peça ")
                else:
                    print("Você tirou", jogada, "Peças.")

                n = n - jogada
                if n <= 0 :
                    joga = False

                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro")
                if n > 1 :
                    print("Agora restam, ", n," peças no tabuleiro")


    if joga == False:
        print("Fim do jogo! O computador ganhou!")


def inicio():
    print ("Bem vindo ao jogo do NIM! Escolha:") 
    print ("1 - para jogar uma partida isolada") 
    x = int (input ("2 - para jogar um campeonato ")) 

    if x == 2: 

        print ("Voce escolheu um capeonato!") 
        print ("**** Rodada 1 ****") 

        partida() 

        print ("**** Rodada 2 ****") 

        partida() 

        print ("**** Rodada 3 ****") 

        partida() 

        print ("**** Final do campeonato! ****") 
        print (" Placar: Você 0 X 3 Computador") 

    if x == 1: 

        print ("Voce escolheu uma partida isolada!") 

        partida()

inicio()




                    
