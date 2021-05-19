import random


def neustart():

    zufallszahl = random.randint(0, 100)
    zahl = input("Gib eine zahl zwischen 0 und 100 ein ")
    Anzahlversuche = 0

    while zufallszahl != int(zahl):
        Anzahlversuche = Anzahlversuche+1
        if zufallszahl < int(zahl):
            zahl = input("Gib eine kleinere Zahl ein ")
        else:
            zahl = input("Gib eine grössere Zahl ein ")

    print("Du hast die Zahl erraten")
    print(f"Du hast {Anzahlversuche} versuche gebraucht")
    wiederholen = input("Möchtest du nochmal spielen? Ja/Nein ")

    if wiederholen == "Ja":
        neustart()

neustart()