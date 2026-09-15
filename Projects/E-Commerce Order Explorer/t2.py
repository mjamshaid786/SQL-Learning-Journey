import json
import os
import streamlit as st
from streamlit_lottie import st_lottie

# 1. Local JSON file load karne ka helper function
def load_lottie_local(filepath: str):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

# Local JSON path
icon_json = load_lottie_local("../Lottie Animations/Searching.json")

# 2. Side-by-side Layout (Icon + Button)
col_icon, col_btn = st.columns([1, 4])

with col_icon:
    if icon_json:
        # Chhota size set karein taake button ke barabar lage
        st_lottie(icon_json, height=45, width=45, key="btn_icon_anim")

with col_btn:
    # Button ko top spacing dene ke liye
    st.write("") 
    if st.button("Click Here to Process"):
        st.success("Button Clicked!")