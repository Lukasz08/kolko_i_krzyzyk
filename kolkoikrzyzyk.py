P = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def ruch(P):
    for k in P:
        print(k)

def ruch_x(P):
    a = int(input("podaj wiersz:"))
    b = int(input("podaj kolumnę:"))
    P.pop(a[b])
    P.insert(a[b], x)

for i in range(9):
    ruch_x(P)
