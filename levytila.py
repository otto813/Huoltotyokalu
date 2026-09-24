import shutil

def tarkista_levytila():
    try:
        total, used, free = shutil.disk_usage("C:\\")

        vapaa = free // (1024 ** 3)
        kaytetty = used // (1024 ** 3)

        print(f"Vapaata levytilaa: {vapaa} GiB")
        print(f"Käytettyä levytilaa: {kaytetty} GiB")

        return vapaa, kaytetty

    except Exception as e:
        print(f"Virhe levytilan tarkistuksessa: {e}")
        return None, None