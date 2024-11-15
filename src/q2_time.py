import pandas as pd
from typing import List, Tuple
import os

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Devuelve las 10 fechas con más tweets y el número de tweets para cada una de ellas.
    
    :param file_path: Ruta del archivo JSON.
    :return: Lista de tuplas con (fecha, número de tweets).
    """
    # Cargar los datos completos del archivo JSON
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    data = pd.read_json(file_path, lines=True)
    
    # Convertir la columna 'date' a formato datetime y extraer solo la fecha (sin la hora)
    data['date'] = pd.to_datetime(data['date']).dt.date
    
    # Contar la cantidad de tweets por fecha
    date_activity = data.groupby('date').size().reset_index(name='tweet_count')
    
    # Ordenar por la cantidad de tweets (de mayor a menor)
    top_dates = date_activity.sort_values(by='tweet_count', ascending=False).head(10)
    
    # Retornar la lista de tuplas (fecha, tweet_count)
    return list(top_dates[['date', 'tweet_count']].itertuples(index=False, name=None))
    pass
