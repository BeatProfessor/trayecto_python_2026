from pathlib import Path

#--------------------EJERCICIO 1--------------------
#
# Elige una carpeta real y con pocos archivos de tu PC (mejor una chica para probar,
# no tu librería de 600 GB todavía). Crea su Path y recórrela con .iterdir(),
# imprimiendo cada elemento.

def ejercicio_1():
    carpeta = Path("E:/BP_COLLECTION/MUSIC/DJCITY")
    for archivo in carpeta.iterdir():
        print(archivo)

#--------------------EJERCICIO 2--------------------
#
# Sobre esa misma carpeta, recórrela y usa .is_file() para imprimir "Archivo:" o "Carpeta:"
# antes de cada elemento.

def ejercicio_2():
    archivos = 0
    carpetas = 0
    carpeta = Path("E:/BP_COLLECTION/MUSIC/VARIAS 312224")
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            print("Archivo:", archivo)
            archivos += 1
        elif archivo.is_dir():
            print("Carpeta:", archivo)
            carpetas += 1

    print(f"Total de archivos: {archivos}")
    print(f"Total de carpetas: {carpetas}")


#--------------------EJERCICIO 3--------------------
#
# Recórrela otra vez y, solo para los archivos, imprime el .name y su tamaño
# en bytes con .stat().st_size.

def ejercicio_3():
    archivos = 0
    tamano = 0
    carpetas = 0
    carpeta = Path("E:/BP_COLLECTION/MUSIC/VARIAS 312224")
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            peso = archivo.stat().st_size
            print("Archivo:", archivo.name, " - ", round(peso / 1024 / 1024, 1), "MB")
            archivos += 1
            tamano += peso
        elif archivo.is_dir():
            print("Carpeta:", archivo)
            carpetas += 1

    print("----------------------------------------")
    print(f"Total de archivos: {archivos}")
    print(f"Total de carpetas: {carpetas}")
    print("----------------------------------------")
    print(f"Total de elementos: {archivos + carpetas}")
    print("----------------------------------------")
    print(f"Tamaño estimado de la carpeta: {round(tamano / 1024 / 1024 / 1024, 1)} GB")

# ejercicio_1()
# ejercicio_2()
# ejercicio_3()