
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime, timedelta

db_path = r"D:\Abacus\ReportAufrufe\ReportAufrufe.sqlite"
#Create a SQLite connection
conn = sqlite3.connect(db_path)

# Load data from the 'my_table' table into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
# Close the SQLite connection
conn.close()

df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
two_weeks_ago = datetime.now() - timedelta(days=14)
df_last_two_weeks = df[df['TimeStamp'] >= two_weeks_ago]
counts = df_last_two_weeks['Report'].value_counts().nlargest(10)

current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Name des PDF-Dateinamens mit Zeitstempel
pdf_filename = f"D:\Abacus\ReportAufrufe\Auswertung\ReportAufrufe_{current_timestamp}.pdf"
pdf_pages = PdfPages(pdf_filename)

# Plot erstellen
fig, ax = plt.subplots(figsize=(12, 6))  # Breite von 12 Zoll, Höhe von 6 Zoll
counts.plot(kind='bar', ax=ax)

# Füge Titel und Achsenbeschriftungen hinzu
ax.set_title('Top 10 der Häufigkeit der Reportaufrufe')
ax.set_xlabel('Report')
ax.set_ylabel('Häufigkeit')

# Beschriftungen der Bars anpassen
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8)

# Achsenbeschriftungen anpassen
ax.tick_params(axis='x', labelrotation=90, labelsize=10)  # Rotiere und verkleinere die x-Achsenbeschriftungen

# Plot zum PDF hinzufügen
pdf_pages.savefig(fig, bbox_inches='tight')

# Nur das Datum extrahieren
df_last_two_weeks['Date'] = df_last_two_weeks['TimeStamp'].dt.date

# Gruppieren nach Report und Datum und zählen
df_grouped = df_last_two_weeks.groupby([df_last_two_weeks['Report'], df_last_two_weeks['Date']]).size().reset_index(name='count')

# Top 10 Berichte auswählen
top_10_reports = df_grouped.groupby('Report').sum().nlargest(10, 'count').index.values
df_top_10 = df_grouped[df_grouped['Report'].isin(top_10_reports)]
unique_reports = df_top_10['Report'].unique().tolist()

# Nach Gesamtzählungen sortieren
df_top_10_sorted = df_top_10.groupby('Report').sum().sort_values('count', ascending=False).reset_index()


# Schleife über die Berichte und Erstellung der Plots
for report in df_top_10_sorted['Report']:
    # DataFrame für den aktuellen Bericht erstellen
    df_report = df_top_10[df_top_10['Report'] == report]
    
    # Plot erstellen
    fig, ax = plt.subplots(figsize=(12, 6))  # Breite von 12 Zoll, Höhe von 6 Zoll
    df_report.plot.bar(x='Date', y='count', title=report, rot=45, ax=ax)
    
    # Beschriftungen hinzufügen
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', fontsize=8)
    
    plt.tight_layout()
    
    # Plot zum PDF hinzufügen
    pdf_pages.savefig(fig)
    
    plt.close()

# PDF-Datei speichern und schließen
pdf_pages.close()
