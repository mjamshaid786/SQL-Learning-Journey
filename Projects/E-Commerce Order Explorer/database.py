import psycopg2
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

def connect_database ():
    try:
        conn = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
        )
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("""
            --sql
            CREATE DATABASE ecommerce_training
            ;
            """)
            return True, "Database Created"
    except Exception as e:
        return False, e
    finally:
        if conn:
            conn.close()
        