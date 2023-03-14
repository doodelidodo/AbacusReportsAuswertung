import pandas as pd
import sqlite3
import os


def get_filename(path):
    print(path)
    print(os.path.basename(path))
    return os.path.basename(path)


# r"D:\Abacus\ReportAufrufe\ReportAufrufe.sqlite"
db_path = r"D:\Abacus\ReportAufrufe\ReportAufrufe.sqlite"


# Load the latest timestamp from the database
conn = sqlite3.connect('ReportAufrufe.sqlite')
# Load data from the 'my_table' table into a Pandas DataFrame
latest_timestamp = pd.read_sql_query('SELECT MAX(TimeStamp) FROM ReportAufrufe', conn).iloc[0, 0]

# Load CSV into a Pandas DataFrame D:/Abacus/abac/log/abaengine/rep/run.log
df = pd.read_csv('log/run.log', usecols=range(15))
df.columns = df.columns.str.strip()
df = df.rename(columns={"Report": "Pfad"})
df["Report"] = df['Pfad'].apply(get_filename)

# Convert the 'TimeStamp' column to a datetime format
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

# Drop duplicates based on the 'TimeStamp' column
df = df.drop_duplicates(subset=['TimeStamp'])

if latest_timestamp is not None:
    print(latest_timestamp)
    # Filter DataFrame to only include new entries
    df = df[df['TimeStamp'] > latest_timestamp]

# Create a new SQLAlchemy engine and append the new entries to the SQLite table, replacing duplicates
if not df.empty:
    df.to_sql('ReportAufrufe', con=conn, if_exists='append', index=False, chunksize=1000)
else:
    print('dataframe is empty')
