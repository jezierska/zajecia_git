import random
losowanie liczb całkowitych w daym zakresie
wylosowana = random.randint(1,10)
print(wylosowana)

# losowanie liczb rzeczywistych
wylosowana = random.random()
print(wylosowana)

losowanie liczb rzeczywistych w podanym zakresie
wylosowana = random.randint(0,1)+random.random()
print(wylosowana)

wylosowana = 2*random.random()
print(wylosowana)

wylosowana = random.randint(0,9)+random.random()-5
print(wylosowana)

# zaokrąglanie do danej liczby miejsc po przecinku
wylosowana = random.random()
zaokraglona = round(wylosowana,2)
print(zaokraglona)

# losowanie elementów - polecenie choice używamy do liter
import random
slowo = "Kognitywistyka"
wylosowana = random.choice(slowo)
print(wylosowana)

# mierzenie czasu
import time
cyfra = 0
start = time.time()
#print(start) # - liczba milisekund, która upłynęła od konkretnej daty
while cyfra != 1:
    print("Nie wcisnąłeś \"1\"\n")
    cyfra = int(input())
koniec = time.time()
czas_trwania = koniec - start
print("Na wciśnięcie 1 potrzebowałeś:", czas_trwania)

# wstrzymywanie działania programu
print("Początek:", time.ctime())
time.sleep(5)
print("Koniec:", time.ctime())

# zadanie 1
import time
print("Ciasteczka będą gotowe za:")
for i in range(5,0,-1):
    time.sleep(1)
    print(i)
time.sleep(1)
print("Ding!")

# zadanie 3
import random
wylosowana = random.randint(1,6)
print("Wynik Twojego rzutu kostką to:", wylosowana)

# zadanie 4
import random
for i in range(6):
    wylosowana = random.randint(2,48)
    print(wylosowana)

# zadanie 5
import random
wylosowana1 = random.randint(2,48)
wylosowana2 = random.randint(2,48)
wylosowana3 = random.randint(2,48)
wylosowana4 = random.randint(2,48)
wylosowana5 = random.randint(2,48)
wylosowana6 = random.randint(2,48)

print(wylosowana1)
if wylosowana2 != wylosowana1:
    print(wylosowana2)
if wylosowana3 != wylosowana2 and wylosowana3 != wylosowana1:
    print(wylosowana3)
if wylosowana4 != wylosowana3 and wylosowana4 != wylosowana2 and wylosowana4 != wylosowana1:
    print(wylosowana4)
if wylosowana5 != wylosowana4 and wylosowana5 != wylosowana3 and wylosowana5 != wylosowana2 and wylosowana5 != wylosowana1:
    print(wylosowana5)
if wylosowana6 != wylosowana5 and wylosowana6 != wylosowana4 and wylosowana6 != wylosowana3 and wylosowana6 != wylosowana2 and wylosowana6 != wylosowana1:
    print(wylosowana6)

# zadanie 6
import random
import time

print("Wyświetli się litera. Twoim zadaniem jest jak najszybsze naciśnięcie przycisku odpowiadającemu tej literze na klawiaturze")
litery = "qwertyuiopasdfghjklzxcvbnm"
wylosowana = random.choice(litery)
print(wylosowana)
start = time.time()
odpowiedz = input()
koniec = time.time()
czas = koniec-start
print("odpowiedź zajęła Tobie:", czas)

# zadanie 7
import random
import time
print("Wyświetli się litera. Twoim zadaniem jest jak najszybsze naciśnięcie przycisku odpowiadającemu tej literze na klawiaturze")
suma = 0
for i in range(5):
    litery = "qwertyuiopasdfghjklzxcvbnm"
    wylosowana = random.choice(litery)
    print(wylosowana)
    start = time.time()
    odpowiedz = input()
    koniec = time.time()
    czas = koniec-start
    print(czas)
    suma = suma+czas
    print(suma)

srednia = suma/5.0
print("Średnia czasu reakcji to:", srednia)

# zadanie 8
import random
while True:
    wylosowana = random.randint(0,99)
    if wylosowana <= 90:
        print(wylosowana)
    else:
        break

# zadanie 9
import random
print("Wybierz liczbę w zakresie od 1 do 100")
liczba = int(input())
wylosowana = random.randint(1,100)
if liczba > wylosowana:
    print("Moja liczba to", wylosowana, "Wygrałxś!")
elif liczba < wylosowana:
    print("Moja liczba to", wylosowana,"Przegrałxś...")
elif liczba == wylosowana:
    print("Moja liczba to", wylosowana,"Remis.")
else:
    print("błąd")

# zadanie 10
import random
print("Podaj liczbę")
liczba = int(input())
wylosowana = random.randint(liczba, 100)
print(wylosowana)

# zadanie 11
import random
print("Wybierz, czym chcesz zagrać:\n Wciśnij\'1\' jeśli kamieniem\n Wciśnij\'2\' jeśli papierem\n Wciśnij\'3\' jeśli nożycami")
wybor = int(input())
komputer = random.randint(1,3)
# if wybor == 1 and komputer == 1:
#     print("Wybór komputera: kamień. Remis!")
# elif wybor == 2 and komputer == 2:
#     print("Wybór komputera: papier. Remis!")
# elif wybor == 3 and komputer == 3:
#     print("Wybór komputera: nożyce. Remis!")
if wybor == komputer:
    print("Remis!")
elif wybor == 1 and komputer == 2:
    print("Kamień przegrywa z papierem - przegrałeś")
elif wybor == 1 and komputer == 3:
    print("Kamień tępi nożyce - wygrałeś!")
elif wybor == 2 and komputer == 1:
    print("Kamień przegrywa z papierem - wygrałeś!")
elif wybor == 2 and komputer == 3:
    print("Nożyce tną papier - przegrałeś")
elif wybor == 3 and komputer == 1:
    print("Kamień tępi nożyce - przegrałeś!")
elif wybor == 3 and komputer == 2:
    print("Nożyce tną papier - wygrałeś!")
else:
    print("błąd")

# zadanie 12
import time
print("podaj liczbę")
liczba = int(input())
while liczba>=0:
    print(liczba)
    time.sleep(1)
    liczba=liczba-1

# zadanie 13
import random
przyslowie1 = "Baba z wozu koniom lżej"
przyslowie2 = "Każdy kij ma dwa końce"
przyslowie3 = "Dzielić włos na czworo"
przyslowie4 = "Mieć mleko pod nosem"
przyslowie5 = "Być w czepku urodzonym"

print("Wylosowanei przysłowie to:")
przyslowie = random.randint(1,5)
if przyslowie ==1:
    print(przyslowie1)
elif przyslowie ==2:
    print(przyslowie2)
elif przyslowie ==3:
    print(przyslowie3)
elif przyslowie ==4:
    print(przyslowie4)
elif przyslowie ==5:
    print(przyslowie5)
else:
    print("błąd")

# zadanie 14
import random
liczba = random.random()
if liczba>=0 and liczba<0.1:
    print("<3")
elif liczba>=0.1 and liczba<0.2:
    print(":)")
elif liczba>=0.2 and liczba<0.3:
    print(";)")
elif liczba>=0.3 and liczba<0.4:
    print(":D")
elif liczba>=0.4 and liczba<0.5:
        print(":P")
elif liczba>=0.5 and liczba<0.6:
    print(":(")
elif liczba>=0.6 and liczba<0.7:
    print(":\'(")
elif liczba>=0.7 and liczba<0.8:
    print(":o")
elif liczba>=0.8 and liczba<0.9:
    print("XD")
elif liczba>=0.9 and liczba<1:
    print(":x")
