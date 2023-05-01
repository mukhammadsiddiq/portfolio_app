import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400 )

with col2:
    st.title("MukhammadSiddiq Ibrokhimov")
    content = """
    Hi, I am Muhammad,I am software engineer,and  bachelor student of University of europe. I was born 13.07.2002 in Uzbekistan.
    For 1 year 
    """

    st.info(content)

content2 = """
    Below you can find some of the apps i have built in python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")


