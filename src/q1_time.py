import pandas as pd
from typing import List, Tuple
from datetime import datetime
import os

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Devuelve las top 10 fechas con más tweets y el usuario más activo por cada una de ellas.
    
    :param file_path: Ruta del archivo JSON.
    :return: Lista de tuplas con (fecha, usuario).
    """
    file_path = os.path.join(os.path.dirname(__file__), '../data.json')
    # Cargar los datos
    data = pd.read_json(file_path, lines=True)
    
    # Asegurarse de que la fecha sea del tipo adecuado
    data['date'] = pd.to_datetime(data['date']).dt.date
    
    # Acceder al nombre de usuario correctamente
    data['user_username'] = data['user'].apply(lambda x: x['username'])
    
    # Agrupar por fecha y usuario, y contar los tweets por fecha
    top_dates = data.groupby(['date', 'user_username']).size().reset_index(name='tweet_count')
    
    
    # Obtener la fecha más popular y el usuario más activo de cada fecha
    top_dates = top_dates.loc[top_dates.groupby('date')['tweet_count'].idxmax()]
    
    # Seleccionar las primeras 10 fechas
    top_10 = top_dates.sort_values(by='tweet_count', ascending=False).head(10)
    
    # Retornar los resultados
    return list(top_10[['date', 'user_username']].itertuples(index=False, name=None))
    
    pass


