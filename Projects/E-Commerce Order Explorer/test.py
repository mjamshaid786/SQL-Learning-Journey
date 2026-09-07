from connection import get_connection
# import streamlit as st

user_query = """
--sql
INSERT INTO customers (customer_id, customer_name, city,  email, phone, signup_date, total_spent) VALUES (1,' ali raza ','lahore','ALI@EMAIL.COM','03001234567','2026-01-05',12000),
(2,'SARA KHAN','ISLAMABAD',NULL,'03111234567','2026-01-10',8500),
(3,'hamza ahmad','faisalabad','hamza@gmail.com',NULL,'2026-01-15',15000),
(4,'  AYESHA malik','LAHORE','AYESHA@MAIL.COM','03221234567','2026-02-01',4200),
(5,NULL,'karachi','bilal@gmail.com','03331234567','2026-02-05',22000),
(6,'Noor Fatima',NULL,'NOOR@MAIL.COM','03441234567','2026-02-10',7600),
(7,'Daniyal Aslam','MULTAN',NULL,NULL,'2026-02-15',19500),
(8,'  usman tariq ','rawalpindi','USMAN@MAIL.COM','03551234567','2026-03-01',9800)
;
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
