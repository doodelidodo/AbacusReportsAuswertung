import pandas as pd
from sqlalchemy import create_engine
import os

def get_filename(path):
    return os.path.basename(path)

path = r"D:\Abacus\ReportAufrufe\ReportAufrufe.sqlite"

# Load CSV into a Pandas DataFrame
df = pd.read_csv('D:/Abacus/abac/log/abaengine/rep/run.log', usecols=range(15))
df.columns = df.columns.str.strip()
df = df.rename(columns={"Report": "Pfad"})
df["Report"] = df['Pfad'].apply(get_filename)

# Convert the 'TimeStamp' column to a datetime format
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

# Create a SQLAlchemy engine
engine = create_engine(f"sqlite:///{path}", echo=True)

# Append the DataFrame to the SQLite table, replacing duplicates
df.to_sql('ReportAufrufe', con=engine, if_exists='replace', index=False, chunksize=1000)

# Close the SQLAlchemy engine
engine.dispose()