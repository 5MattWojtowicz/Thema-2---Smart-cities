#klasse aanmaken voor elke leering zijn naam, nummer en klas te geven, als er niets voor klas wordt ingevoerd zal
#de leerling automatisch in 1A gaan.
class school:
    def __init__ (self, naam, nummer, klas = "1A"):
        self.naam = naam
        self.klas = klas
        self.nummer = nummer
        

    def leerling_inschrijven(self, klas_inschrijving):
        self.klas = klas_inschrijving

    def leerling_uitschrijven(self):
        self.klas = ""   
    
#leerlingen instellen
leerling1 = school("Jan Jansens",7)
leerling2 = school("Marie Mariën",10)
leerling3 = school("Bert Balders",14,"1B")


leerling2.leerling_uitschrijven()
leerling1.leerling_inschrijven("1C")


