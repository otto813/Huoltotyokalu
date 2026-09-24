from datetime import datetime
import levytila
import jarjestelma
import palvelut

def luo_raportti():
    try:
        aika = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        vapaa, kaytetty = levytila.tarkista_levytila()

        kayttojarjestelma, versio, suoritin, tietokone = jarjestelma.nayta_tiedot()

        palveluiden_tiedot = palvelut.tarkista_palvelut()

        with open("raportti.txt", "a", encoding="utf-8") as tiedosto:
            tiedosto.write("=== Huoltotyökalun raportti ===\n")
            tiedosto.write(f"Aika: {aika}\n\n")

            tiedosto.write("Levytila:\n")
            tiedosto.write(f"Vapaata levytilaa: {vapaa} GiB\n")
            tiedosto.write(f"Käytettyä levytilaa: {kaytetty} GiB\n\n")

            tiedosto.write("Järjestelmätiedot:\n")
            tiedosto.write(f"Käyttöjärjestelmä: {kayttojarjestelma}\n")
            tiedosto.write(f"Versio: {versio}\n")
            tiedosto.write(f"Suoritin: {suoritin}\n")
            tiedosto.write(f"Tietokoneen nimi: {tietokone}\n\n")

            tiedosto.write("Palveluiden tila:\n")

            for palvelu, tila in palveluiden_tiedot:
                tiedosto.write(f"{palvelu}: {tila}\n")

            tiedosto.write("\n")

        print("Raportti luotu onnistuneesti.")

    except Exception as e:
        print(f"Virhe raportin luonnissa: {e}")