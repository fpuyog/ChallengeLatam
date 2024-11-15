import gdown
import pandas as pd
import os

# ID del archivo JSON en Google Drive
file_id = '1Q3zXDqWNCAYomybkHT_MsQhQGjTsP1Zt' 
# Ruta de destino donde se guardará el archivo descargado en tu computadora local
local_path = 'data.json'

def download_json():
    """Función para descargar el archivo JSON si no está presente."""
    if not os.path.exists(local_path):
        print("Descargando archivo JSON...")
        gdown.download(f'https://drive.google.com/uc?id={file_id}', local_path, quiet=False)
        print(f"Archivo descargado correctamente a {local_path}")
    else:
        print(f"Archivo JSON ya existe en: {local_path}")
    

# Esto asegura que el código solo se ejecute si el archivo se ejecuta directamente
if __name__ == "__main__":
    download_json()
