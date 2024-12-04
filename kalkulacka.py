print("Vítejte v mé kalkulačce")

prvniCislo = int(input("Zadejte první číslo"))
druheCislo = int(input("Zadejte druhé číslo"))
operace = int(input("Zadejte operace (1 scitani, 2 odcitani, 3 nasobeni, 4 deleni)\n"))

if (operace == 1):
    vysledek = prvniCislo + druheCislo
elif (operace == 2):
    vysledek = prvniCislo - druheCislo
elif (operace == 3):
    vysledek = prvniCislo * druheCislo
else:
    vysledek = prvniCislo / druheCislo

    print("výsledek je")
    print(vysledek)