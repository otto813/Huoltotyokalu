import platform

def nayta_tiedot():
    try:
        kayttojarjestelma = platform.system()
        versio = platform.version()
        suoritin = platform.processor()
        tietokone = platform.node()

        print("\n=== Järjestelmätiedot ===")
        print(f"Käyttöjärjestelmä: {kayttojarjestelma}")
        print(f"Versio: {versio}")
        print(f"Suoritin: {suoritin}")
        print(f"Tietokoneen nimi: {tietokone}")

        return kayttojarjestelma, versio, suoritin, tietokone

    except Exception as e:
        print(f"Virhe järjestelmätietojen haussa: {e}")
        return None, None, None, None