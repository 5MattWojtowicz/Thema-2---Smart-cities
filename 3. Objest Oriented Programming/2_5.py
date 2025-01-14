#klasse aanmaken voor elke apparte fiets met hun nummer en kiezen of hij klassiek of elektrisch is
class fiets:
    def __init__ (self, nummer, type, status = False):
        self.nummer = nummer
        self.type = type
        self.status = status
    #methode aanmaken voor na te kijken of de fiets al is uitgeleend.
    def fiets_uitlenen (self):
        if self.status == True:
            print("De fiets is al uitgeleend")

        if self.status == False:
            print("Je kan de fiets uitlenen")     
      
#elke fiets instellen
fiets1 = fiets(20,"elktrische")
fiets2 = fiets(31,"klassieke")
fiets3 = fiets(5,"klassieke")

#vragen om de fiets uit te lenen.
fiets3.fiets_uitlenen()



