# main.py
from pathlib import Path
from datetime import datetime, timedelta
from config import ESCRITORIO
from utils import obtener_archivos_ayer, crear_carpeta_fecha, mover_archivos

def organizar_escritorio():
    """
    Función principal que ejecuta la organización
    """
    print("=" * 50)
    print("🗂️  ORGANIZADOR DE ESCRITORIO")
    print("=" * 50)
    
    # 1. Verificar que existe el escritorio
    if not ESCRITORIO.exists():
        print(f"❌ No se encontró el escritorio en: {ESCRITORIO}")
        return
    
    # 2. Obtener archivos de ayer
    print("\n📋 Buscando archivos del día anterior...")
    archivos = obtener_archivos_ayer(ESCRITORIO)
    
    if not archivos:
        print("✓ No hay archivos para organizar")
        return
    
    print(f"✓ Encontrados {len(archivos)} archivos")
    
    # 3. Crear carpeta para ayer
    ayer = datetime.now() - timedelta(days=1)
    carpeta_destino = crear_carpeta_fecha(ESCRITORIO, ayer)
    print(f"\n📁 Carpeta creada: {carpeta_destino.name}")
    
    # 4. Mover archivos
    print("\n🚚 Moviendo archivos...")
    movidos = mover_archivos(archivos, carpeta_destino)
    
    # 5. Resumen
    print("\n" + "=" * 50)
    print(f"✅ Proceso completado: {movidos}/{len(archivos)} archivos movidos")
    print("=" * 50)

if __name__ == "__main__":
    organizar_escritorio()  