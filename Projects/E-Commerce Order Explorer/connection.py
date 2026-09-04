import psycopg2
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

def get_connection():
    return psycopg2.connect(
        host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT'),
            dbname=os.getenv('DBNAME')
    )