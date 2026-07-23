from pathlib import Path
import tkinter as tk
from tkinter import filedialog, ttk


#--------------------PROYECTO FINAL SEMANAL--------------------
#
# Conjuntar todos los ejercicios de la semana para crear un programa que lea todos los archivos
# de una carpeta, imprimirlos en pantalla y contar la cantidad de archivos en un directorio y
# sus subdirectorios.

# Funcion para que el usuario seleccione como quiere ordenar la información a mostrar (por elemento o
# peso).


def criterio_ordenamiento():
    ventana = tk.Tk()
    ventana.title("Selecciona el criterio de ordenamiento")
    ventana.geometry("320x150")
    ventana.attributes("-topmost", True)

    criterio_seleccionado = tk.StringVar(master=ventana, value="elementos")

    resultado = {"criterio": "elementos"}
    def confirmar():
        resultado["criterio"] = criterio_seleccionado.get()
        ventana.destroy()

    etiqueta = tk.Label(ventana, text="Selecciona el criterio de ordenamiento:")
    etiqueta.pack(pady=10)

    combo_orden = ttk.Combobox(
        ventana,
        values=["elementos", "peso"],
        textvariable=criterio_seleccionado,
        state="readonly"
    )
    combo_orden.pack(pady=10)

    boton_confirmar = tk.Button(
        ventana,
        text="Confirmar",
        command=confirmar
    )
    boton_confirmar.pack(pady=10)

    ventana.mainloop()

    return resultado["criterio"]


# Funcion para seleccionar la carpeta a escanear con Tkinter.
def seleccionar_carpeta():
    # 1. Crear una ventana oculta (evita que se abra una ventana vacía de Tkinter).
    root = tk.Tk()
    root.withdraw()

    # 2. Forzar que la ventana esté al frente de todas.
    root.attributes("-topmost", True)

    # 3. Abrir el selector de carpetas.
    carpeta = filedialog.askdirectory(title="Selecciona la carpeta a escanear")

    # 4. Cerrar la ventana.
    root.destroy()
    return carpeta


# Funcion para contar los archivos, rescatando la carpeta seleccionada en seleccionar_carpeta().
def contar_archivos(ruta_carpeta, orden):

# Asignar la ruta con Path y validar si tiene informacion o no para continuar.
    if not ruta_carpeta:
        print("No se seleccionó ninguna carpeta.")
        return

    carpeta = Path(ruta_carpeta)

    if not carpeta.exists() or not carpeta.is_dir():
        print("La ruta seleccionada no es una carpeta válida.")
        return

    print(f"Carpeta seleccionada: {carpeta}")

# Escanear la carpeta y contar archivos por tipo, guardando en diccionario.

    conteo = {}
    errores = 0
    archivos_fallidos = []
    try:
        for archivo in carpeta.rglob("*"):
            if archivo.is_file():
                if archivo.suffix == "":
                    ext = "Sin extensión"
                else:
                    ext = archivo.suffix.lower()
                try:
                    tamano = archivo.stat().st_size
                except (PermissionError, OSError) as e:
                    tamano = 0
                    errores += 1
                    archivos_fallidos.append(archivo.name)
                    if errores <= 5:
                        print(f"No se puede leer {archivo.name}: {e}")
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
    except (PermissionError, OSError) as e:
        print(
            f"No se tienen permisos de lectura para algunos archivos o carpetas: {e}"
        )
    if not conteo:
        print("No se encontraron archivos en la carpeta seleccionada.")
        return

# Muestra los resultados ordenados por cantidad de elementos o peso en GB.

    for ext, info in sorted(conteo.items(), key=lambda x: x[1][orden], reverse=True):
        if ext != "Directorio":
            if 0.99 > info["peso"] / 1024 / 1024 / 1024 > 0.001:
                print(f"Tipo {ext}: {info['elementos']} elementos, {round(info['peso'] / 1024 / 1024, 1)} MB")
            elif info["peso"] / 1024 / 1024 / 1024 < 0.001:
                print(f"Tipo {ext}: {info['elementos']} elementos, {round(info['peso'] / 1024, 2)} KB")
            else:
                print(f"Tipo {ext}: {info['elementos']} elementos, {round(info['peso'] / 1024 / 1024 / 1024, 1)} GB")

    print("----------------------------------------")

# Muestra el informe de elementos y peso total.

    total_archivos = sum(
        datos["elementos"]
        for ext, datos in conteo.items()
        if ext != "Directorio"
    )

    total_directorios = sum(
        datos["elementos"]
        for ext, datos in conteo.items()
        if ext == "Directorio"
    )

    total_peso = sum(info["peso"] for info in conteo.values())

    print(f"Total de elementos: {total_archivos} archivos, {total_directorios} directorios")
    if 0.99 > total_peso / 1024 / 1024 / 1024 > 0.001:
        print(f"Total de peso en MB: {round(total_peso / 1024 / 1024, 1)} MB")
    elif total_peso / 1024 / 1024 / 1024 < 0.001:
        print(f"Total de peso en KB: {round(total_peso / 1024, 2)} KB")
    else:
        print(f"Total de peso en GB: {round(total_peso / 1024 / 1024 / 1024, 1)} GB")
    print("----------------------------------------")

    if errores > 0:
        print(f"⚠ Archivos que no se pudieron leer: {errores}")
        for archivo in archivos_fallidos:
            print(f"No se puede leer {archivo}")
        print("----------------------------------------")
        print("Su peso NO está incluido en el total.")
    else:
        print("----------------------------------------")
        print("✓ Todos los archivos se leyeron correctamente.")

# Pantalla de inicio y llamada a la funcion.

print("Script para contar archivos por tipo en una carpeta dada:")
try:
    ruta_carpeta = seleccionar_carpeta()
except Exception as e:
    print(f"No se puede abrir el selector de carpeta: {e}")
    ruta_carpeta = None

if ruta_carpeta:
    criterio = criterio_ordenamiento()
    contar_archivos(ruta_carpeta, criterio)
else:
    print("Programa cancelado. No se seleccionó ninguna carpeta.")

