# AbacusReportsAuswertung

Diese Python Scripts sind dafür da, um das Log der Abaengine auszuwerten. Abacus schreibt jede Ausführung von einem Designreport in das run Verzeichnis rein. Dieses Log bleibt aber nicht bestehen. Wenn man nun auswerten will, welche Reports wann und wie viel mal aufgerufen wird, muss man diese Daten selber speichern.

Darum wurden diese Scripts geschrieben, um diese Auswertung machen zu können. 

createDB.py
Dieses Script muss nur einmal verwendet werden, um eine leere sqlite Tabelle zu erstellen, welches dann mit den Informationen gefüllt wird

writeNewLog.py
Dieses Script wird in unserem Fall via Windows Scheduler jede Stunde ausgeführt. Dieses Script schreibt dann all die neuen Aufrufe aus dem Log in die eben erstellte sqlite Tabelle. Somit gehen keine Aufrufe mehr verloren

ReportAuswertun.ipynb
Dieses Jupyter Notebook erstellt eine Ausertung er 10 meist aufgerufenen Reports im Abacus. Es plottet zum einen eine Gesamtauswertung all dieser Reports und zum anderen für jeden dieser 10 Reports die Auswertung über die einzelnen Tage.
