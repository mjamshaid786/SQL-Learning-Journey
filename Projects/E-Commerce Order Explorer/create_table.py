import psycopg2
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())
def table_creation():
    try:
        with psycopg2.connect(
            host=os.getenv('HOST'),
                    user=os.getenv('USER'),
                    password=os.getenv('PASSWORD'),
                    port=os.getenv('PORT'),
                    dbname=os.getenv('DBNAME')) as conn:
            with conn.cursor() as cur:
                query = """
                --sql
                 CREATE TABLE IF NOT EXISTS orders (
                 order_id INT PRIMARY KEY,
                 customer_name VARCHAR(100),
                 city VARCHAR(50),
                 order_date DATE,
                 total_amount NUMERIC(10,2),
                 status VARCHAR(20)
                 )
                ;
                """
                cur.execute(query)
                return True, "Table Created"
    except Exception as e:
        return False, str(e)

