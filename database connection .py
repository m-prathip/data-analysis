import pandas as pd
from sqlalchemy import create_engine

# 1. Load and analyze your data
# Replace 'data.csv' with your actual file path
df = pd.read_csv('sales_performance.csv', nrows=150)

# --- Perform your Python analysis here ---
# Example: df['total'] = df['price'] * df['quantity']
# df = df.dropna() 

# 2. Set up the database connection
# Format: mysql+pymysql://username:password@host/database_name
username = 'root'
password = 'root'
host = 'localhost' # or your server IP, e.g., '127.0.0.1'
database = 'sales_data' # <-- Example: 'sales_db'

connection_string = f"mysql+pymysql://{username}:{password}@{host}/{database}"
engine = create_engine(connection_string)

# 3. Export to MySQL
table_name = 'analyzed_data_table'

try:
    df.to_sql(
        name=table_name, 
        con=engine, 
        if_exists='append', # Options: 'fail', 'replace', 'append'
        index=False         # Set to True if your DataFrame index is meaningful
    )
    print(f"Data successfully exported to {table_name}!")
except Exception as e:
    print(f"An error occurred: {e}")