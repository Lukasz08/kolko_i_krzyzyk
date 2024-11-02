P = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
spr = 0

def ruch_x(P):
    a = int(input("podaj wiersz:"))
    b = int(input("podaj kolumnę:"))
    while P[a][b] != ' ':
        a = int(input("podaj wiersz:"))
        b = int(input("podaj kolumnę:"))
    P[a][b] = "x"
    for k in P:
        print(k)

def ruch_o(P):
    a = int(input("podaj wiersz:"))
    b = int(input("podaj kolumnę:"))
    while P[a][b] != ' ':
        a = int(input("podaj wiersz:"))
        b = int(input("podaj kolumnę:"))
    P[a][b] = "o"
    for k in P:
        print(k)

while spr == 0:
    ruch_o(P)
    if P[0][0] == "o" and P[0][1] == "o" and P[0][2] == "o" or P[1][0] == "o" and P[1][1] == "o" and P[1][2] == "o" or P[2][0] == "o" and P[2][1] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][0] == "o" and P[2][0] == "o" or P[0][1] == "o" and P[1][1] == "o" and P[2][1] == "o" or P[0][2] == "o" and P[1][2] == "o" and P[2][2] == "o" or P[0][0] == "o" and P[1][1] == "o" and P[2][2] == "o" or P[0][2] == "o" and P[1][1] == "o" and P[2][0] == "o":
        spr = 1
        print("wygrywa kółko")
        break
    ruch_x(P)
    if P[0][0] == "x" and P[0][1] == "x" and P[0][2] == "x" or P[1][0] == "x" and P[1][1] == "x" and P[1][2] == "x" or P[2][0] == "x" and P[2][1] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][0] == "x" and P[2][0] == "x" or P[0][1] == "x" and P[1][1] == "x" and P[2][1] == "x" or P[0][2] == "x" and P[1][2] == "x" and P[2][2] == "x" or P[0][0] == "x" and P[1][1] == "x" and P[2][2] == "x" or P[0][2] == "x" and P[1][1] == "x" and P[2][0] == "x":
        spr = 1
        print("wygrywa krzyżyk")
