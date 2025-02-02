import streamlit as st
import pandas as pd
import mysql.connector as db
from mysql.connector import Error

def create_connection():
        try:
            connection = db.connect(
                user='root',
                password='Iamgokul@123',
                host='localhost',
                database='cricsheet')
            return connection
        
        except Error as e:
            st.error(f"Error Connecting to Database...! {e}")
            return None
        
def get_table_names(connection):
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
        
        except Error as e:
              st.error(f"Error Connecting to Database...! {e}")
              return []
        
        finally:
              if cursor:
                    cursor.close()

def fetch_tables(connection, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            return pd.read_sql(query, connection)
        
        except Error as e:
              st.error(f"Error Fetching Data from {table_name} : {e}")
              return None
        
def main():
        st.title("Cricsheet Table View")
        connection = create_connection()

        if connection is not None:
            tables = get_table_names(connection)
        
            if tables:
                selected_table = st.selectbox("Select a Table", tables)
                if selected_table:
                    data = fetch_tables(connection, selected_table)
                    if data is not None:
                        st.dataframe(data)
            else:
                st.warning("No tables found in the database.")

            connection.close()

        else:
            st.error("Unable to connect to the database.")



if __name__ == "__main__":
    main()
            
          