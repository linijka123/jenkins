
import pandas as pd
from sqlalchemy import create_engine

# Parametry połączenia
server = 'LAPTOP-CF84MHVJ\DEVELOPER'
database = 'Hurtownia'
driver = 'ODBC Driver 17 for SQL Server'

# Tworzenie adresu połączenia SQLAlchemy
connection_string = f'mssql://@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

# Zapytanie SQL
query = "SELECT * FROM date_dim"

# Załadowanie danych do DataFrame
df = pd.read_sql(query, engine)

# Pokazanie pierwszych kilku wierszy DataFrame
print(df.head())

# Zamknięcie połączenia
engine.dispose()

