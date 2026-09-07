import psycopg2
import streamlit as st
from connection import get_connection

def table():
    st.subheader("Create New Table")
    
    # 1. Table Name
    table_name = st.text_input("Table Name", placeholder="e.g. customers").strip()
    
    # 2. Number of Columns
    num_cols = st.number_input("Kitne columns banane hain?", min_value=1, max_value=10, value=2)
    
    # Columns ki information store karne ke liye list
    columns_data = []

    st.write("---")
    
    # 3. Simple Loop - Har column ke liye 3 inputs
    for i in range(num_cols):
        st.write(f"**Column {i+1}**")
        c1, c2, c3 = st.columns(3)
        
        col_name = c1.text_input(f"Name", key=f"name_{i}").strip()
        data_type = c2.selectbox(f"Type", ['INT', 'VARCHAR(50)', 'VARCHAR(100)', 'VARCHAR(255)', 'NUMERIC(10, 2)', 'TIMESTAMP', 'DATE'], key=f"type_{i}")
        constraint = c3.multiselect(f"Constraint", ['NONE', 'NOT NULL', 'PRIMARY KEY', 'UNIQUE'], key=f"cons_{i}")
        
        if col_name:
            cons_val = "" if constraint == "NONE" else constraint
            columns_data.append(f"{col_name} {data_type} {cons_val}".strip())

    st.write("---")

    # 4. Create Table Button
    if st.button('CREATE TABLE', type='primary'):
        if not table_name:
            st.error("Table Name likhna zaroori hai!")
            return
            
        if len(columns_data) == 0:
            st.error("Kam se kam 1 Column Name likhna zaroori hai!")
            return

        # SQL Query Definition
        sql_query = f"CREATE TABLE {table_name} (\n  " + ",\n  ".join(columns_data) + "\n);"

        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql_query)
                    conn.commit()
                    
            st.success(f"Table '{table_name}' Created")
            st.code(sql_query, language="sql")
            
        except Exception as e:
            st.error(f"Error: {e}")