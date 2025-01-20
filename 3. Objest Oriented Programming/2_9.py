#klasse aanmaken voor elke auto en hun waarde om mee te vergelijken
class auto:

    def __init__ (self, kleur, prijs, waarde):
        self.kleur = kleur
        self.prijs = prijs
        self.waarde = waarde

#methonde voor de prijs te vergelijken
    def prijsVergelijker(self):
        print(self.prijs - self.waarde)
    
#voorbeeld van rode auto gerbuiken
rode_auto = auto("rood", 13000, 20000)

rode_auto.prijsVergelijker()  