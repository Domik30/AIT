

def pozdrav():
    jmeno = input("Zadejte své jméno: ")
    print("Ahoj", jmeno)

def porovnani_zlomku():
    citatel = int(input("Zadejte čitatel: "))
    jmenovatel = int(input("Zadejte jmenovatel: "))
    
    if citatel > jmenovatel:
        print("větší než 1")
    elif jmenovatel > citatel:
        print("menší než 1")

def delitelne_deseti():
    cislo = int(input("Zadejte číslo: "))
    
    if cislo % 10 == 0:
        print("Číslo", cislo, "je dělitelné 10.")
    else:
        print("Číslo", cislo, "není dělitelné 10.")

def  vypis_cisel():
    prvniCislo = int(input("Zadejte první číslo"))
    druheCislo = int(input("Zadejte druhé číslo"))
    for i in range(prvniCislo,druheCislo,1):
        print(i)    

def soucet_kladnych():
    soucet = 0
    x = int(input("Zadejte číslo "))
    for i in range(1, x):
        cislo = int(input("Zadejte číslo "))
        if cislo == 0:
            break
        elif cislo > 0:
            soucet += cislo
    
    print("Součet kladných čísel je:", soucet)

def pricitani():
        for i in range(1, 10):
            x = "1"
            for j in range(1,i):
                x += "0"
            print(x)

                


def main():
    print("Vyberte úlohu:")
    print("1: Pozdrav")
    print("2: Porovnání zlomku")
    print("3: Dělitelnost 10")
    print("4: Výpis čísel od X do Y")
    print("5: Součet kladných čísel")
    print("6: vypsání čísel  1 12 123")
    
    volba = int(input("Zadejte číslo úlohy: "))
    
    if (volba == 1):
        pozdrav()
    elif (volba == 2):
        porovnani_zlomku()
    elif (volba == 3):
        delitelne_deseti()
    elif (volba == 4):
        vypis_cisel()
    elif (volba == 5):
        soucet_kladnych()
    elif (volba == 6):
        pricitani()
    else:
        print("Neplatná volba, zkuste to znovu.")
    
main()

