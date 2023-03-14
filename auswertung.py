import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Create a SQLite connection
conn = sqlite3.connect('ReportAufrufe.sqlite')

# Load data from the 'my_table' table into a Pandas DataFrame
df = pd.read_sql_query('SELECT * FROM ReportAufrufe', conn)
print(df.head())
# Close the SQLite connection
conn.close()

counts = df['Report'].value_counts().nlargest(10)

print(df["Report"].head())

# Erstelle ein Balkendiagramm
ax = counts.plot(kind='bar')

# Füge Titel und Achsenbeschriftungen hinzu
ax.set_title('Häufigkeit von Reports')
ax.set_xlabel('Report-Art')
ax.set_ylabel('Häufigkeit')

# Zeige das Diagramm an
plt.show()
