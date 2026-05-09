import os
from pathlib import Path

# 1. Detectar la carpeta personal y el escritorio automáticamente
# Path.home() ya te lleva a /home/perezman
ESCRITORIO = Path.home() / "Escritorio"

# 2. Verificación de seguridad por si el sistema está en inglés
if not ESCRITORIO.exists():
    ESCRITORIO = Path.home() / "Desktop"

# 3. Verificación final para asegurar que la ruta es válida
if not ESCRITORIO.exists():
    print(f"⚠️ Alerta: No se encontró la carpeta Escritorio en {Path.home()}")


