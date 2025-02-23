#klasse functie aanmaken met benodigde attributen
class Functie:
    def __init__(self, omschrijving: str, loon: int, opslag: float):
        self.omschrijving = omschrijving
        self.loon = loon  
        self.opslag = opslag 

#methode die de opslag berekent
    def berekenOpslagJaar(self):
        return self.loon * self.opslag  

#klasse aanmaken voor gegevens met benodigde attributen
class Gegevens:
    def __init__(self, naam: str, voornaam: str, ancienniteit: int, functie: Functie):
        self.naam = naam
        self.voornaam = voornaam
        self.ancienniteit = ancienniteit 
        self.functie = functie  

#string methode voor het weergeven van de berekende waardes
    def __str__(self):
        return "{} {} werkt al {} jaar in ons bedrijf.".format(self.voornaam,self.naam,self.ancienniteit)

    def berekenOpslagAnc(self):
        return self.functie.berekenOpslagJaar() * self.ancienniteit  


#objecten aanmaken met benodigde waardes
functie_manager = Functie("Manager", 2000, 0.05)  
medewerker = Gegevens("Maes", "Marie", 5, functie_manager)

#methodes aanroepen en de resultaten printen
print(medewerker) 
print(medewerker.functie.berekenOpslagJaar())  
print(medewerker.berekenOpslagAnc()) 
