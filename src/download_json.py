import gdown
import pandas as pd

# ID del archivo JSON en Google Drive
file_id = '1Q3zXDqWNCAYomybkHT_MsQhQGjTsP1Zt' 
# Ruta de destino donde se guardará el archivo descargado en tu computadora local
local_path = 'data.json'

# Descarga el archivo JSON usando gdown
gdown.download(f'https://drive.google.com/uc?id=1Q3zXDqWNCAYomybkHT_MsQhQGjTsP1Zt', local_path, quiet=False)
# Carga el archivo JSON en un DataFrame
data = pd.read_json(local_path, lines=True)  # Usa lines=True si el JSON es de línea por registro

print(f"Archivo descargado correctamente a {local_path}")