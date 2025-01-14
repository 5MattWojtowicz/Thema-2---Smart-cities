#klasse aanmaken voor elke apparte fiets met hun nummer en kiezen of hij klassiek of elektrisch is
class fiets:
    def __init__ (self, nummer, type):
        self.nummer = nummer
        self.type = type

#elke fiets instellen
fiets1 = fiets(20,"elktrische")
fiets2 = fiets(31,"klassieke")
fiets3 = fiets(5,"klassieke")


#elke fiets printen
print(type(fiets1))
print(type(fiets2))
print(type(fiets3))