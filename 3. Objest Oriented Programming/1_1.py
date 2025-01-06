# Opgave: Code zonder functies met veel regels die afhankelijk zijn van elkaar.

prijs_maaltijd = 20
korting = 0
totale_prijs = 0

def korting_geven ():
 global korting
 if prijs_maaltijd > 15:
    korting = 0.1
 else:
    korting = 0

def totale_prijs_berekenen ():
 global totale_prijs
 totale_prijs = prijs_maaltijd - (prijs_maaltijd * korting)

def totale_prijs_printen():
 print(f"Totale prijs: €{totale_prijs}")
 print("Bon: Bedankt voor uw bestelling!")

korting_geven()
totale_prijs_berekenen()
totale_prijs_printen() 