from math import *
from random import *
#�lesanne 11

#11
print("Arvuti m�istatab numbrit 1-10 ja sina �ritad seda �ra arvuti.")
a=randint(1,10)
vastus=int(input("Mis arv on m�istatanud arvutit:"))
k=p=1
while vastus!=a:
    print("�ra sa ei arvanud �ra, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2:
        print("P��luseda on l�ppenud")
        b=print("Proovi veel kord: S")
        if b.upper()=="J�H":
            k=0
            continue
        else:
            break
if vastus==a:
    print("Palju �nne, sa arvasid �ra!",p )
 
print()


#�lesanne
#0
while True:
    number = int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("�igessti")
        break
    else:
        print("Arv on liiga v�ike")
print("katsed",p)

#22
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "komm":
        print(f"Teil kommid kirjutakse kulua katsed katse.")
        break
katsed=0
answer=""
while answer!="komm":
    answer=input("Tahan kommi!")
    katsed+=1
print(f"Katsed: {katsed}")
print()

#1
while True:
    try:
        nimi=input("Palun sisesta oma nimi:")
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervistus saada: "))
            for i in range(1, n+1):
                print(f"Ole tervitatud, {nimi}, {i}. korda.")
        else:
            break
    
