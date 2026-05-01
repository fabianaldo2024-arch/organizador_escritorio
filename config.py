import os
from pathlib import Path

# 1. Intentamos detectar la carpeta personal automáticamente
# En tu caso, esto debería detectar: /media/perezman/home/perezman
home = Path.home()

# 2. Definimos la ruta del escritorio basándonos en ese 'home'
ESCRITORIO = home / "Escritorio"

# 3. SEGURIDAD: Si por alguna razón la detección falla, usamos tu ruta fija
if not ESCRITORIO.exists():
    # Esta es tu ruta específica que ya sabemos que funciona
    ESCRITORIO = Path("/media/perezman/home/perezman/Escritorio")

