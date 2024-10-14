from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_korting = prijs * (1-korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_korting} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(a, btw):
    totaal = sum(a)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomensten deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09

print(inkomsten_totaal(inkomsten_per_dag, btw_percentage))

#opdracht 8
def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return [laag, hoog]

inkomsten = [220, 430, 125, 160, 205, 90, 345]

print(laag_en_hoog(inkomsten))

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
#    return totaal / aantal #opdracht 9
    gemiddelde_inkomsten = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

inkomsten_van_deze_week = [220, 430, 125, 160, 205, 90, 345]
#print(gemiddelde(inkomsten_van_deze_week)) #---> Opdracht 9
print(gemiddelde(inkomsten_van_deze_week))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst = [10,5,3,2,1,2,9]
print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    laagste, hoogste = korte_lijst
    resultaat = mijn_functie_2(laagste, hoogste)
    return resultaat

invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]
print(combinatie(invoer_lijst_2))