from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# SQLite-Datenbank erstellen
engine = create_engine('sqlite:///ReportAufrufe.sqlite', echo=True)

# Basisdeklaration für ORM-Objekte erstellen
Base = declarative_base()


# ORM-Klasse für Tabelle definieren
class Table(Base):
    __tablename__ = 'ReportAufrufe'

    TimeStamp = Column(DateTime, primary_key=True)
    Type = Column(String)
    State = Column(String)
    Seconds = Column(String)
    ErrorCode = Column(String)
    ErrorMessage = Column(String)
    Application = Column(String)
    Scope = Column(String)
    Mandant = Column(String)
    User = Column(String)
    Pfad = Column(String)
    Report = Column(String)
    SubReportTables = Column(String)
    SubReportFields = Column(String)
    Tables = Column(Integer)
    Finds = Column(Integer)


# Tabelle erstellen
Base.metadata.create_all(engine)
