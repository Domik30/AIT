def scitani(prvniCislo, druheCislo):
    return prvniCislo + druheCislo

def odcitani(prvniCislo, druheCislo):
    return prvniCislo - druheCislo

def kalkulacka(prvniCsilo, druheCislo, operace):
    if (operace == "scitani"):
        print(scitani(prvniCislo, druheCislo))
    elif (operace == "odcitani"):
        print(odcitani(prvniCislo, druheCislo))
    
prvniCislo = int(input("Zadejte první číslo"))
druheCislo = int(input("Zadejte druhé číslo"))
operace = input("zadejte operaci")

kalkulacka(prvniCislo, druheCislo, operace)