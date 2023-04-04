import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("MukhammadSiddiq Ibrokhimov")
    content = """
    Hi, I am Muhammad,I am software engineer,and  bachelor student of University of europe. I was born 13.07.2002 in Uzbekistan.
    For 1 year 
    """

    st.info(content)