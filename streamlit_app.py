import streamlit as st
import pandas as pd
import pandasql as psql

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
            
    # Input field for SQL query
    st.subheader("Enter SQL Query")
    sql_query = st.text_area("SQL Query", value="", height=150)


            
# Add a button to load the selected data sources
if st.button("Load Selected Data"):
    selected_data = {source.csv_name: source.df() for source in data_sources if source.csv_name in selected_sources}
    if sql_query:
        # Execute SQL query using pandasql
        try:
            result_df = psql.sqldf(sql_query, selected_data)
            st.write("Result of SQL Query:")
            st.write(result_df)
        except Exception as e:
            st.error(f"Error executing SQL query: {str(e)}")
            st.write(selected_data)



