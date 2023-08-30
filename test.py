import pandas as pd
import sqlite3
import os

def get_filename(path):
    return os.path.basename(path)

# r"D:\Abacus\ReportAufrufe\ReportAufrufe.sqlite"
db_path = r"ReportAufrufe.sqlite"


# Load the latest timestamp from the database
conn = sqlite3.connect(db_path)

print("Connected to SQLite")
 
# Getting all tables from sqlite_master
sql_query = """SELECT name FROM sqlite_master
WHERE type='table';"""
 
# Creating cursor object using connection object
cursor = conn.cursor()
     
# executing our sql query
cursor.execute(sql_query)
print("List of tables\n")
    
# printing all tables list
print(cursor.fetchall())

df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
latest_timestamp = pd.read_sql_query('SELECT MIN(TimeStamp) FROM ReportAufrufe', conn).iloc[0, 0]
print(latest_timestamp)

conn.close()
