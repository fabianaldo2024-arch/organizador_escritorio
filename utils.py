import shutil
from datetime import datetime, timedelta
from pathlib import Path


def obtener_archivos_ayer(ruta_escritorio):
    """Devuelve los archivos del escritorio modificados ayer."""
    ayer = datetime.now().date() - timedelta(days=1)
    archivos = []
    for elemento in Path(ruta_escritorio).iterdir():
        if elemento.is_file():
            fecha_modificacion = datetime.fromtimestamp(elemento.stat().st_mtime).date()
            if fecha_modificacion == ayer:
                archivos.append(elemento)
    return archivos


def crear_carpeta_fecha(ruta_escritorio, fecha):
    """Crea una carpeta con la fecha y le asigna un icono de color."""
    nombre_carpeta = fecha.strftime("%Y-%m-%d")
    ruta_carpeta = Path(ruta_escritorio) / nombre_carpeta

    # Creamos la carpeta
    ruta_carpeta.mkdir(exist_ok=True)

    # Creamos el archivo .directory para cambiar el icono a rojo
    archivo_icono = ruta_carpeta / ".directory"
    contenido_icono = """[Desktop Entry]
Icon=folder-red
"""
    # Si el archivo no existe, lo creamos
    if not archivo_icono.exists():
        with open(archivo_icono, "w", encoding="utf-8") as f:
            f.write(contenido_icono)

    return ruta_carpeta


def mover_archivos(archivos, destino):
    """Mueve los archivos a la carpeta destino y devuelve cuántos movió."""
    movidos = 0
    for archivo in archivos:
        try:
            shutil.move(str(archivo), str(Path(destino) / archivo.name))
            print(f"  ➜ Movido: {archivo.name}")
            movidos += 1
        except Exception as e:
            print(f"  ❌ Error moviendo {archivo.name}: {e}")

    return movidos