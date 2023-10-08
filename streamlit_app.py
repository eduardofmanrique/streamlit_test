import pandas as pd
import streamlit as st

df1 = pd.read_csv("data_1.csv")
df2 = pd.read_csv("data_2.csv")

st.write(df1)
st.write(df2)
