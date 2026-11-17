# watcher.py
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Importa tu función de organización existente.
# Ajusta el nombre si en tu utils.py se llama distinto.
from utils import organizar_archivo  # o como se llame tu función


class DesktopOrganizerHandler(FileSystemEventHandler):
    """Maneja los eventos de creación de archivos en el escritorio."""

    def organizar_archivo (self, event):
        if event.is_directory:
            return

        # Pequeña espera para que el archivo termine de copiarse/descargarse
        time.sleep(1.5)

        file_path = Path(event.src_path)

        # Ignora archivos temporales o parciales típicos de descargas
        if file_path.suffix in ('.crdownload', '.part', '.tmp'):
            return

        try:
            organizar_archivo(str(file_path))
            print(f"OK Organizado: {file_path.name}")
        except Exception as e:
            print(f"ERROR con {file_path.name}: {e}")


def start_watching(path_to_watch: str):
    event_handler = DesktopOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()
    print(f"Monitorizando: {path_to_watch}")
    print("Presiona Ctrl+C para detener.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Ajusta esta ruta si tu escritorio está en otro idioma
    DESKTOP_PATH = str(Path.home() / "Escritorio")  # o "Desktop"
    start_watching(DESKTOP_PATH)
