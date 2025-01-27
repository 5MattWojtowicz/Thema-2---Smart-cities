#superklasse gegevens aanmaken met een attribuut naam en een methode
class gegevens():
    def __init__(self,naam):
        self.naam = naam

    def krijgnaam(self):
        return "{}".format(self.naam) 

#subklasse van gegvens aanmaken met dezelfde attributen van gegvens plus een exta attribuut en een methode
class kind(gegevens):
    def __init__(self,naam, leeftijd):
        self.leeftijd = leeftijd
        super().__init__(naam)

    def krijgleeftijd(self):
        return "{}".format(self.leeftijd)

#een subklasse maken van de klasse kind en ook de attributen mee overnemen plus een extra attribuut en een methode
class kleinkind(kind):
    def __init__(self,naam, leeftijd, adres):
        self.adres = adres
        super().__init__(naam, leeftijd)

    def krijgAdres(self):
        return "{}".format(self.adres)


#kleinkind1 instellen met de juiste attributen
kleinkind1 = kleinkind("Lana",15,"Turnhout")

#alle methodes printen van kleinkind
print(kleinkind1.krijgnaam(),kleinkind1.krijgleeftijd(),kleinkind1.krijgAdres())