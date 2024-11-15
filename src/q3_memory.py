import json
import re
import os
import pandas as pd
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str, n: int = 10) -> List[Tuple[str, int]]:
    """
    Devuelve las 'n' palabras más frecuentes de los tweets, optimizando el uso de memoria.
    
    :param file_path: Ruta del archivo JSON.
    :param n: Número de palabras más frecuentes a devolver (por defecto 10).
    :return: Lista de tuplas con (palabra, frecuencia).
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    word_count = Counter()  # Contador de palabras
    
    # Leemos el archivo JSON en fragmentos
    for chunk in pd.read_json(file_path, lines=True, chunksize=1000):
        # Asegurémonos de que estamos trabajando con la columna 'content'
        if 'content' in chunk.columns:
            # Procesar la columna 'content', eliminar NaN y aplicar la expresión regular
            texts = chunk['content'].fillna('').apply(lambda x: re.findall(r'\b\w+\b', x.lower()))  
        else:
            print("Columna 'content' no encontrada, saltando este fragmento.")
            continue
        
        # Actualizar el contador de palabras
        for words in texts:
            word_count.update(words)
    
    # Obtener las 'n' palabras más frecuentes
    top_words = word_count.most_common(n)
    return top_words
pass
