import os
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import src.download_json 

def main():
    # Ruta para el archivo JSON descargado
    json_path = os.path.join(os.getcwd(), 'data.json')
    
    # Verificar si el archivo ya existe
    if not os.path.exists(json_path):
        print("Descargando archivo JSON...")
        # Ejecuta el script para descargar el JSON
        src.download_json  # Esto ejecutará el script `download_json.py`
    else:
        print(f"Archivo JSON encontrado en: {json_path}")
    
    # Número de palabras más frecuentes para Q3
    top_n = 10  # Puedes ajustar este número según sea necesario
    
    # Ejecutar las soluciones Q1, Q2, Q3
    print("\nEjecutando Q1 (time)...")
    result_q1_time = q1_time(json_path)
    print(f"Resultado Q1 (time): {result_q1_time}")
    
    print("\nEjecutando Q1 (memory)...")
    result_q1_memory = q1_memory(json_path)
    print(f"Resultado Q1 (memory): {result_q1_memory}")
    
    print("\nEjecutando Q2 (time)...")
    result_q2_time = q2_time(json_path)
    print(f"Resultado Q2 (time): {result_q2_time}")
    
    print("\nEjecutando Q2 (memory)...")
    result_q2_memory = q2_memory(json_path)
    print(f"Resultado Q2 (memory): {result_q2_memory}")
    
    print("\nEjecutando Q3 (time)...")
    result_q3_time = q3_time(json_path, top_n)
    print(f"Resultado Q3 (time): {result_q3_time}")
    
    print("\nEjecutando Q3 (memory)...")
    result_q3_memory = q3_memory(json_path, top_n)
    print(f"Resultado Q3 (memory): {result_q3_memory}")
    
if __name__ == "__main__":
    main()
