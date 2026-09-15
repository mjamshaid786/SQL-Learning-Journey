from connection import get_connection
# import streamlit as st

user_query = """
--sql
INSERT INTO deliveries VALUES
(6001, 1, '2026-04-01', 2, 1500, 'Delivered'),
(6002, 2, '2026-04-01', 4, 1800, 'Delayed'),
(6003, 3, '2026-04-02', 1, 1200, 'Delivered'),
(6004, 1, '2026-04-03', 3, 1600, 'Delivered'),
(6005, 5, '2026-04-04', 5, 2200, 'Delayed'),
(6006, 6, '2026-04-05', 2, 1700, 'Delivered'),
(6007, 7, '2026-04-06', 1, 1300, 'Delivered'),
(6008, 4, '2026-04-07', 6, 2500, 'Delayed'),
(6009, 8, '2026-04-08', 2, 1550, 'Delivered'),
(6010, 3, '2026-04-09', 3, 1400, 'Delivered'),
(6011, 2, '2026-04-10', 2, 1750, 'Delivered'),
(6012, 5, '2026-04-11', 4, 2100, 'Delayed'),
(6013, 1, '2026-04-12', 1, 1500, 'Delivered'),
(6014, 6, '2026-04-13', 5, 1900, 'Delayed'),
(6015, 7, '2026-04-14', 2, 1350, 'Delivered'),
(6016, 4, '2026-04-15', 3, 2400, 'Delivered'),
(6017, 8, '2026-04-16', 4, 1650, 'Delayed'),
(6018, 5, '2026-04-17', 2, 2000, 'Delivered'),
(6019, 2, '2026-04-18', 1, 1750, 'Delivered'),
(6020, 3, '2026-04-19', 5, 1450, 'Delayed');
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
