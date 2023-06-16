import random
import time

pAvioesPC = True
pAvioesJogador = True
nTanquePC = True
nTanqueJogador = True
destroierPC = True
destroierJogador = True
subPC = True
subJogador = True
botePC = True
boteJogador = True

naviosPC = 5
naviosJogador = 5

tabuleiroPC = [["_", " A", " B", " C", " D", " E", " F", " G", " H", "  I", " J"],
               ["1", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
               ["2", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
               ["3", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
               ["4", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
               ["5", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]]

ocultoPC = [["_", " A", " B", " C", " D", " E", " F", " G", " H", "  I", " J"],
            ["1", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
            ["2", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
            ["3", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
            ["4", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
            ["5", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]]

tabuleiroJogador = [["_", " A", " B", " C", " D", " E", " F", " G", " H", "  I", " J"],
                    ["1", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                    ["2", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                    ["3", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                    ["4", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                    ["5", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]]

ocultoJogador = [["_", " A", " B", " C", " D", " E", " F", " G", " H", "  I", " J"],
                 ["1", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                 ["2", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                 ["3", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                 ["4", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
                 ["5", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]]

def creditos():
    print("Muito obrigado por jogar nosso jogo :D")
    time.sleep(1)
    print("Desenvolvido por:\n Armando Oliveira\n Honorato Machado\n William Botelho")

def gigaShip():
   dir = random.randint(0, 1)

   if dir == 0:
       x = random.randint(1, 6)
       y = random.randint(1, 5)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y][x+1] == "🌊" and tabuleiroPC[y][x+2] == "🌊" and tabuleiroPC[y][x+3] == "🌊" and tabuleiroPC[y][x+4] == "🌊":
           tabuleiroPC[y][x] = "🛳️"
           tabuleiroPC[y][x+1] = "🛳️"
           tabuleiroPC[y][x+2] = "🛳️"
           tabuleiroPC[y][x+3] = "🛳️"
           tabuleiroPC[y][x+4] = "🛳️"
       else:
           gigaShip()

   if dir == 1:
       x = random.randint(1, 10)
       y = 0

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y+1][x] == "🌊" and tabuleiroPC[y+2][x] == "🌊" and tabuleiroPC[y+3][x] == "🌊" and tabuleiroPC[y+4][x] == "🌊":
           tabuleiroPC[y][x] = "🛳️"
           tabuleiroPC[y+1][x] = "🛳️"
           tabuleiroPC[y+2][x] = "🛳️"
           tabuleiroPC[y+3][x] = "🛳️"
           tabuleiroPC[y+4][x] = "🛳️"
       else:
           gigaShip()

def bigShip():
   dir = random.randint(0, 1)

   if dir == 0:
       x = random.randint(1, 7)
       y = random.randint(1, 5)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y][x+1] == "🌊" and tabuleiroPC[y][x+2] == "🌊" and tabuleiroPC[y][x+3] == "🌊":
           tabuleiroPC[y][x] = "⛴️"
           tabuleiroPC[y][x+1] = "⛴️"
           tabuleiroPC[y][x+2] = "⛴️"
           tabuleiroPC[y][x+3] = "⛴️"
       else:
           bigShip()

   if dir == 1:
       x = random.randint(1, 10)
       y = random.randint(1, 2)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y+1][x] == "🌊" and tabuleiroPC[y+2][x] == "🌊" and tabuleiroPC[y+3][x] == "🌊":
           tabuleiroPC[y][x] = "⛴️"
           tabuleiroPC[y+1][x] = "⛴️"
           tabuleiroPC[y+2][x] = "⛴️"
           tabuleiroPC[y+3][x] = "⛴️"
       else:
           bigShip()

def mediumShip():
   dir = random.randint(0, 1)

   if dir == 0:
       x = random.randint(1, 8)
       y = random.randint(1, 5)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y][x+1] == "🌊" and tabuleiroPC[y][x+2] == "🌊":
           tabuleiroPC[y][x] = "🛥️"
           tabuleiroPC[y][x+1] = "🛥️"
           tabuleiroPC[y][x+2] = "🛥️"
       else:
           mediumShip()

   if dir == 1:
       x = random.randint(1, 10)
       y = random.randint(1, 3)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y+1][x] == "🌊" and tabuleiroPC[y+2][x] == "🌊":
           tabuleiroPC[y][x] = "🛥️"
           tabuleiroPC[y+1][x] = "🛥️"
           tabuleiroPC[y+2][x] = "🛥️"
       else:
           mediumShip()

def submarine():
   dir = random.randint(0, 1)

   if dir == 0:
       x = random.randint(1, 9)
       y = random.randint(1, 5)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y][x+1] == "🌊":
           tabuleiroPC[y][x] = "🛁"
           tabuleiroPC[y][x+1] = "🛁"
       else:
           submarine()

   if dir == 1:
       x = random.randint(1, 10)
       y = random.randint(1, 4)

       if tabuleiroPC[y][x] == "🌊" and tabuleiroPC[y+1][x] == "🌊":
           tabuleiroPC[y][x] = "🛁"
           tabuleiroPC[y+1][x] = "🛁"
       else:
           submarine()


def boat():

    x = random.randint(1, 10)
    y = random.randint(1, 5)

    if tabuleiroPC[y][x] == "🌊":
        tabuleiroPC[y][x] = "⛵"
    else:
        boat()

def stringParaNum(x, y):

    if x == "A" or x == "a":
        x = 1
        return x
    elif x == "B" or x == "b":
        x = 2
        return x
    elif x == "C" or x == "c":
        x = 3
        return x
    elif x == "D" or x == "d":
        x = 4
        return x
    elif x == "E" or x == "e":
        x = 5
        return x
    elif x == "F" or x == "f":
        x = 6
        return x
    elif x == "G" or x == "g":
        x = 7
        return x
    elif x == "H" or x == "h":
        x = 8
        return x
    elif x == "I" or x == "i":
        x = 9
        return x
    elif x == "J" or x == "j":
        x = 10
        return x
    else:
        x = 0
        return x

def stringAtaque(x):

    if x == "A" or x == "a":
        x = 1
        return x
    elif x == "B" or x == "b":
        x = 2
        return x
    elif x == "C" or x == "c":
        x = 3
        return x
    elif x == "D" or x == "d":
        x = 4
        return x
    elif x == "E" or x == "e":
        x = 5
        return x
    elif x == "F" or x == "f":
        x = 6
        return x
    elif x == "G" or x == "g":
        x = 7
        return x
    elif x == "H" or x == "h":
        x = 8
        return x
    elif x == "I" or x == "i":
        x = 9
        return x
    elif x == "J" or x == "j":
        x = 10
        return x
    else:
        print("Coluna Inválida!")
        time.sleep((1))
        print("\n" * 1000)
        exibirTabuleiro()
        return ataque("player")

def gigaShipPlayer():
   print("Coloque seu Porta-Aviões, ele ocupa 5 Espaços!\n")
   exibirJogador()

   dir = input("Escolha direção do seu Navio:\n 0 - Horizontal\n 1 - Vertical\n ")

   if dir == "0":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), gigaShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if x >= 1 and x <= 6 and y <= 5:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y][x+1] == "🌊" and tabuleiroJogador[y][x+2] == "🌊" and tabuleiroJogador[y][x+3] == "🌊" and tabuleiroJogador[y][x+4] == "🌊":
                   tabuleiroJogador[y][x] = "🛳️"
                   tabuleiroJogador[y][x+1] = "🛳️"
                   tabuleiroJogador[y][x+2] = "🛳️"
                   tabuleiroJogador[y][x+3] = "🛳️"
                   tabuleiroJogador[y][x+4] = "🛳️"
                   print("\n" * 1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   gigaShipPlayer()
           elif x >= 7 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               gigaShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               gigaShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           gigaShipPlayer()

   elif dir == "1":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), gigaShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if y == 1:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y+1][x] == "🌊" and tabuleiroJogador[y+2][x] == "🌊" and tabuleiroJogador[y+3][x] == "🌊" and tabuleiroJogador[y+4][x] == "🌊":
                   tabuleiroJogador[y][x] = "🛳️"
                   tabuleiroJogador[y+1][x] = "🛳️"
                   tabuleiroJogador[y+2][x] = "🛳️"
                   tabuleiroJogador[y+3][x] = "🛳️"
                   tabuleiroJogador[y+4][x] = "🛳️"
                   print("\n" * 1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   gigaShipPlayer()
           elif y >= 1 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               gigaShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               gigaShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           gigaShipPlayer()
   else:
       print("Direção inválida!!")
       time.sleep(1)
       print("\n"*1000)
       gigaShipPlayer()

def bigShipPlayer():
   print("Coloque seu Navio-Tanque, ele ocupa 4 Espaços!\n")
   exibirJogador()

   dir = input("Escolha direção do seu Navio:\n 0 - Horizontal\n 1 - Vertical\n ")

   if dir == "0":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), bigShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if x >= 1 and x <= 7 and y <= 5:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y][x+1] == "🌊" and tabuleiroJogador[y][x+2] == "🌊" and tabuleiroJogador[y][x+3] == "🌊":
                   tabuleiroJogador[y][x] = "⛴️"
                   tabuleiroJogador[y][x+1] = "⛴️"
                   tabuleiroJogador[y][x+2] = "⛴️"
                   tabuleiroJogador[y][x+3] = "⛴️"
                   print("\n"*1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   bigShipPlayer()
           elif x >= 8 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               bigShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               bigShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           bigShipPlayer()

   elif dir == "1":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), bigShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if y >= 1 and y <= 2:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y+1][x] == "🌊" and tabuleiroJogador[y+2][x] == "🌊" and tabuleiroJogador[y+3][x] == "🌊":
                   tabuleiroJogador[y][x] = "⛴️"
                   tabuleiroJogador[y+1][x] = "⛴️"
                   tabuleiroJogador[y+2][x] = "⛴️"
                   tabuleiroJogador[y+3][x] = "⛴️"
                   print("\n" * 1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   bigShipPlayer()
           elif y >= 3 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               bigShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               bigShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           bigShipPlayer()
   else:
       print("Direção inválida!!")
       time.sleep(1)
       print("\n"*1000)
       bigShipPlayer()

def mediumShipPlayer():
   print("Coloque seu Destróier, ele ocupa 3 Espaços!\n")
   exibirJogador()

   dir = input("Escolha direção do seu Navio:\n 0 - Horizontal\n 1 - Vertical\n ")

   if dir == "0":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), mediumShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if x >= 1 and x <= 8 and y <= 5:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y][x+1] == "🌊" and tabuleiroJogador[y][x+2] == "🌊":
                   tabuleiroJogador[y][x] = "🛥️"
                   tabuleiroJogador[y][x+1] = "🛥️"
                   tabuleiroJogador[y][x+2] = "🛥️"
                   print("\n"*1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   mediumShipPlayer()
           elif x >= 9 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               mediumShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               mediumShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           mediumShipPlayer()

   elif dir == "1":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), mediumShipPlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if y >= 1 and y <= 3:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y+1][x] == "🌊" and tabuleiroJogador[y+2][x] == "🌊":
                   tabuleiroJogador[y][x] = "🛥️"
                   tabuleiroJogador[y+1][x] = "🛥️"
                   tabuleiroJogador[y+2][x] = "🛥️"
                   print("\n" * 1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   mediumShipPlayer()
           elif y >= 4 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               mediumShipPlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               mediumShipPlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           mediumShipPlayer()
   else:
       print("Direção inválida!!")
       time.sleep(1)
       print("\n"*1000)
       mediumShipPlayer()

def submarinePlayer():
   print("Coloque seu Submarino, ele ocupa 2 Espaços!\n")
   exibirJogador()

   dir = input("Escolha direção do seu Navio:\n 0 - Horizontal\n 1 - Vertical\n ")

   if dir == "0":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), submarinePlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if x >= 1 and x <= 9 and y <= 5:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y][x+1] == "🌊":
                   tabuleiroJogador[y][x] = "🛁"
                   tabuleiroJogador[y][x+1] = "🛁"
                   print("\n"*1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   submarinePlayer()
           elif x >= 10 and y <= 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               submarinePlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               submarinePlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           submarinePlayer()

   elif dir == "1":
       x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), submarinePlayer))

       if x >= 1 and x <= 10:
           y = int(input("Escolha a linha (1-5): "))
           if y >= 1 and y <= 4:
               if tabuleiroJogador[y][x] == "🌊" and tabuleiroJogador[y+1][x] == "🌊":
                   tabuleiroJogador[y][x] = "🛁"
                   tabuleiroJogador[y+1][x] = "🛁"
                   print("\n" * 1000)
               else:
                   print("Posição inválida! Há uma embarcação no caminho.")
                   time.sleep((2))
                   print("\n" * 1000)
                   submarinePlayer()
           elif y == 5:
               print("Sem espaço! Altere a direção, ou escolha outra posição.")
               time.sleep((2))
               print("\n" * 1000)
               submarinePlayer()
           else:
               print("Linha inválida!")
               time.sleep((1))
               print("\n" * 1000)
               submarinePlayer()
       else:
           print("Coluna inválida!")
           time.sleep((1))
           print("\n" * 1000)
           submarinePlayer()
   else:
       print("Direção inválida!!")
       time.sleep(1)
       print("\n"*1000)
       submarinePlayer()

def boatPlayer():
    print("Coloque seu Bote, ele ocupa 1 Espaço!\n")
    exibirJogador()

    x = (stringParaNum(str(input("Escolha a Coluna (A-J): ")), boatPlayer))

    if x >= 1 and x <= 10:
        y = int(input("Escolha a linha (1-5): "))
        if y >= 1 and y <= 5:
            if tabuleiroJogador[y][x] == "🌊":
                tabuleiroJogador[y][x] = "⛵"
                print("\n" * 1000)
            else:
                print("Posição inválida! Há uma embarcação no caminho.")
                time.sleep((2))
                print("\n" * 1000)
                boatPlayer()
        else:
            print("Linha inválida!")
            time.sleep((1))
            print("\n" * 1000)
            boatPlayer()
    else:
        print("Coluna inválida!")
        time.sleep((1))
        print("\n" * 1000)
        boatPlayer()

def exibirJogador():

    for linha in tabuleiroJogador:
        print(" ".join(linha))
    print("")

def exibirTabuleiro():

    atualizarPontos()
    print(f"==========[Computador]==========\nEmbarcações restantes: {naviosPC}")
    for linha in ocultoPC:
        print(" ".join(linha))
    print("---------------------------------")
    print(f"===========[Jogador ]===========\nEmbarcações restantes: {naviosJogador}")
    for linha in ocultoJogador:
        print(" ".join(linha))

def ataque(z):
    if z == "player":
        x = (stringAtaque(str(input("Escolha a Coluna (A-J): "))))

        if x >= 1 and x <= 10:
            y = int(input("Escolha a linha (1-5): "))
            if y >= 1 and y <= 5:
                if ocultoPC[y][x] != "💦" and ocultoPC[y][x] != "💥":
                    if tabuleiroPC[y][x] != "🌊":
                        tabuleiroPC[y][x] = "💥"
                        ocultoPC[y][x] = "💥"
                        print("\n" * 1000)
                        exibirTabuleiro()
                        print("Parabéns, você acertou uma embarcação!")
                        time.sleep((2))
                        print("\n" * 1000)
                        exibirTabuleiro()
                        if naviosPC > 0:
                            ataque("player")
                        else:
                            print("Parabéns! Você destruiu toda frota inimiga 😎")
                            time.sleep(2)
                            creditos()
                    else:
                        tabuleiroPC[y][x] = "💦"
                        ocultoPC[y][x] = "💦"
                        print("\n" * 1000)
                        exibirTabuleiro()
                        print("Que pena, você errou!")
                        time.sleep((2))
                        print("\n" * 1000)
                        exibirTabuleiro()
                        print("O Computador está atacando...")
                        time.sleep((2))
                        ataque("PC")


                else:
                    print("Posição Inválida! Esta região já foi atacada.")
                    time.sleep((2))
                    print("\n" * 1000)
                    exibirTabuleiro()
                    ataque("player")

            else:
                print("Linha inválida!")
                time.sleep((1))
                print("\n" * 1000)
                exibirTabuleiro()
                ataque("player")
    else:
        x = random.randint(1, 10)
        y = random.randint(1, 5)
        if ocultoJogador[y][x] != "💦" and ocultoJogador[y][x] != "💥":
            if tabuleiroJogador[y][x] != "🌊":
                ocultoJogador[y][x] = "💥"
                tabuleiroJogador[y][x] = "💥"
                print("\n" * 1000)
                exibirTabuleiro()
                print("O Computador acertou uma embarcação!")
                time.sleep((2))
                print("\n" * 1000)
                exibirTabuleiro()
                if naviosJogador > 0:
                    print("O Computador está atacando...")
                    time.sleep((2))
                    ataque("PC")
                else:
                    print("Que pena! Sua frota foi destrúida 😭")
                    time.sleep(2)
                    creditos()
            else:
                tabuleiroJogador[y][x] = "💦"
                ocultoJogador[y][x] = "💦"
                print("\n" * 1000)
                exibirTabuleiro()
                print("Ufa! O Computador errou.")
                time.sleep((2))
                print("\n" * 1000)
                exibirTabuleiro()
                print("Você está no seu turno, ataque o inimigo!")
                time.sleep(2)
                ataque("player")
        else:
            ataque("PC")

def atualizarPontos():
    global tabuleiroPC
    global tabuleiroJogador
    global pAvioesPC
    global pAvioesJogador
    global nTanquePC
    global nTanqueJogador
    global destroierPC
    global destroierJogador
    global subPC
    global subJogador
    global naviosPC
    global naviosJogador
    global botePC
    global boteJogador

    pAvioesPCCont = 0
    nTanquePCCont = 0
    destroierPCCont = 0
    subPCCont = 0
    botePCCont = 0

    pAvioesJogadorCont = 0
    nTanqueJogadorCont = 0
    destroierJogadorCont = 0
    subJogadorCont = 0
    boteJogadorCont = 0

    for i in range(6):
        for j in range(11):
            if "🛳️" in tabuleiroPC[i][j]:
                pAvioesPCCont += 1

    for i in range(6):
        for j in range(11):
            if "⛴️" in tabuleiroPC[i][j]:
                nTanquePCCont += 1

    for i in range(6):
        for j in range(11):
            if "🛥️" in tabuleiroPC[i][j]:
                destroierPCCont += 1

    for i in range(6):
        for j in range(11):
            if "🛁" in tabuleiroPC[i][j]:
                subPCCont += 1

    for i in range(6):
        for j in range(11):
            if "⛵" in tabuleiroPC[i][j]:
                botePCCont += 1

    if pAvioesPCCont == 0 and pAvioesPC == True:
        print("Você destruiu o Porta-Aviões inimigo!")
        pAvioesPC = False
        naviosPC -= 1

    if nTanquePCCont == 0 and nTanquePC == True:
        print("Você destruiu o Navio-Tanque inimigo!")
        nTanquePC = False
        naviosPC -= 1

    if destroierPCCont == 0 and destroierPC == True:
        print("Você destruiu o Destróier inimigo!")
        destroierPC = False
        naviosPC -= 1

    if subPCCont == 0 and subPC == True:
        print("Você destruiu o Submarino inimigo!")
        subPC = False
        naviosPC -= 1

    if botePCCont == 0 and botePC == True:
        print("Você destruiu o Bote inimigo!")
        botePC = False
        naviosPC -= 1


    for i in range(6):
        for j in range(11):
            if "🛳️" in tabuleiroJogador[i][j]:
                pAvioesJogadorCont += 1

    for i in range(6):
        for j in range(11):
            if "⛴️" in tabuleiroJogador[i][j]:
                nTanqueJogadorCont += 1

    for i in range(6):
        for j in range(11):
            if "🛥️" in tabuleiroJogador[i][j]:
                destroierJogadorCont += 1

    for i in range(6):
        for j in range(11):
            if "🛁" in tabuleiroJogador[i][j]:
                subJogadorCont += 1

    for i in range(6):
        for j in range(11):
            if "⛵" in tabuleiroJogador[i][j]:
                boteJogadorCont += 1

    if pAvioesJogadorCont == 0 and pAvioesJogador == True:
        print("Seu Porta-Aviões foi destruído!")
        pAvioesJogador = False
        naviosJogador -= 1

    if nTanqueJogadorCont == 0 and nTanqueJogador == True:
        print("Seu Navio-Tanque foi destruído!")
        nTanqueJogador = False
        naviosJogador -= 1

    if destroierJogadorCont == 0 and destroierJogador == True:
        print("Seu Destróier foi destruído!")
        destroierJogador = False
        naviosJogador -= 1

    if subJogadorCont == 0 and subJogador == True:
        print("Seu Submarino foi destruído!")
        subJogador = False
        naviosJogador -= 1

    if boteJogadorCont == 0 and boteJogador == True:
        print("Seu Bote foi destruído!")
        boteJogador = False
        naviosJogador -= 1

gigaShip()
bigShip()
mediumShip()
submarine()
boat()

print("===========💣Bem-vindo ao Batalha Naval🚢===========")
print("Posicione suas embarcações para iniciarmos a batalha!")
print("====================================================")

time.sleep(3)

gigaShipPlayer()
time.sleep((0.5))
print("\n" * 1000)
bigShipPlayer()
time.sleep((0.5))
print("\n" * 1000)
mediumShipPlayer()
time.sleep((0.5))
print("\n" * 1000)
submarinePlayer()
time.sleep((0.5))
print("\n" * 1000)
boatPlayer()
print("\n" * 1000)
exibirJogador()
time.sleep((2))
print("\n" * 1000)

exibirTabuleiro()
print("Você está no seu turno, ataque o inimigo!")
time.sleep(2)
ataque("player")








