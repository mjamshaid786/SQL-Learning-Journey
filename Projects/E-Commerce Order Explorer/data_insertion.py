from connection import get_connection
import streamlit as st
def insert_data():
        #------------- ORDER ID ------------
        order_id = st.number_input("Enter Order ID", min_value=1, step=1)
        #------------- CUSTOMER NAME ------------
        name = st.text_input("Enter Customer Name")
        #------------- CITY NAME ------------
        c_name = st.text_input("Enter City Name")
        #------------- ORDER DATE ------------
        order_date = st.date_input("Enter Order Date")
        #------------- TOTAL AMOUNT ------------
        total_amount = st.number_input("Enter Total Amount", min_value=1, step=1)
        #------------- ORDER STATUS ------------
        order_status = st.selectbox("Select Order Status", ['Pending', 'Shipped', 'Delivered', 'Cancelled'])

        if st.button("INSERT"):
            #------------- INPUT VALIDATIONS ------------
            customer_name = name.strip().title()
            city_name = c_name.strip().title()
            if not customer_name:
                st.error("Name can not be Empty.")
                return
            elif not customer_name.replace(" ", "").isalpha():
                st.error("Name only contain Alphabets.")
                return
            else:
                valid_customer_name = customer_name
            if not city_name:
                st.error("City Name can not be Empty.")
                return
            elif not city_name.replace(" ", "").isalpha():
                st.error("City Name only contain Alphabets.")
                return
            else:
                valid_city_name = city_name
        



            user_query = """
                --sql
                INSERT INTO orders (order_id, customer_name, city,  order_date, total_amount, status) VALUES (%s, %s, %s, %s, %s, %s)
                ;
                """
            try:
                with get_connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(user_query, (order_id, valid_customer_name, valid_city_name, order_date, total_amount, order_status))
                        if cur.description: # For SELECT Query
                            rows = cur.fetchall()
                            st.write(rows)
                        else: # For INSERT / UPDATE Query
                            st.success("Query Executed Successfully")
            except Exception as e:
                        st.write(f"ERROR: {e}")
