import levytila
import jarjestelma
import palvelut
import raportti

def valikko():
    print("\n=== Huoltotyökalu ===")
    print("1. Tarkista levytila")
    print("2. Näytä järjestelmätiedot")
    print("3. Tarkista palvelut")
    print("4. Luo raportti")
    print("0. Lopeta")

while True:
    valikko()

    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        levytila.tarkista_levytila()

    elif valinta == "2":
        jarjestelma.nayta_tiedot()

    elif valinta == "3":
        palvelut.tarkista_palvelut()

    elif valinta == "4":
        raportti.luo_raportti()

    elif valinta == "0":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")