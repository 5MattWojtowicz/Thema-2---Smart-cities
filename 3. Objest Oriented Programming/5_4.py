#klasse aanmaken voor Meter
class Meter:
    def __init__(self, waarde: float):
        self.waarde = waarde  

    def __str__(self):
        return "{} meter".format(self.waarde)

#omzetting maken
    def naar_centimeter(self):
        return Centimeter(self.waarde * 100)  

#klasse aanmaken voor Centimeter
class Centimeter:
    def __init__(self, waarde: float):
        self.waarde = waarde  

    def __str__(self):
        return "{} centimeter".format(self.waarde)

#omzetting maken
    def naar_meter(self):
        return Meter(self.waarde / 100)  


#Objecten aanmaken
geodriehoek = Centimeter(14)
lintmeter = Meter(2.5)

#methodes printen
print(geodriehoek.naar_meter()) 
print(lintmeter.naar_centimeter())  
