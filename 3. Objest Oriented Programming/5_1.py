#klasse boete aanmaken met hun attributen
class Boete:
    def __init__(self, niveau, prijs):
        self.niveau = int(niveau)
        self.prijs = int(prijs)

#functie aanmaken om de boete te printen
    def __str__(self):
        return "Je hebt een boete van niveau {}. Je moet {} euro betalen.".format(self.niveau, self.prijs)

#klasse opvertreding aanmaken
class Overtreding:
    def __init__(self, maxSnelheid, geredenSnelheid):
        self.maxSnelheid = int(maxSnelheid)
        self.geredenSnelheid = int(geredenSnelheid)

#fucntie aanmaken die het niveau en de prijs bepaald van de boete
    def bepaalBoete(self):
        overtreding = self.geredenSnelheid - self.maxSnelheid
        
        if overtreding < 0:
            return Boete(0, 0)
        elif overtreding < 10:
            return Boete(1, 50)
        elif overtreding < 20:
            return Boete(2, 100)
        else:
            return Boete(3, 150)


#een overtreding aanmaken en vervolgens de boete bepalen en printen
overtreding = Overtreding(50, 55)
boete = overtreding.bepaalBoete()
print(boete)  
  



        
           