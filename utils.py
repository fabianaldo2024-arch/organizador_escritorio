from pathlib import Path
from datetime import datetime, timedelta
from typing import List

def obtener_archivos_ayer(carpeta: Path) -> List[Path]:
    """
    DOCSTRING: Explica qué hace la función
    
    Args:
        carpeta: Ruta de la carpeta a analizar (Path object)
    
    Returns:
        Lista de archivos modificados ayer
    """
    # 1. Calcular fecha de ayer
    ayer = datetime.now() - timedelta(days=1)
    
    # 2. Obtener inicio y fin del día de ayer
    inicio_ayer = ayer.replace(hour=0, minute=0, second=0, microsecond=0)
    fin_ayer = ayer.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    # 3. Lista para almacenar resultados
    archivos_ayer = []
    
    # 4. Iterar sobre archivos en la carpeta
    # .iterdir() devuelve un generador con todos los items
    for item in carpeta.iterdir():
        # Saltear carpetas organizadas anteriormente
        if item.is_dir() and item.name.startswith("Archivos_"):
            continue
            
        # Solo procesar archivos (no carpetas)
        if item.is_file():
            # Obtener timestamp de modificación
            tiempo_modificacion = datetime.fromtimestamp(item.stat().st_mtime)
            
            # Verificar si fue modificado ayer
            if inicio_ayer <= tiempo_modificacion <= fin_ayer:
                archivos_ayer.append(item)
    
    return archivos_ayer

# ============================================
# FUNCIÓN 4.2: Crear carpeta con fecha
# ============================================
def crear_carpeta_fecha(carpeta_base: Path, fecha: datetime) -> Path:
    """
    Crea una carpeta con formato 'Archivos_YYYY-MM-DD'
    """
    nombre_carpeta = f"Archivos_{fecha.strftime('%Y-%m-%d')}"
    ruta_carpeta = carpeta_base / nombre_carpeta
    ruta_carpeta.mkdir(exist_ok=True)
    
    return ruta_carpeta

# ============================================
# FUNCIÓN 4.3: Mover archivos ← NUEVA
# ============================================
def mover_archivos(archivos: List[Path], destino: Path) -> int:
    """
    Mueve archivos a la carpeta destino
    
    Args:
        archivos: Lista de rutas de archivos a mover
        destino: Ruta de la carpeta destino
    
    Returns:
        Cantidad de archivos movidos exitosamente
    """
    contador = 0
    
    for archivo in archivos:
        try:
            # shutil.move mueve archivo/carpeta
            shutil.move(str(archivo), str(destino))
            contador += 1
            print(f"✓ Movido: {archivo.name}")
        except Exception as e:
            # Capturar errores (permisos, archivo en uso, etc.)
            print(f"✗ Error moviendo {archivo.name}: {e}")
    
    return contador
