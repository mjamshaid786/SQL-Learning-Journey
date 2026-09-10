from connection import get_connection
# import streamlit as st

user_query = """
--sql
INSERT INTO customer_orders VALUES
(5001, 1, 101, 1, '2026-03-01', 'Delivered'),
(5002, 2, 102, 2, '2026-03-02', 'Pending'),
(5003, 3, 104, 1, '2026-03-03', 'Delivered'),
(5004, 1, 103, 2, '2026-03-04', 'Shipped'),
(5005, 5, 106, 1, '2026-03-05', 'Delivered'),
(5006, 6, 105, 1, '2026-03-06', 'Pending'),
(5007, 7, 107, 5, '2026-03-07', 'Delivered'),
(5008, 8, 101, 1, '2026-03-08', 'Shipped'),
(5009, 3, 106, 2, '2026-03-09', 'Delivered'),
(5010, 9, 104, 1, '2026-03-10', 'Cancelled'),
(5011, 2, 107, 10, '2026-03-11', 'Delivered'),
(5012, 5, 102, 3, '2026-03-12', 'Pending');
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
