import pandas as pd
from typing import List, Tuple
from datetime import datetime
import os

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    """
    Devuelve los 10 usuarios más activos y el número de tweets para cada uno.
    
    :param file_path: Ruta del archivo JSON.
    :return: Lista de tuplas con (usuario, número de tweets).
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    
   # Cargar los datos completos del archivo JSON
    data = pd.read_json(file_path, lines=True)
    
    # Normalizar la columna 'user' para extraer 'username'
    data_user = pd.json_normalize(data['user'])
    
    # Añadir la columna 'username' al DataFrame
    data['username'] = data_user['username']
    
    # Agrupar por usuario y contar los tweets
    user_activity = data.groupby('username').size().reset_index(name='tweet_count')
    
    # Ordenar por la cantidad de tweets (de mayor a menor)
    top_users = user_activity.sort_values(by='tweet_count', ascending=False).head(10)
    
    # Retornar la lista de tuplas (usuario, tweet_count)
    return list(top_users[['username', 'tweet_count']].itertuples(index=False, name=None))
    pass
