prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"

#Opdracht 4
#print(reclame_tekst)

#Opdracht 5
# --> Berekenen totaal aantal tekens
#print(len(reclame_tekst))

reclame_tekst2 = reclame_tekst[:63]

#Opdracht 5
#print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2.upper()

#Opdracht 6
#print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split()

#Opdracht 7
#print(reclame_tekst4)

for el in reclame_tekst4:
    #Opdracht 9
    #print(el.lower())
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())