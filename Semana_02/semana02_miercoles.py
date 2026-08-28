from pathlib import Path
from collections import Counter, defaultdict

from unicodedata import numeric


# List comprehensions y Collections

# List comprehensions

def list_comprehension():
    print("Ejemplo de list comprehensions")
    descargas_normalizadas = []
    descargas = ["Kalypso.mp3", "Kalypso.mp3", "Kalypso.mp3"]
    for nombre in descargas:
        descargas_normalizadas.append(nombre.lower())
    print(descargas_normalizadas)

    descargas_nomalizadas_comprehension = [nombre.lower() for nombre in descargas]
    print(descargas_nomalizadas_comprehension)

# Set comprehensions

def set_comprehension():
    print("Ejemplo de set comprehensions")
    extensiones = set()
    carpeta = Path("C:/Users/uhias/Music")
    for archivo in carpeta.rglob("*"):
        if archivo.is_file():
            extensiones.add(archivo.suffix.lower())

    for ext in extensiones:
        print(ext)

    extensiones_comprehension = {archivo.suffix.lower() for archivo in carpeta.rglob("*") if archivo.is_file()}
    for ext in extensiones_comprehension:
        print(ext)

    conteo = sum(Counter(extensiones_comprehension).values())
    print(conteo)

# Dict comprehensions

def dict_comprehension():
    print("Ejemplo de dict comprehensions")
    descargas = ["Kalypso.mp3", "juanito.mp3", "Kripton.mp3"]
    descargas_normalizadas = {nombre: nombre.lower() for nombre in descargas}
    print(descargas_normalizadas)

    descargas_normalizadas_comprehension = {nombre: nombre.lower() for nombre in descargas if nombre != "Kalypso.mp3"}
    print(descargas_normalizadas_comprehension)

# Counter

def contador():
    print("Ejemplo de Counter")
    palabras = ["Kalypso", "Kalypso", "perrito", "Kalypso", "Kalypso", "Kalypso", "Kalypso", "Kalypso", "Kalypso", "Kalypso", "perrito", "perrito", "perrito", "perrito", "perrito", "perrito", "perrito", "perrito", "perrito", "perrito"]
    conteo = Counter(palabras)
    print(conteo)

# defaultdict

def default_dict():
    print("Ejemplo de defaultdict")
    carpeta = Path("C:/Users/uhias/Music")
    conteo = defaultdict(list)
    for archivo in carpeta.rglob("*"):
        if archivo.is_file():
            extensiones = archivo.suffix.lower()
            conteo[extensiones].append(archivo)
    print(conteo)

def ejercicio_2():
    # Ejercicio 2: Hacer conteo de archivos de una carpeta con comprehension
    # Establecer la carpeta a analizar
    carpeta = Path("E:/BP_COLLECTION/MUSIC/")

    # Verificar que exista y que sea una carpeta
    if not carpeta.exists() or not carpeta.is_dir():
        print("La carpeta no existe o no es una carpeta")
        return

    # Hacer un conteo por extension e imprimirlo
    conteo = Counter(a.suffix.lower() for a in carpeta.rglob("*") if a.is_file())

    print(f"Analisis de la carpeta {carpeta}:")
    print("------------------------------------")



    # Mostrar el top 5 de extensiones mas comunes
    print("Archivos mas comunes por extensión:")

    for ext, cantidad in conteo.most_common(5):
        print(f"Extension: {ext}, Cantidad: {cantidad:,} archivos")

    print("------------------------------------")
    # Imprimir los tipos de archivos que hay
    print(f"Tipos de archivos distintos: {len(conteo)}")
    print("------------------------------------")

    # Imprimir el total de archivos
    print(f"Total de archivos: {conteo.total():,}")
    print("------------------------------------")

def ejercicio_3():

    carpeta = Path("E:/BP_COLLECTION/MUSIC/")

    if not carpeta.exists() or not carpeta.is_dir():
        print(f"La ruta no existe o no es una carpeta: {carpeta}")
        return

    ubicaciones = defaultdict(list)
    songs_total = 0

    try:
        for archivo in carpeta.rglob("*"):
            if archivo.is_file():
                songs_total += 1
                nombre = archivo.name.lower()
                ubicaciones[nombre].append(archivo)
    except (OSError, PermissionError) as e:
        print(f"Error al acceder a la carpeta: {e}")

    # Resumen primero
    print(f"Total de archivos revisados: {songs_total:,}")
    print(f"Nombres distintos: {len(ubicaciones):,}")
    print(f"Copias extra: {songs_total - len(ubicaciones)}")
    print("-" * 60)

    # Detalle después
    for nombre, rutas in sorted(ubicaciones.items()):
        if len(rutas) > 1:
            print(f"'{nombre}' aparece en {len(rutas)} lugares:")
            for ruta in rutas:
                print(f"   {ruta.parent}")


def formato_peso(bytes_):
    """Convierte bytes a texto legible: elige KB, MB, GB o TB según el tamaño."""
    if bytes_ < 1024:
        return f"{round(bytes_,2):,} bytes"
    elif 1024 <= bytes_ < 1024**2:
        return f"{bytes_ / 1024:,.2f} KB"
    elif 1024 ** 2 <= bytes_ < 1024**3:
        return f"{bytes_ / 1024**2:,.2f} MB"
    elif 1024 ** 3 <= bytes_ < 1024**4:
        return f"{bytes_ / 1024**3:,.2f} GB"
    elif bytes_ == 0:
        return "0 bytes"
    else:
        return f"{bytes_ / 1024**4:,.2f} TB"


#list_comprehension()
#set_comprehension()
#dict_comprehension()
#contador()
#default_dict()
#ejercicio_2()
#ejercicio_3()

print(formato_peso(512))              # bytes chicos → KB
print(formato_peso(1_048_576))        # exactamente 1 MB → tu caso frontera
print(formato_peso(9_800_000))        # un track wav típico → MB
print(formato_peso(45_000_000_000))   # una colección → GB
print(formato_peso(0))                # cero → no debe romperse
print(formato_peso(1_073_741_824))
print(formato_peso(1_699_000_000_000))



