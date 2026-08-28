
#---------------------------------------EJEMPLOS PARA COMPRENDER CONCEPTOS MARTES---------------------------------------

# import time
import timeit

# print(time.time())
# print(time.localtime())

# inicio = time.perf_counter()
# #... el codigo que se va a medir
# for i in range(100000000):
#     i * i + 1
# fin = time.perf_counter()
# duracion = fin - inicio
#
# print(f"Tardó {duracion:.6f} segundos")

# MAL: mide el cálculo + la impresión

# a_buscar = [f"Track_{i:06d}.mp3" for i in range(1000000)]
# tracks_set = set(a_buscar)
#
# inicio = time.perf_counter()
# for nombre in a_buscar:
#     resultado = nombre in tracks_set
#     print(resultado)                    # ← esto domina la medición
# fin = time.perf_counter()
#
# # BIEN: mide solo el cálculo, imprime después
# inicio = time.perf_counter()
# for nombre in a_buscar:
#     resultado = nombre in tracks_set
# fin = time.perf_counter()
# print(f"Tardó {fin - inicio:.6f} s")


# resultados = timeit.repeat(
#     stmt="'Track_199999.mp3' in tracks_set",       # el código a medir, como TEXTO
#     setup="""
# tracks_lista = [f"Track_{i:06d}.mp3" for i in range(200_000)]
# tracks_set = set(tracks_lista)
# """,                                                # preparación, NO se mide
#     repeat=5,                                       # 5 rondas de medición
#     number=1_000                                    # 1,000 ejecuciones por ronda
# )
#
# print(resultados)                # lista con 5 números: el total de cada ronda
# print(min(resultados) / 1_000)   # el mejor tiempo promedio por ejecución
#----------------------------------------------HASTA AQUI LLEGAN EJEMPLOS-----------------------------------------------

import time
import random

# ---------- Generador de datos sintéticos ----------

def generar_archivos(cantidad, porcentaje_duplicados=0.12):
    """Genera tuplas (nombre, carpeta) simulando una librería musical.
    porcentaje_duplicados: fracción de archivos que repiten nombre (12% como tu subcarpeta real)."""
    unicos = int(cantidad * (1 - porcentaje_duplicados))
    archivos = []

    for i in range(unicos):
        archivos.append((f"track_{i:06d}.wav", f"E:/CARPETA_{i % 20}"))

    # Los duplicados: nombres ya usados, en otra carpeta
    for i in range(cantidad - unicos):
        nombre_repetido = f"track_{i:06d}.wav"          # repite los primeros nombres
        archivos.append((nombre_repetido, f"E:/CARPETA_{(i + 7) % 20}"))

    random.shuffle(archivos)      # desordenar, como en un disco real
    return archivos

# ---------- Tu v1: sets + bucles anidados (solo la parte del reporte) ----------

def reporte_v1(archivos):
    set_all_names = set()
    set_repeated_names = set()
    set_all_songs = set()
    set_repeated_songs = set()

    # Fase de detección (igual que tu v1)
    for nombre, carpeta in archivos:
        if nombre in set_all_names:
            set_repeated_names.add(nombre)
            set_repeated_songs.add((nombre, carpeta))
        else:
            set_all_names.add(nombre)
            set_all_songs.add((nombre, carpeta))

    # Fase de reporte (igual que tu v1: la parte O(n²))
    lineas = []
    sorted_all_names = sorted(set_all_names)
    sorted_repeated_names = sorted(set_repeated_names)
    sorted_all_songs = sorted(set_all_songs, key=lambda x: x[0])
    sorted_repeated_songs = sorted(set_repeated_songs, key=lambda x: x[0])

    for song in sorted_all_names:
        if song in sorted_repeated_names:                      # in sobre LISTA: O(n)
            for nombre_o, carpeta_o in sorted_all_songs:       # bucle anidado
                if song == nombre_o:
                    lineas.append(f"original: {nombre_o} en {carpeta_o}")
                    for nombre_r, carpeta_r in sorted_repeated_songs:
                        if song == nombre_r:
                            lineas.append(f"duplicado: {nombre_r} en {carpeta_r}")
    return lineas

# ---------- Tu v2: diccionario de listas ----------

def reporte_v2(archivos):
    ubicaciones = {}

    for nombre, carpeta in archivos:
        if nombre in ubicaciones:
            ubicaciones[nombre].append(carpeta)
        else:
            ubicaciones[nombre] = [carpeta]

    lineas = []
    for nombre, carpetas in sorted(ubicaciones.items()):
        if len(carpetas) > 1:
            lineas.append(f"'{nombre}' aparece en {len(carpetas)} lugares:")
            for carpeta in carpetas:
                lineas.append(f"   {carpeta}")
    return lineas

# ---------- El experimento ----------

def medir(funcion, archivos, rondas=3):
    """Ejecuta la función varias rondas y devuelve el mejor tiempo."""
    tiempos = []
    for _ in range(rondas):
        inicio = time.perf_counter()
        funcion(archivos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return min(tiempos)

def experimento():
    print(f"{'n':>8} | {'v1 (seg)':>12} | {'v2 (seg)':>12} | {'v1/v2':>10}")
    print("-" * 52)

    for cantidad in [1_000, 2_000, 4_000, 8_000]:
        archivos = generar_archivos(cantidad)
        t1 = medir(reporte_v1, archivos)
        t2 = medir(reporte_v2, archivos)
        print(f"{cantidad:>8} | {t1:>12.6f} | {t2:>12.6f} | {t1 / t2:>10.1f}")

# experimento()

def costo_tiempo():
    resultados = timeit.repeat(
        stmt="'track_099999.wav' in tracks_set",       # el código a medir, como TEXTO
        setup="""
tracks = [f"track_{i:06d}.wav" for i in range(100_000)]
tracks_set = set(tracks)
    """,                                                # preparación, NO se mide
        repeat=5,                                       # 5 rondas de medición
        number=1_000                                    # 1,000 ejecuciones por ronda
    )

    print(resultados)                # lista con 5 números: el total de cada ronda
    print(min(resultados) / 1_000)   # el mejor tiempo promedio por ejecución

costo_tiempo()