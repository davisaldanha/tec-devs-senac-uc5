'''Este arquivo será responsável por fazer a conexão com o banco de dados.'''

import os, psycopg as pg
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')
address = os.getenv('DATABASE_ADDRESS')
port = os.getenv('DATABASE_PORT')
dbname = os.getenv('DATABASE_NAME')

def connect():
    '''Retorna a conexão com o banco de dados'''
    try:
        connection = pg.connect(f"user={user} password={password} host={address} port={port} dbname={dbname}")
        print('Banco de dados conectado com sucesso!')

        return connection
    except Exception as e:
        print(f'Error: {e}')
        return None