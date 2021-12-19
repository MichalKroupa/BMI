# Projekt na výpočet BMI
print("Vitejte u vypoctu BMI")

# Funkce, která kontroluje, zda byla váha zadána správně (zda se jedná o číslo)
def kontrola_vahy():
    while True:
        vaha = input("Zadejte prosim Vasi vahu v kg\n")
        # Zkouška, zda je input opravdu číslo, nebo je ve správném formátu
        try:
            return float(vaha)
        # Pokud není, vyhodí Error a uživatel zadává znovu
        except ValueError:
            print("Nezadal jste cislo")

# Funkce, která kontroluje, zda byla výška zadána správně (zda se jedná o číslo)
def kontrola_vysky():
    while True:

        vyska = input("Zadejte prosim Vasi vysku v m (viz 1,5)\n")
        if ',' in vyska:
            vyska = vyska.replace(",", ".")

        try:
            return float(vyska)

        except ValueError:
            print("Nezadal jsi cislo")

# přiřazení hodnot
vaha = kontrola_vahy()
vyska = kontrola_vysky()

# výpočet BMI se zaokrouhlením na 2 desetinná místa
BMI = (vaha /  (vyska * vyska))
BMI = round(BMI, 2)

print("Vase BMI je:", BMI)
# výsledek BMI podle indexu
if BMI < 16.5:
    print("To je tezka podvyziva")
elif BMI < 18.5:
    print("To je podvaha")
elif BMI < 25:
    print("To je idealni vaha")
elif BMI < 30:
    print("To je nadvaha")
elif BMI < 35:
    print("To je obezita prvniho stupne")
elif BMI < 40:
    print("To je obezita druheho stupne")
else:
    print("To je težká obezita")

input("Pro ukončení stiskni libovolnou klávesu")