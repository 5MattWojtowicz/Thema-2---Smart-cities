#klasse aanmaken voor Categorie
class Categorie:
    def __init__(self, naam):
        self.naam = str(naam) 

#klasse aanmaken voor Product
class Product:
    def __init__(self, naam, categorie: Categorie):
        self.naam = str(naam)  
        self.categorie = categorie  

#methode die nakijkt of de objecten tot dezelfde soort behoren
    def behoortTotCategorie(self, categorie: Categorie) -> bool:
        return self.categorie.naam == categorie.naam  


#objecten instellen
fruit = Categorie("Fruit")
brood = Categorie("Brood")

appel = Product("Appel", fruit)

#methode aanroepen voor na te kijken of de objecten tot dezelfde soort behoren
print(appel.behoortTotCategorie(fruit))  
print(appel.behoortTotCategorie(brood))  
