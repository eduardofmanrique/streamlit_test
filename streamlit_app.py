import streamlit as st
import pandas as pd

class ReadCSV():
    def __init__(self, csv_name):
        self.csv_name = csv_name

    def df(self):
        return pd.read_csv(self.csv_name)
data_sources = [
    ReadCSV("data_1.csv"),
    ReadCSV("data_2.csv"),
    # Add more data sources as needed
]

st.title("Select Data Sources")
selected_sources = st.multiselect(
    "Select Data Sources",
    options=[source.csv_name for source in data_sources]
)

if selected_sources:
    st.write("Selected Data Sources:")
    for source in data_sources:
        if source.csv_name in selected_sources:
            st.write(source.csv_name)

# Add a button to load the selected data sources
if st.button("Load Selected Data"):
    selected_data = [source.df() for source in data_sources if source.csv_name in selected_sources]
    
    # You can now work with the selected data as needed
    # For example, you can concatenate the selected DataFrames:
    if selected_data:
        combined_data = pd.concat(selected_data)
        st.write("Combined Data:")
        st.write(combined_data)
