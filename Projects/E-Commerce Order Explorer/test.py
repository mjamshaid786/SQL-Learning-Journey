from connection import get_connection
# import streamlit as st

user_query = """
--sql
INSERT INTO drivers VALUES
(1, 'Ali Raza', 'Lahore'),
(2, 'Sara Khan', 'Islamabad'),
(3, 'Hamza Ahmad', 'Faisalabad'),
(4, 'Ayesha Malik', 'Lahore'),
(5, 'Bilal Shah', 'Karachi'),
(6, 'Zainab Noor', 'Islamabad'),
(7, 'Usman Tariq', 'Faisalabad'),
(8, 'Hira Ali', 'Lahore');
"""
try:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(user_query)
            if cur.description: # For SELECT Query
                rows = cur.fetchall()
                print(rows)
            else: # For INSERT / UPDATE Query
                print("Query Executed Successfully")
except Exception as e:
    print(f"ERROR: {e}")
