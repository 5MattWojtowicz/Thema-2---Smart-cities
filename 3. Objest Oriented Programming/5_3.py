#klasse voor een boek aanmaken met een titel en de attributen van auteur
class boek:
    def __init__ (self, titel, auteur):
        self.titel  = str(titel)
        self.auteur = auteur

#functie die de titel van het boek en de naam van de auteur teruggeeft
    def toonInformatie(self):
        return "{}is geschreven door {}".format(self.titel, self.auteur.naam)

#klasse auteur die een naam en geboortedatum heeft als attribuut
class auteur:
    def __init__ (self, naam, geboortedatum):
        self.naam = str(naam)
        self.geboortedatum = str(geboortedatum) 

#objecten instellen en de functie toonInformatie aanroepen
info = auteur("J.K. Rowling", "31 juli 1965") 
boek1 = boek("Harry Potter",info)
print(boek1.toonInformatie())              