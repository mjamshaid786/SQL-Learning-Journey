from connection import get_connection
# import streamlit as st

user_query = """
--sql
INSERT INTO orders
(order_id, customer_name, city, order_date, total_amount, status)
VALUES
(2001, 'Ali Raza', 'Lahore', '2026-01-05', 3200, 'Pending'),
(2002, 'Sara Khan', 'Islamabad', '2026-01-06', 5000, 'Shipped'),
(2003, 'Hamza Ahmad', 'Faisalabad', '2026-01-08', 7800, 'Delivered'),
(2004, 'Ayesha Malik', 'Lahore', '2026-01-10', 10000, 'Pending'),
(2005, 'Bilal Shah', 'Karachi', '2026-01-12', 12500, 'Shipped'),
(2006, 'Zainab Noor', 'Islamabad', '2026-01-15', 15000, 'Pending'),
(2007, 'Usman Tariq', 'Faisalabad', '2026-01-18', 15001, 'Delivered'),
(2008, 'Hira Ali', 'Lahore', '2026-01-20', 17500, 'Pending'),
(2009, 'Saad Khan', 'Multan', '2026-01-22', 20000, 'Shipped'),
(2010, 'Maryam Iqbal', 'Karachi', '2026-01-25', 20001, 'Delivered'),

(2011, 'Ahmad Hassan', 'Islamabad', '2026-01-28', 22000, 'Pending'),
(2012, 'Fatima Zahra', 'Faisalabad', '2026-02-01', 25000, 'Shipped'),
(2013, 'Hassan Ali', 'Lahore', '2026-02-03', 27500, 'Delivered'),
(2014, 'Noor Fatima', 'Multan', '2026-02-05', 4500, 'Cancelled'),
(2015, 'Daniyal Aslam', 'Karachi', '2026-02-07', 6500, 'Pending'),
(2016, 'Bilal Riaz', 'Rawalpindi', '2026-02-10', 8500, 'Shipped'),
(2017, 'Waseem Akram', 'Faisalabad', '2026-02-12', 11000, 'Delivered'),
(2018, 'Naeem Akram', 'Lahore', '2026-02-15', 13500, 'Cancelled'),
(2019, 'Azeem Akram', 'Islamabad', '2026-02-18', 16500, 'Pending'),
(2020, 'Ahmad Raza', 'Multan', '2026-02-20', 18500, 'Shipped'),

(2021, 'Hassan Raza', 'Rawalpindi', '2026-02-22', 20500, 'Delivered'),
(2022, 'Ali Haidar', 'Karachi', '2026-02-25', 23500, 'Pending'),
(2023, 'Hamza Waseem', 'Islamabad', '2026-03-01', 2800, 'Delivered'),
(2024, 'Sultan Waseem', 'Karachi', '2026-03-05', 9200, 'Cancelled'),
(2025, 'Imran Khan', 'Lahore', '2026-03-08', 14500, 'Pending'),
(2026, 'Usama Farooq', 'Faisalabad', '2026-03-10', 15500, 'Shipped'),
(2027, 'Kashif Mehmood', 'Islamabad', '2026-03-12', 19500, 'Pending'),
(2028, 'Rashid Ali', 'Lahore', '2026-03-15', 30000, 'Delivered'),
(2029, 'Shoaib Ahmed', 'Karachi', '2026-03-18', 35000, 'Pending'),
(2030, 'Muneeb Hassan', 'Rawalpindi', '2026-03-20', 60000, 'Cancelled');
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
