import pandas as pd
from typing import List, Tuple
from collections import Counter
import os
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    """
    Devuelve las 10 fechas con más tweets y el número de tweets para cada una de ellas,
    optimizando el uso de memoria al procesar el archivo JSON.
    
    :param file_path: Ruta del archivo JSON.
    :return: Lista de tuplas con (fecha, número de tweets).
    """
    
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    date_count = Counter()

    # Abrir el archivo JSON línea por línea
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)  # Parsear la línea JSON correctamente
            tweet_date = tweet.get('date')  # Extraer la fecha
            
            if tweet_date:
                # Convertir la fecha a solo la parte de la fecha (sin la hora)
                date = tweet_date.split('T')[0]  # Asumimos formato ISO 8601 (YYYY-MM-DDTHH:MM:SS)
                date_count[date] += 1

    # Obtenemos las 10 fechas con más tweets
    top_dates = date_count.most_common(10)

    return top_dates

pass