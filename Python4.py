import random

class GameOver(Exception):
    pass

class Spieler:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.maxAttack = 25
        self.maxDefens = 5


spieler1 = Spieler(input("Gib Name für Spieler1 ein "))
spieler2 = Spieler(input("Gib Name für Spieler2 ein "))

print(f"spieler1 dein Name ist {spieler1.name}")
print(f"spieler2 dein name ist {spieler2.name}")
print("---------------------")


def playerTurn(ausgewaehlterSpieler, gegner):
    Auswahl = input(
        f"{ausgewaehlterSpieler.name} beginnt Wähle aus ob du einen Angriff[1] oder ein Block[2] machen möchtest ")
    bonus = 5
    if int(Auswahl) == 1:
        Attacke = random.randrange(ausgewaehlterSpieler.maxAttack)+bonus
        Defens = random.randrange(gegner.maxDefens)


    elif int(Auswahl) == 2:
        Attacke = random.randrange(gegner.maxAttack)
        Defens  = random.randrange(ausgewaehlterSpieler.maxDefens)+bonus

    Attacke = Attacke - Defens
    if Attacke < 0:
        print(f"{gegner.name} hat geblockt du Hast kein Schaden gemacht.")
    else:
        gegner.health = gegner.health - Attacke
        print(f"Du hast {gegner.name} {Attacke} Schaden hinzugefügt")
        print(f"{gegner.name} hat noch {gegner.health} Leben\n")

    if ausgewaehlterSpieler.health <= 0:
        print(f"{ausgewaehlterSpieler.name} hat verloren {gegner.name} hat gewonnen.")
        raise GameOver
    elif gegner.health <= 0:
        print(f"{gegner.name} hat verloren {ausgewaehlterSpieler.name} hat gewonnen.")
        raise GameOver


while spieler1.health > 0 and spieler2.health > 0:
    try:
        playerTurn(spieler1, spieler2)
        playerTurn(spieler2, spieler1)
    except GameOver:
        pass

