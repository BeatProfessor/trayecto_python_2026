from pathlib import Path

#--------------------EJERCICIO 1--------------------
#
# Sobre una de tus carpetas de música, construye el diccionario conteo con la lógica del if ext in conteo.
# Imprime cuántos archivos hay de cada extensión.

def ejercicio_1():
    carpeta = Path("E:/BP_COLLECTION/MUSIC/VARIAS 312224")
    conteo = {}
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            ext = archivo.suffix
            if ext in conteo:
                conteo[ext] += 1
            else:
                conteo[ext] = 1
        elif archivo.is_dir():
            ext = "Directorio"
            if ext in conteo:
                conteo[ext] += 1
            else:
                conteo[ext] = 1

    for ext, cantidad in conteo.items():
        print(f"Tipo {ext}: {cantidad} elementos")


#--------------------EJERCICIO 2--------------------
#
# Al final, además del desglose por extensión, imprime el total de archivos contados.
# (Pista: puedes ir sumando en una variable aparte, o sumar los valores del diccionario al final.)

def ejercicio_2():
    carpeta = Path("E:/BP_COLLECTION/MUSIC/VARIAS 312224")
    conteo = {}
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            ext = archivo.suffix
            if ext in conteo:
                conteo[ext] += 1
            else:
                conteo[ext] = 1
        elif archivo.is_dir():
            ext = "Directorio"
            if ext in conteo:
                conteo[ext] += 1
            else:
                conteo[ext] = 1

    for ext, cantidad in conteo.items():
        print(f"Tipo {ext}: {cantidad} elementos")

    print("----------------------------------------")
    total_elementos = sum(conteo.values())
    print(f"Total de elementos: {total_elementos}")


#--------------------EJERCICIO 3--------------------
#
# En vez de contar cuántos, suma los bytes de cada extensión.
# O sea, un diccionario {".mp3": 4500000000, ".wav": ...}.
# Es la misma lógica, pero en lugar de + 1 le sumas archivo.stat().st_size. Junta lo del miércoles con lo que ya hiciste ayer.

def ejercicio_3():
    carpeta = Path("E:/BP_COLLECTION/MUSIC/VARIAS 312224")
    conteo = {}

    for archivo in carpeta.iterdir():
        if archivo.is_file():
            ext = archivo.suffix
            tamano = archivo.stat().st_size
        elif archivo.is_dir():
            ext = "Directorio"
            tamano = 0
        else:
            continue

        if ext in conteo:
            conteo[ext]["elementos"] += 1
            conteo[ext]["peso"] += tamano
        else:
            conteo[ext] = {
            "elementos": 1,
            "peso": tamano
        }

    for ext, info in conteo.items():
        print(f"Tipo {ext}: {info['elementos']} elementos, {round(info['peso'] / 1024 / 1024 / 1024, 1)} GB")

    print("----------------------------------------")


# ejercicio_1()
# ejercicio_2()
ejercicio_3()