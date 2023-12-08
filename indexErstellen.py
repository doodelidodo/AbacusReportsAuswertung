import sqlite3

# Verbindung zur SQLite-Datenbank herstellen oder eine neue Datenbank erstellen
conn = sqlite3.connect(r"ReportAufrufe.sqlite")
cursor = conn.cursor()

# SQL-Anweisung zur Erstellung eines Index für die Felder TimeStamp und Report
index_sql = "CREATE INDEX IF NOT EXISTS timestamp_report_index ON ReportAufrufe (TimeStamp, Report);"

# Index erstellen
cursor.execute(index_sql)

# Änderungen in der Datenbank speichern
conn.commit()

# Verbindung zur Datenbank schließen
conn.close()