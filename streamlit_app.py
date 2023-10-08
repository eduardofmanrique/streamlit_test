import pandas as pd
import streamlit as st

# Define your Streamlit app
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

def select_data_sources():
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
