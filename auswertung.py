import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#Create a SQLite connection
conn = sqlite3.connect('ReportAufrufe.sqlite')

# Load data from the 'my_table' table into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
# Close the SQLite connection
conn.close()

counts = df['Report'].value_counts().nlargest(10)


# Datum konvertieren
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])

# Nur das Datum extrahieren
df['Date'] = df['TimeStamp'].dt.date

# Gruppieren nach Report und Datum und zählen
df_grouped = df.groupby([df['Report'], df['Date']]).size().reset_index(name='count')

# Top 10 Berichte auswählen
top_10_reports = df_grouped.groupby('Report').sum().nlargest(10, 'count').index.values
df_top_10 = df_grouped[df_grouped['Report'].isin(top_10_reports)]
unique_reports = df_top_10['Report'].unique().tolist()

# Nach Gesamtzählungen sortieren
df_top_10_sorted = df_top_10.groupby('Report').sum().sort_values('count', ascending=False).reset_index()

# Erstelle PDF-Datei zum Speichern der Plots
with PdfPages('plots.pdf') as pdf:
    # Schleife über die Berichte und Erstellung der Plots

    ax = counts.plot(kind='bar')
    # Füge Titel und Achsenbeschriftungen hinzu
    ax.set_title('Häufigkeit von Reports')
    ax.set_xlabel('Report-Art')
    ax.set_ylabel('Häufigkeit')
    
    
    # Zeige das Diagramm an
    plt.tight_layout()
    pdf.savefig()  # Plot in PDF speichern
    plt.close()  # Plot schließen, um Speicher freizugeben

    for report in df_top_10_sorted['Report']:
        # DataFrame für den aktuellen Bericht erstellen
        df_report = df_top_10[df_top_10['Report'] == report]

        # Plot erstellen
        ax = df_report.plot.bar(x='Date', y='count', title=report, rot=45)
        plt.tight_layout()
        pdf.savefig()  # Plot in PDF speichern
        plt.close()  # Plot schließen, um Speicher freizugeben
