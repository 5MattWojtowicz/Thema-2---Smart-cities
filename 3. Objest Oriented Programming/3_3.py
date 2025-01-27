class persoon:
    def __init__ (self, naam):
        self.naam = naam
        
#methodes aanmaken
    def krijgnaam(self):
        return "{}".format(self.naam)

    def ismedewerker(self):
        return "False"

#subklasse aanmaken
class medewerker (persoon):

#methode aanmaken
    def ismedewerker(self):
        return "True"


#personen instellen
jan = persoon("Jan")
ben = medewerker("ben")

#print de naam en of de persoon een medewerker is
print(jan.krijgnaam(), jan.ismedewerker())
print(ben.krijgnaam(), ben.ismedewerker())