# Ejercicios correspondientes al lunes de la semana 1.

#----------------EJERCICIO 1---------------------
# Crea una variable llamada artista que guarde tu nombre de DJ ("Beat Professor")
# y otra llamada genero con el texto "Open Format". Luego imprime las dos.

def ejercicio_1():
    artista = "Beat Professor"
    genero = "Open Format"
    print(artista)
    print(genero)


#----------------EJERCICIO 2---------------------
# Crea una lista llamada generos con estos cuatro textos: "house", "reggaeton", "techno", "cumbia". Luego:
#
# Imprime la lista completa.
# Imprime solo el primer género usando su posición.
# Imprime solo el tercero..

def ejercicio_2():
    generos = ["house", "reggaeton", "techno", "cumbia"]
    print(generos)
    print(generos[0])
    print(generos[2])

#----------------EJERCICIO 3----------------------
#
# Usando la misma lista generos, recórrela con un for e imprime cada género, uno por línea.

def ejercicio_3():
    generos = ["house", "reggaeton", "techno", "cumbia"]
    for genero in generos:
        print(genero)


#----------------EJERCICIO 4----------------------
#
# Crea un diccionario llamado bpm con estos tres tracks y sus BPM:
#
# "track_intro" → 124
# "track_drop" → 128
# "track_outro" → 120

def ejercicio_4():
    bpm = {
        "track_intro": 124,
        "track_drop": 128,
        "track_outro": 120
    }

    print(bpm["track_drop"])
    print(bpm.get("track_secreto"))


#---------------EJERCICIO 5----------------------
#
# Usando el diccionario bpm, recórrelo con un for e imprime cada track junto a su BPM, así:

def ejercicio_5():
    bpm = {
        "track_intro": 124,
        "track_drop": 128,
        "track_outro": 120
    }

    for track, beats in bpm.items():
        print(f"{track}: {beats}")


#----------------EJERCICIO 6----------------------
#
# Usando otra vez el diccionario bpm, recórrelo y solo imprime los tracks que tengan más de 122 BPM.
# El resultado debería mostrar únicamente track_intro y track_drop.

def ejercicio_6():
    bpm = {
        "track_intro": 124,
        "track_drop": 128,
        "track_outro": 120
    }
    for track, beats in bpm.items():
        if beats > 122:
            print(f"{track}: {beats}")
# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()
# ejercicio_5()
# ejercicio_6()