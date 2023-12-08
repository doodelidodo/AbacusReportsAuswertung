import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('ReportAufrufe.sqlite')

# Erstelle ein SQLite-Cursor-Objekt
cursor = conn.cursor()

# Tabellenname
table_name = "ReportAufrufe"

# Indexliste für die Tabelle abrufen
cursor.execute(f"PRAGMA index_list({table_name})")
index_list = cursor.fetchall()

# Überprüfen, ob Indexe vorhanden sind
if index_list:
    print(f"Es gibt Indexe auf der Tabelle {table_name}:")
    for index_info in index_list:
        index_name = index_info[1]
        print(f"- Indexname: {index_name}")
else:
    print(f"Es gibt keine Indexe auf der Tabelle {table_name}.")

# Verbindung schließen
conn.close()