#klasse aanmaken voor elke leering zijn naam, nummer en klas te geven, als er niets voor klas wordt ingevoerd zal
#de leerling automatisch in 1A gaan.
class school:
    def __init__ (self, naam, nummer, klas = "1A"):
        self.naam = naam
        self.klas = klas
        self.nummer = nummer


#leerlingen instellen
leerling1 = ("Jan Jansens",7)
leerling2 = ("Marie Mariën",10)
leerling3 = ("Bert Balders",14,"1B")