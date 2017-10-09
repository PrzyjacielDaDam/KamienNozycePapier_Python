import random

#GAME BY Damian Lielbriedis (9.14.2017) pierwszy projekt obiektowy w Python'ie

class Przeciwnik:
    wygranych = 0
    znak = 0         # 0 - kamien, 1 - nozyczki, 2 - papier

    def __init__(self):
        Przeciwnik.wygranych = 0

    def Graj(self):
        Przeciwnik.znak = random.randint(0,2)

class Gracz:
    wygranych = 0
    znak = 0
    znakString = ""
    def __init__(self):
        Gracz.wygranych = 0
        Gracz.znak = 0
        Gracz.znakString = ""

    def Graj(self):
        Gracz.znakString = input("Wybierz (k, n, p): ")
        if(Gracz.znakString == 'k'):  Gracz.znak = 0
        elif (Gracz.znakString == 'n'):  Gracz.znak = 1
        elif (Gracz.znakString == 'p'):  Gracz.znak = 2

class Gra:
    runda = 0 # "do 3 razy sztuka"
    kolej = 0
    gracz = Gracz()
    przeciwnik = Przeciwnik()

    def __init__(self):
        Gra.runda = -1
        Gra.NowaRunda(self)

    def SprawdzWynik(self):
        if (Przeciwnik.znak == 0 and Gracz.znak == 0): Gra.Remis(self)
        elif (Przeciwnik.znak == 0 and Gracz.znak == 1): Gra.WygrywaPrzeciwnik(self)
        elif (Przeciwnik.znak == 0 and Gracz.znak == 2): Gra.WygrywaGracz(self)

        elif (Przeciwnik.znak == 1 and Gracz.znak == 0): Gra.WygrywaGracz(self)
        elif (Przeciwnik.znak == 1 and Gracz.znak == 1): Gra.Remis(self)
        elif (Przeciwnik.znak == 1 and Gracz.znak == 2): Gra.WygrywaPrzeciwnik(self)

        elif (Przeciwnik.znak == 2 and Gracz.znak == 0): Gra.WygrywaPrzeciwnik(self)
        elif (Przeciwnik.znak == 2 and Gracz.znak == 1): Gra.WygrywaGracz(self)
        elif (Przeciwnik.znak == 2 and Gracz.znak == 2): Gra.Remis(self)

    def WygrywaGracz(self):
        Gra.runda += 1
        Gracz.wygranych += 1
        print("Wygrales!")
        Gra.NowaRunda(self)

    def WygrywaPrzeciwnik(self):
        Gra.runda += 1
        Przeciwnik.wygranych += 1
        print("Przegrales!")
        Gra.NowaRunda(self)

    def Remis(self): #powtorz runde
        print("Remis!")
        Gra.NowaRunda(self)

    def NowaRunda(self):
        if(Przeciwnik.wygranych > 2 or Gracz.wygranych > 2):
            print("Wynik (Gracz : Przeciwnik): ", Gracz.wygranych, ":", Przeciwnik.wygranych)
            print("###_KONIEC_###")
        else:
            print("Wynik (Gracz : Przeciwnik): ", Gracz.wygranych, ":", Przeciwnik.wygranych)
            Przeciwnik.Graj(self)
            Gracz.Graj(self)
            Gra.SprawdzWynik(self)




def Main():
    print("###_Kamien, Nozyce, Papier_###")
    print("###_(Do trzech razy sztuka)_###\n")
    Gra() #rozpocznij nowa gre



Main()