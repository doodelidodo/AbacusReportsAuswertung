
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime, timedelta

db_path = r"ReportAufrufe.sqlite"
#Create a SQLite connection
conn = sqlite3.connect(db_path)

# Load data from the 'my_table' table into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
# Close the SQLite connection

df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
# df = df.replace({'"': ''}, regex=True)
# df = df[~df['Report'].str.endswith('.tmp')]
# df = df[~df.Report.str.contains('8370')]


current_date = datetime.now()
threshold_date = current_date - timedelta(days=42)

# Filtern der Zeilen basierend auf dem TimeStamp
df_filtered = df[df['TimeStamp'] >= threshold_date]

df_filtered.to_sql('ReportAufrufe', conn, if_exists='replace', index=False)

# Close the SQLite connection
conn.close()
