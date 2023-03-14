import pandas as pd
import sqlite3


# Create a SQLite connection
conn = sqlite3.connect('ReportAufrufe.sqlite')

# Load data from the 'my_table' table into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
print(df)
