import sqlite3
from datetime import datetime, timedelta

db_path = r"D:\Abacus\abac\kd\abav\datenbanken\Aufrufe_LongRunning_AbaReports\ReportAufrufe.sqlite"

# Create a SQLite connection
with sqlite3.connect(db_path) as conn:
    current_date = datetime.now()
    threshold_date = current_date - timedelta(days=28)

    # Delete rows older than the threshold date
    conn.execute(f"DELETE FROM ReportAufrufe WHERE TimeStamp < '{threshold_date}'")

with sqlite3.connect(db_path) as conn:
    conn.execute("VACUUM")
