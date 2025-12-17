from datetime import datetime as dt
from ..exceptions.exceptions import *

''' Função para converter data para padrão YYYY-MM-DD '''
def convert_date(date_str, date_format="%d/%m/%Y"):
    '''Retorna uma data no padrão YYYY-MM-DD'''

    try:
        date_obj = dt.strptime(date_str.strip(), date_format)

        return date_obj.strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Data Inválida: {date_str}. Esperado formato {date_format}")

