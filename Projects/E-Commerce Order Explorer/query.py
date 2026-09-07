from connection import get_connection
import streamlit as st
import pandas as pd
from code_editor import code_editor
def run_query():
    response = code_editor(
        code="", # initial text blank rakha hai
        lang="sql",
        theme="vs-dark",
        height=[5, 20],
        response_mode="debounce", # track live text state, without it will show empty query error
        options={"placeholder": "Write SQL Query here..."},
        key="sql_editor"
    )
    user_query = ""
    if isinstance(response, dict) and "text" in response:
        user_query = response["text"].strip()
    elif isinstance(response, str):
        user_query = response.strip()
    if st.button("Run", type="primary", icon=':material/play_arrow:'):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(user_query)
                    if cur.description: # For SELECT Query
                        rows = cur.fetchall()
                        colnames = [desc[0] for desc in cur.description]
                        df = pd.DataFrame(rows, columns=colnames)
                        st.dataframe(df)
                        st.code(user_query, language="sql")
                    else: # For INSERT / UPDATE Query
                        st.success("Query Executed Successfully")
                        st.code(user_query, language="sql")
        except Exception as e:
            st.write(f"ERROR: {e}")
