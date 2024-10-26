P = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spr = 0
def ruch(P):
    for k in P:
        print(k)

def ruch_x(P):
    a = int(input("podaj wiersz:"))
    b = int(input("podaj kolumnę:"))
    P[a][b] = 1
    for k in P:
        print(k)

def ruch_o(P):
    a = int(input("podaj wiersz:"))
    b = int(input("podaj kolumnę:"))
    P[a][b] = 2
    for k in P:
        print(k)

while spr == 0:
    ruch_x(P)
    if P[0][0] == 2 and P[0][1] == 2 and P[0][2] == 1 or P[1][0] == 2 and P[1][1] == 2 and P[1][2] == 2 or P[2][0] == 2 and P[2][1] == 2 and P[2][2] == 2 or P[0][0] == 2 and P[1][0] == 2 and P[2][0] == 2 or P[0][1] == 2 and P[1][1] == 2 and P[2][1] == 2 or P[0][2] == 2 and P[1][2] == 2 and P[2][2] == 2 or P[0][0] == 2 and P[1][1] == 2 and P[2][2] == 2 or P[0][2] == 2 and P[1][1] == 2 and P[2][0] == 2:
        spr = 1
        print("wygrywa kółko")
    ruch_o(P)
    if P[0][0] == 1 and P[0][1] == 1 and P[0][2] == 1 or P[1][0] == 1 and P[1][1] == 1 and P[1][2] == 1 or P[2][0] == 1 and P[2][1] == 1 and P[2][2] == 1 or P[0][0] == 1 and P[1][0] == 1 and P[2][0] == 1 or P[0][1] == 1 and P[1][1] == 1 and P[2][1] == 1 or P[0][2] == 1 and P[1][2] == 1 and P[2][2] == 1 or P[0][0] == 1 and P[1][1] == 1 and P[2][2] == 1 or P[0][2] == 1 and P[1][1] == 1 and P[2][0] == 1:
        spr = 1
        print("wygrywa krzyżyk")

