import subprocess

def tarkista_palvelut():
    try:
        palvelut = ["Spooler", "wuauserv", "BITS"]
        tulokset = []

        print("\n=== Palveluiden tila ===")

        for palvelu in palvelut:
            tulos = subprocess.run(
                ["sc", "query", palvelu],
                capture_output=True,
                text=True
            )

            if "RUNNING" in tulos.stdout:
                tila = "Käynnissä"
            elif "STOPPED" in tulos.stdout:
                tila = "Pysäytetty"
            else:
                tila = "Tilaa ei voitu selvittää"

            print(f"{palvelu}: {tila}")
            tulokset.append((palvelu, tila))

        return tulokset

    except Exception as e:
        print(f"Virhe palveluiden tarkistuksessa: {e}")
        return []