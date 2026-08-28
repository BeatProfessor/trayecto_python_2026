from pathlib import Path
import time

#--------------------EJERCICIOS LUNES--------------------
#
#--------------------EJERCICIO NO. 1---------------------
# PARTE A:
# Convierte la lista en un set con set().
# Imprime cuántos elementos tiene la lista original (len() de la lista).
# Imprime cuántos elementos tiene el set (len() del set).
# Imprime cuántos duplicados se eliminaron (la resta de los dos números anteriores).

# DATOS EJ. 1--------------------------------------------
descargas = [
    "Adiel - Wandering.mp3",
    "Kalypso.mp3",
    "adiel - wandering.MP3",
    "Aphelion.wav",
    "Kalypso.mp3",
    "Closer.mp3",
    "APHELION.wav",
]

# DATOS EJ. 2---------------------------------------------
kingston = {"Wandering.mp3", "Kalypso.mp3", "Aphelion.wav", "Closer.mp3"}
respaldo = {"Wandering.mp3", "Closer.mp3", "Nocturne.mp3"}

# DATOS EJ. 3---------------------------------------------
archivos = [
    ("Wandering.mp3", 9_800_000),
    ("Kalypso.mp3", 11_200_000),
    ("wandering.mp3", 9_800_000),
    ("Kalypso.mp3", 4_100_000),
]

def ejercicio_1_a():
    set_descargas = set(descargas)
    elementos_list_descargas = len(descargas)
    elementos_set_descargas = len(set_descargas)
    elementos_duplicados = elementos_list_descargas - elementos_set_descargas
    print(f"Elementos en la lista original: {elementos_list_descargas}")
    print(f"Elementos en el set creado: {elementos_set_descargas}")
    print(f"Elementos duplicados eliminados: {elementos_duplicados}")

# PARTE B:
#
# 1. Construye una lista nueva donde cada nombre esté pasado por .lower().
# Con lo que ya sabes, esto se hace con un bucle for y .append():
# 2. Convierte esa lista nueva en un set.
# 3. Imprime los mismos tres números que en la parte A.

def ejercicio_1_b():
    descargas_sin_mayusc = []
    for nombre in descargas:
        descargas_sin_mayusc.append(nombre.lower())

    set_descargas_sin_mayusc = set(descargas_sin_mayusc)

    elementos_list_normalizada = len(descargas_sin_mayusc)
    elementos_set_normalizado = len(set_descargas_sin_mayusc)
    elementos_duplicados_normalizado = elementos_list_normalizada - elementos_set_normalizado

    print(f"Elementos en la lista original: {elementos_list_normalizada}")
    print(f"Elementos en el set creado: {elementos_set_normalizado}")
    print(f"Elementos duplicados eliminados: {elementos_duplicados_normalizado}")

    print(descargas_sin_mayusc)
    print(set_descargas_sin_mayusc)


#--------------------EJERCICIO NO. 2---------------------
#
# Imprime, con un mensaje descriptivo cada uno (usa f-strings):
#
# Los tracks que están en la Kingston pero NO en el respaldo
# (es decir: lo que perderías si la Kingston muriera hoy). Operador: -.
# Los tracks que están en ambos lados (lo que ya está a salvo). Operador: &.
# Los tracks que están en el respaldo pero ya NO en la Kingston
# (archivos que borraste de la Kingston pero siguen ocupando espacio
# en el respaldo). Operador: - en la dirección contraria.
# El catálogo completo: todos los nombres que existen en algún lado,
# sin repetir. Operador: |.
# Además de imprimir los sets, imprime len() de cada resultado,
# con un mensaje tipo: "Tracks sin respaldar: 2".

def ejercicio_2():
    sin_respaldo = kingston - respaldo
    kingston_respaldo = kingston & respaldo
    sin_kingston = respaldo - kingston
    todos_tracks = kingston | respaldo
    print(f"Tracks en kingston pero no en respaldo: {sin_respaldo} Cantidad: {len(sin_respaldo)}")
    print(f"Tracks que están en kingston y respaldo: {kingston_respaldo} Cantidad: {len(kingston_respaldo)}")
    print(f"Tracks en respaldo pero no en kingston: {sin_kingston} Cantidad: {len(sin_kingston)}")
    print(f"Tracks en ambos lados: {todos_tracks} Cantidad: {len(todos_tracks)}")


#--------------------EJERCICIO NO. 3---------------------
#
# 1. Crea un set vacío llamado firmas (con set(), no con {}).
# 2. Crea una lista vacía llamada sospechosos.
# 3. Recorre la lista archivos con un for. En cada vuelta desempaqueta la tupla:
# 4. Dentro del bucle, construye la firma: una tupla (nombre.lower(), tamano).
# 5. Pregunta si esa firma ya está en el set firmas:
#    Si ya está → este archivo es un duplicado sospechoso: agrégalo a sospechosos.
#    Si no está → agrégala al set con .add().
# 6. Al final imprime: cuántos archivos se revisaron, cuántas firmas únicas
#    quedaron, y la lista de sospechosos.

def ejercicio_3():
    firmas = set()
    sospechosos = []

    for archivo in archivos:
        nombre, tamano = archivo
        firma = (nombre.lower(), tamano)
        if firma in firmas:
            sospechosos.append(archivo)
        else:
            firmas.add(firma)

    print(f"Archivos revisados: {len(archivos)}")
    print(f"Firmas únicas: {len(firmas)}")
    print(f"Archivos sospechosos: {len(sospechosos)}")
    print(f"Sospechosos: {sospechosos}")


#--------------------EJERCICIO NO. 4---------------------
#
# Alcance: elige UNA subcarpeta de tu música en la Kingston (por ejemplo un género o un año), no el disco completo.
# Algo de unos cuantos miles de archivos como máximo, para que las pruebas sean rápidas.
# El disco completo lo tocaremos el viernes.
#
# Qué debe hacer el programa:
#
# 1. Definir la ruta directamente en el código con Path("E:/...") — sin Tkinter esta vez. Decidimos no profundizar ahí,
#    y para un script de análisis basta con escribir la ruta.
# 2. Validar que la ruta existe y es carpeta (como en la semana 1: .exists() y .is_dir()).
# 3. Recorrer recursivamente con .rglob("*"), considerando solo archivos (.is_file()).
# 4. Por cada archivo, tomar archivo.name.lower() como nombre normalizado.
# 5. Detectar qué nombres aparecen más de una vez (en la misma carpeta no puede haber dos archivos con el mismo nombre,
#    así que si un nombre se repite, está en carpetas distintas).
# 6. Al final imprimir: total de archivos revisados, cuántos nombres están repetidos, y por cada nombre repetido, en qué
#    rutas está.


# def ejercicio_4():
    # VERSION 1---------------------------------------------------------------------------------------------------------
    # set_all_songs = set()
    # set_repeated_songs = set()
    # set_all_names = set()
    # set_repeated_names = set()
    # songs_repeated = 0
    # songs_total = 0
    #
    # carpeta = Path("E:/BP_COLLECTION/MUSIC/")
    #
    # try:
    #     if carpeta.exists() and carpeta.is_dir():
    #         for archivo in carpeta.rglob("*"):
    #             if archivo.is_file():
    #                 songs_total += 1
    #                 song_name = archivo.name.lower()
    #                 if song_name in set_all_names:
    #                     set_repeated_names.add(song_name)
    #                     firma = (song_name, archivo.parent, "DUPLICADO")
    #                     set_repeated_songs.add(firma)
    #                     songs_repeated += 1
    #                 else:
    #                     set_all_names.add(song_name)
    #                     firma = (song_name, archivo.parent, "ORIGINAL")
    #                     set_all_songs.add(firma)
    # except (OSError, PermissionError) as e:
    #     print(f"Error al acceder a la carpeta: {e}")
    #
    # sorted_set_all_songs = sorted(set_all_songs, key=lambda x: x[0])
    # sorted_set_repeated_songs = sorted(set_repeated_songs, key=lambda x: x[0])
    # sorted_set_all_names = sorted(set_all_names)
    # sorted_set_repeated_names = sorted(set_repeated_names)
    # print(f"Total de archivos revisados: {songs_total}")
    # print(f"Total de archivos únicos: {len(set_all_songs)}")
    # print(f"Total de archivos repetidos: {songs_repeated}")
    # print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #
    # i = 0
    # for song in sorted_set_all_names:
    #     if song in sorted_set_repeated_names:
    #         for song_original, path_original, status_original in sorted_set_all_songs:
    #             if song == song_original:
    #                 print(f"✅. Cancion original: {song_original} en {path_original}, {status_original}")
    #                 for song_repeated, path_repeated, status_repeated in sorted_set_repeated_songs:
    #                     if song == song_repeated:
    #                         i += 1
    #                         print(f"❌ {i}. Cancion duplicada: {song_repeated} en {path_repeated}, {status_repeated}")
    #                 print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


    # VERSION 2---------------------------------------------------------------------------------------------------------

def ejercicio_4_v2():
    carpeta = Path("E:/BP_COLLECTION/MUSIC/")

    if not carpeta.exists() or not carpeta.is_dir():
        print(f"La ruta no existe o no es una carpeta: {carpeta}")
        return

    ubicaciones = {}      # nombre normalizado → lista de rutas
    songs_total = 0

    try:
        for archivo in carpeta.rglob("*"):
            if archivo.is_file():
                songs_total += 1
                nombre = archivo.name.lower()
                if nombre in ubicaciones:
                    ubicaciones[nombre].append(archivo)
                else:
                    ubicaciones[nombre] = [archivo]
    except (OSError, PermissionError) as e:
        print(f"Error al acceder a la carpeta: {e}")

    # Resumen primero
    print(f"Total de archivos revisados: {songs_total}")
    print(f"Nombres distintos: {len(ubicaciones)}")
    print(f"Copias extra: {songs_total - len(ubicaciones)}")
    print("-" * 60)

    # Detalle después
    for nombre, rutas in sorted(ubicaciones.items()):
        if len(rutas) > 1:
            print(f"'{nombre}' aparece en {len(rutas)} lugares:")
            for ruta in rutas:
                print(f"   {ruta.parent}")

#--------------------EJERCICIO NO. 5---------------------
#
# 1. Revisa el código del ejercicio_5()
# 2. Corre el programa con CANTIDAD = 200_000. Anota los tres números de la salida.
# 3. Cambia a CANTIDAD = 400_000 y corre otra vez. Anota los tres números.
# 4. Reflexiona sobre el tiempo que le lleva al codigo realizar lo que se pide.

def ejercicio_5():
    cantidad = 400_000
    busquedas = 1_000

    # Construir una librería falsa de nombres de tracks
    tracks_lista = [f"Track_{i:06d}.mp3" for i in range(cantidad)]
    tracks_set = set(tracks_lista)

    # Los 1,000 nombres a buscar: los últimos de la lista (el peor caso para la lista)
    a_buscar = [f"Track_{i:06d}.mp3" for i in range(cantidad - busquedas, cantidad)]

    # --- Medición con LISTA ---
    inicio = time.perf_counter()
    for nombre in a_buscar:
        encontrado = nombre in tracks_lista
    fin = time.perf_counter()
    tiempo_lista = fin - inicio

    # --- Medición con SET ---
    inicio = time.perf_counter()
    for nombre in a_buscar:
        encontrado = nombre in tracks_set
    fin = time.perf_counter()
    tiempo_set = fin - inicio

    print(f"Lista: {tiempo_lista:.6f} segundos")
    print(f"Set:   {tiempo_set:.6f} segundos")
    print(f"El set fue {tiempo_lista / tiempo_set:,.0f} veces más rápido")


# ejercicio_1_a()
# ejercicio_1_b()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
ejercicio_4_v2()
# ejercicio_5()