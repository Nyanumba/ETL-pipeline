#relevant dictionaries
import requests
import pandas as pd
import os
from sqlalchemy import create_engine
import sqlite3
#importing the api request
api_url = "https://football98.p.rapidapi.com/premierleague/table/squadname/Liv"
header = {
    "X-RapidAPI-Host": "football98.p.rapidapi.com",
    "X-RapidAPI-Key": "a6850beb1dmsh61b46eda9a90372p1b193bjsn330f9dd99f27",
    "Content-Type": "application/json",
    "Accept-Encoding": "deflate"
}

response = requests.get(api_url, headers = header)
# checking request code status
if response.status_code == 200:
    response_data = response.json()

    # normalizing the data
    items = response_data.get('items', [])
    final_data = pd.json_normalize(items)

     # Flatten nested columns if any
    final_data = final_data.applymap(lambda x: ', '.join(x) if isinstance(x, list) else x)
    #loading data to a excel database
    db_file_path = 'C:/Users/antho/OneDrive/Desktop/APIs Lesson/epl.db'  # Path to your SQLite database
    table_name = 'questions'  # Name of the table to create in the database
    
    # Create a SQLite engine
    engine = create_engine(f'sqlite:///{db_file_path}')
    
    # Write the DataFrame to the SQLite table
    final_data.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Data loaded into table '{table_name}' in database '{db_file_path}' successfully.")
else:
    print(f"Error: {response.status_code}")
                        



