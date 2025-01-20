#klasse figuren aanmaken met attributen
class figuren:
    def __init__ (self, vorm, breedte, hoogte):
        self.vorm = vorm
        self.breedte = breedte
        self.hoogte = hoogte

#attributen van een figuur printen
    def __str__(self):
        return "Figuur heeft een breedte van {} en een hoogte van {}".format(self.breedte, self.hoogte)

#oppervlakte van een rechthoek berekenen
    def oppervlakte_rechthoek_berekenen(self):
        if self.vorm == "vierkant":
            print(self.breedte * self.hoogte)
    
#de omtrek van elke figuur berekenen    
    def omtrek_figuren(self):
        print((self.breedte * 2) + (self.hoogte * 2))

#figuur1 aanmaken
figuur1 = figuren("vierkant",5,2)

#alle methodes van de figuur uitvoeren en de attributen printen
figuur1.oppervlakte_rechthoek_berekenen()
figuur1.omtrek_figuren()
print(figuur1)

