#klasse persoon aanmaken met attributen
class persoon:
    def __init__ (self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __str__ (self):
        return "Mijn naam is {} {}".format(self.voornaam, self.achternaam)
    
#subklasse aanmaken voor studenten en attributen van superklasse overnemen
class student(persoon):
    def __init__ (self,voornaam,achternaam, afstudeerjaar):
        super().__init__(voornaam,achternaam)
        self.afstudeerjaar = afstudeerjaar


    def welkom(self):
        return "Welkom {} {} bij de klas van {}".format(self.voornaam, self.achternaam, self.afstudeerjaar)

#persoon1 instellen
persoon1 = persoon("John", "Doe")
print(persoon1)

#student1 instellen
student1 = student("Mike","Olsen","2019")
print(student1.welkom())