#klasse punten aanmaken voor het punt dat de leerling behaalde
class Punten():
    def __init__(self, punt):
        self.punt = int(punt)

#functie die de max en gewicht van de klasse Test gebruikt voor het gewogen punt te berekenen
    def berekenpunt(self, max, gewicht):
        gewogen_punt = self.punt / max*gewicht
        print(gewogen_punt)

    def __repr__(self):
        print(self.punt)    

#klasse aanmaken voor het max punt en het gewichtpunt van de test
class Test():
    def __init__ (self, max, gewicht):
        self.max = int(max)
        self.gewicht = int(gewicht)

#objecten instellen en som uitvoeren
punt = Test(25, 20)
jef = Punten(15)
jef.berekenpunt(punt.max,punt.gewicht)

 

