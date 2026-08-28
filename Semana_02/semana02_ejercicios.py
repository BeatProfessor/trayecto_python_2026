from pathlib import Path
from collections import Counter, defaultdict

def list_comprehension():
    nombres = ["Wandering.mp3", "KALYPSO.MP3", "Aphelion.wav"]
    # normalizados = []
    # for n in nombres:
    #     normalizados.append(n.lower())
    #
    # print(normalizados)

    normalizados_v2 = [n.lower() for n in nombres]
    print(normalizados_v2)

def list_comprehension_2():
    pesos_bytes = [9_800_000, 45_000_000, 1_200, 11_200_000, 890]
    # pesos_grandes_mb = []
    # for p in pesos_bytes:
    #     if p > 1_000_000:
    #         pesos_grandes_mb.append(round(p / 1024 / 1024, 1))

    pesos_grandes_mb_v2 = [round(p / 1024 / 1024, 1) for p in pesos_bytes if p > 1_000_000]

    print(pesos_grandes_mb_v2)

def set_comprehension():
    rutas = ["E:/A/t1.wav", "E:/B/t2.mp3", "E:/C/t3.WAV", "E:/D/t4.flac"]
    # extensiones = set()
    # for r in rutas:
    #     extensiones.add(r[r.rfind("."):].lower())

    extensiones_v2 = {r[r.rfind("."):].lower() for r in rutas}
    print(extensiones_v2)

# list_comprehension()
# list_comprehension_2()
# set_comprehension()


