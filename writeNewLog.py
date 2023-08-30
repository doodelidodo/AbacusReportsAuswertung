import pandas as pd
import sqlite3
import os
import logging

def get_filename(path):
    return os.path.basename(path)

# Configure logging
logging.basicConfig(filename='D:/Abacus/ReportAufrufe/error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # r"D:\Abacus\abac\kd\abav\datenbanken\Aufrufe_LongRunning_AbaReports\ReportAufrufe.sqlite"
    db_path = r"D:\Abacus\abac\kd\abav\datenbanken\Aufrufe_LongRunning_AbaReports\ReportAufrufe.sqlite"


    # Load the latest timestamp from the database
    conn = sqlite3.connect(db_path)
    # Load data from the 'my_table' table into a Pandas DataFrame
    latest_timestamp = pd.read_sql_query('SELECT MAX(TimeStamp) FROM ReportAufrufe', conn).iloc[0, 0]

    # D:/Abacus/abac/log/abaengine/rep/run.log
    # D:/Abacus/abac/log/abaengine/prl/run.log
    df = pd.read_csv('D:/Abacus/abac/log/abaengine/rep/run.log', usecols=range(15))
    df_snap = pd.read_csv('D:/Abacus/abac/log/abaengine/prl/run.log', usecols=range(15), index_col=False)
    df = pd.concat([df, df_snap])

    df.columns = df.columns.str.strip()
    df = df.replace({'"': ''}, regex=True)
    df = df[~df['Report'].str.endswith('.tmp')]
    df = df[~df.Report.str.contains('8370')]
    df = df.rename(columns={"Report": "Pfad"})
    df["Report"] = df['Pfad'].apply(get_filename)


    # Convert the 'TimeStamp' column to a datetime format
    df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

    # Drop duplicates based on the 'TimeStamp' column
    df = df.drop_duplicates(subset=['TimeStamp'])

    if latest_timestamp is not None:
        # Filter DataFrame to only include new entries
        df = df[df['TimeStamp'] > latest_timestamp]

    if not df.empty:
        df.to_sql("ReportAufrufe", con=conn, if_exists='append', index=False, chunksize=1000)
        conn.close()
    else:
        print('dataframe is empty')
        conn.close()
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")