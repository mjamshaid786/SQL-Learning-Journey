import streamlit as st
from database import connect_database
from create_table import table_creation
from query import run_query
from data_insertion import insert_data
#------------ STREAMLIT INTERFACE -----------
st.title("E-Commerce Order Explorer")

#------- Database connection -------
is_connected, result = connect_database()
st.sidebar.header("Menu")
if is_connected == True:
    st.sidebar.success(result)
else:
    st.sidebar.error(result)


# #------- Table Creation -------
is_success, result = table_creation()
if is_success == True:
    st.sidebar.success(result)
else:
    st.sidebar.error(result)


#------- Query Runner  -------

option = st.selectbox("What Do You Want", ['Insert Data', 'Fetch Data'])

if option == "Fetch Data":
    run_query()
elif option == "Insert Data":
    insert_data()
