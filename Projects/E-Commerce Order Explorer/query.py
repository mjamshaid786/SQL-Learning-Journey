from connection import get_connection
import streamlit as st
import pandas as pd
def run_query():
    user_query = st.text_area(
        label="Write Your Query Here",
        height=150,
        placeholder="Write SQL Query"
    ).strip()
    if st.button("Run"):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(user_query)
                    if cur.description: # For SELECT Query
                        rows = cur.fetchall()
                        colnames = [desc[0] for desc in cur.description]
                        df = pd.DataFrame(rows, columns=colnames)
                        st.dataframe(df)
                    else: # For INSERT / UPDATE Query
                        st.success("Query Executed Successfully")
        except Exception as e:
            st.write(f"ERROR: {e}")
