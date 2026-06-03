import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
 
# ── Ruta al proyecto (ajustá si lo moviste) ──────────────────────────────────
PROJECT_DIR = Path(__file__).parent          # misma carpeta que este script
MAIN_PY     = PROJECT_DIR / "main.py"
LOG_FILE    = PROJECT_DIR / "log.txt"
 
def log(msg: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
 
def main():
    log("=== Autostart iniciado ===")
 
    if not MAIN_PY.exists():
        log(f"ERROR: No se encontró {MAIN_PY}")
        sys.exit(1)
 
    try:
        result = subprocess.run(
            [sys.executable, str(MAIN_PY)],
            capture_output=True,
            text=True,
            timeout=120          # 2 min máximo
        )
 
        if result.stdout:
            log(f"stdout: {result.stdout.strip()}")
        if result.stderr:
            log(f"stderr: {result.stderr.strip()}")
 
        if result.returncode == 0:
            log("Escritorio organizado correctamente ✓")
        else:
            log(f"main.py terminó con código {result.returncode}")
 
    except subprocess.TimeoutExpired:
        log("ERROR: El organizador tardó demasiado (timeout 120 s)")
    except Exception as e:
        log(f"ERROR inesperado: {e}")
 
    log("=== Autostart finalizado ===\n")
 
if __name__ == "__main__":
    main()