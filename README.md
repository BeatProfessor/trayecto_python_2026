# Trayecto 2026 · Python

Ruta de aprendizaje de Python orientada a backend y AI.

## Semana 1 — Fundamentos y sistema de archivos

**Proyecto:** Escáner de librería de archivos.

Recorre una carpeta y todas sus subcarpetas, agrupa los archivos por
extensión y reporta cuántos hay de cada tipo y cuánto pesan. Incluye
selector gráfico de carpeta y ordenamiento configurable.

### Cómo correrlo

python semana_01/proyecto_final_semanal.py

### Lo que aprendí
- `pathlib` para recorrer el sistema de archivos (`iterdir`, `rglob`, `suffix`, `stat`)
- Diccionarios anidados para acumular varios datos por categoría
- `sorted()` con `key` para ordenar por un campo dinámico
- Manejo de errores con `try/except` y sus límites: `rglob()` salta
  carpetas sin permisos en silencio, sin lanzar excepción
- Validado contra Windows sobre 421,846 archivos: coincidencia exacta