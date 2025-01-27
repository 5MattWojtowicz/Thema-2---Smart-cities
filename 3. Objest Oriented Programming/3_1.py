#klasse persoon aanmaken met attributen
class persoon:
    def __init__ (self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __str__ (self):
        return "Mijn naam is {} {}".format(self.voornaam, self.achternaam)
    
#subklasse aanmaken voor studenten
class student(persoon):

    def welkom(self):
        return "Welkom {} {}".format(self.voornaam, self.achternaam)

#persoon1 instellen
persoon1 = persoon("John", "Doe")
print(persoon1)

#student1 instellen
student1 = student("Mike", "Olsen")
print(student1.welkom())