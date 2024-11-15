import os
import time
from memory_profiler import memory_usage
from tabulate import tabulate
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
        src.download_json  # Esto ejecutará el script `download_json.py`
    else:
        print(f"Archivo JSON encontrado en: {json_path}")
    
    # Número de palabras más frecuentes para Q3
    top_n = 10  # Puedes ajustar este número según sea necesario

    # Tabla de resultados
    results = []

    # Funciones a evaluar
    tests = [
        ("Q1 (time)", q1_time, [json_path]),
        ("Q1 (memory)", q1_memory, [json_path]),
        ("Q2 (time)", q2_time, [json_path]),
        ("Q2 (memory)", q2_memory, [json_path]),
        ("Q3 (time)", q3_time, [json_path, top_n]),
        ("Q3 (memory)", q3_memory, [json_path, top_n])
    ]

    # Ejecución de pruebas
    for test_name, func, args in tests:
        print(f"\nEjecutando {test_name}...")

        # Medir tiempo y memoria
        start_time = time.time()
        mem_usage = memory_usage((func, args), interval=0.1, timeout=None)
        end_time = time.time()

        exec_time = end_time - start_time
        peak_memory = max(mem_usage)  # Memoria máxima usada

        # Ejecutar la función para obtener el resultado
        result = func(*args)
        print(f"Resultado {test_name}: {result}")

        # Almacenar resultados
        results.append([test_name, f"{exec_time:.2f} s", f"{peak_memory:.2f} MB"])

    # Mostrar la tabla con tabulate
    headers = ["Prueba", "Tiempo de Ejecución", "Memoria Máxima"]
    print("\nResultados:")
    print(tabulate(results, headers=headers, tablefmt="github"))

    
if __name__ == "__main__":
    main()
