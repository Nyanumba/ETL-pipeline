#relevant dictionaries
import requests
import pandas as pd
import os
from sqlalchemy import create_engine
import sqlite3
#importing the api request
api_url = "http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
header = {
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
    db_file_path = 'C:/Users/antho/stackoverflow.db'  # Path to your SQLite database
    table_name = 'questions'  # Name of the table to create in the database
    
    # Create a SQLite engine
    engine = create_engine(f'sqlite:///{db_file_path}')
    
    # Write the DataFrame to the SQLite table
    final_data.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Data loaded into table '{table_name}' in database '{db_file_path}' successfully.")
else:
    print(f"Error: {response.status_code}")
                        




