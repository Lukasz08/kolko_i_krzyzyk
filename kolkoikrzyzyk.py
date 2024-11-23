from random import randint

g = int(input("podaj liczbę graczy (1 lub 2): "))
if g == 1:
    z = input("wybierz znak: ")
    while z != "o" and z != "x":
        print("Podano nieprawidłowe dane")
        z = input("wybierz znak: ")
P = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
spr = 0

def narysuj_plansze(P):
    print("     |     |     ")
    print(f"  {P[0][0]}  |  {P[0][1]}  |  {P[0][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {P[1][0]}  |  {P[1][1]}  |  {P[1][2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {P[2][0]}  |  {P[2][1]}  |  {P[2][2]}  ")
    print("     |     |     ")

def ruch_komputer(P, znak):
    a = randint(1, 3)
    b = randint(1, 3)
    while True:
        if P[a - 1][b - 1] == ' ':
            break
        a = randint(1, 3)
        b = randint(1, 3)
    for i in range(3):
        for j in range(3):
            pom = P
            pom[i][j] == znak
            print("pom", pom)
            print("P",P)
            print("znak",znak)
            print("i", i)
            print("j", j)
            if pom[0][0] == znak and pom[0][1] == znak and pom[0][2] == znak or pom[1][0] == znak and pom[1][1] == znak and pom[1][
                2] == znak or pom[2][0] == znak and pom[2][1] == znak and pom[2][2] == znak or pom[0][0] == znak and pom[1][
                0] == znak and pom[2][0] == znak or pom[0][1] == znak and pom[1][1] == znak and pom[2][1] == znak or pom[0][
                2] == znak and pom[1][2] == znak and pom[2][2] == znak or pom[0][0] == znak and pom[1][1] == znak and pom[2][
                2] == znak or pom[0][2] == znak and pom[1][1] == znak and pom[2][0] == znak:
                P[i][j] = znak
                break
    P[a - 1][b - 1] = znak

def ruch(P, znak):
    a = int(input("podaj wiersz: "))
    b = int(input("podaj kolumnę: "))
    while True:
        if a < 4 and b < 4 and a > 0 and b > 0:
            if P[a - 1][b - 1] == ' ':
                break
        print("Podano nieprawidłowe dane")
        a = int(input("podaj wiersz: "))
        b = int(input("podaj kolumnę: "))
    P[a - 1][b - 1] = znak

while spr == 0:
    if g == 1:
        if z == "o":
            ruch(P, z)
            if P[0][0] == "o" and P[0][1] == "o" and P[0][2] == "o" or P[1][0] == "o" and P[1][1] == "o" and P[1][
                2] == "o" or P[2][0] == "o" and P[2][1] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][0] == "o" and \
                    P[2][0] == "o" or P[0][1] == "o" and P[1][1] == "o" and P[2][1] == "o" or P[0][2] == "o" and P[1][
                2] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][1] == "o" and P[2][2] == "o" or P[0][2] == "o" and \
                    P[1][1] == "o" and P[2][0] == "o":
                spr = 1
                print("wygrywa kółko")
                narysuj_plansze(P)
                break
            ruch_komputer(P, "x")
            narysuj_plansze(P)
            if P[0][0] == "x" and P[0][1] == "x" and P[0][2] == "x" or P[1][0] == "x" and P[1][1] == "x" and P[1][
                2] == "x" or P[2][0] == "x" and P[2][1] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][0] == "x" and \
                    P[2][0] == "x" or P[0][1] == "x" and P[1][1] == "x" and P[2][1] == "x" or P[0][2] == "x" and P[1][
                2] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][1] == "x" and P[2][2] == "x" or P[0][2] == "x" and \
                    P[1][1] == "x" and P[2][0] == "x":
                spr = 1
                print("wygrywa krzyżyk")
                narysuj_plansze(P)
        if z == "x":
            ruch_komputer(P, "o")
            narysuj_plansze(P)
            if P[0][0] == "o" and P[0][1] == "o" and P[0][2] == "o" or P[1][0] == "o" and P[1][1] == "o" and P[1][
                2] == "o" or P[2][0] == "o" and P[2][1] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][0] == "o" and \
                    P[2][0] == "o" or P[0][1] == "o" and P[1][1] == "o" and P[2][1] == "o" or P[0][2] == "o" and P[1][
                2] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][1] == "o" and P[2][2] == "o" or P[0][2] == "o" and \
                    P[1][1] == "o" and P[2][0] == "o":
                spr = 1
                print("wygrywa kółko")
                narysuj_plansze(P)
                break
            ruch(P, z)
            if P[0][0] == "x" and P[0][1] == "x" and P[0][2] == "x" or P[1][0] == "x" and P[1][1] == "x" and P[1][
                2] == "x" or P[2][0] == "x" and P[2][1] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][0] == "x" and \
                    P[2][0] == "x" or P[0][1] == "x" and P[1][1] == "x" and P[2][1] == "x" or P[0][2] == "x" and P[1][
                2] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][1] == "x" and P[2][2] == "x" or P[0][2] == "x" and \
                    P[1][1] == "x" and P[2][0] == "x":
                spr = 1
                print("wygrywa krzyżyk")
                narysuj_plansze(P)
    if g == 2:
        ruch(P, "o")
        narysuj_plansze(P)
        if P[0][0] == "o" and P[0][1] == "o" and P[0][2] == "o" or P[1][0] == "o" and P[1][1] == "o" and P[1][
            2] == "o" or P[2][0] == "o" and P[2][1] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][0] == "o" and \
                P[2][0] == "o" or P[0][1] == "o" and P[1][1] == "o" and P[2][1] == "o" or P[0][2] == "o" and P[1][
            2] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][1] == "o" and P[2][2] == "o" or P[0][2] == "o" and \
                P[1][1] == "o" and P[2][0] == "o":
            spr = 1
            print("wygrywa kółko")
            break
        ruch(P, "x")
        narysuj_plansze(P)
        if P[0][0] == "x" and P[0][1] == "x" and P[0][2] == "x" or P[1][0] == "x" and P[1][1] == "x" and P[1][
            2] == "x" or P[2][0] == "x" and P[2][1] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][0] == "x" and \
                P[2][0] == "x" or P[0][1] == "x" and P[1][1] == "x" and P[2][1] == "x" or P[0][2] == "x" and P[1][
            2] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][1] == "x" and P[2][2] == "x" or P[0][2] == "x" and \
                P[1][1] == "x" and P[2][0] == "x":
            spr = 1
            print("wygrywa krzyżyk")
