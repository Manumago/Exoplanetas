import sqlite3
import pandas as pd

# El orden de los datos es 'pl_name', 'pl_rade', 'pl_bmasse'
df = pd.read_csv('exoplanets.csv')
df = df.dropna(subset = ['pl_bmasse', 'pl_rade']) # Eliminamos valores nulos de masa o radio
df = df.drop_duplicates(subset=['pl_name']) # Eliminamos planetas repetidos (solo se toma uno de los valores reportados)

# Conectamos a la base de dato de SQLite
con = sqlite3.connect('datos_mision.db') # objeto de conexión
df.to_sql('exoplanetas', con, if_exists='replace', index=False) # Guardamos en la tabla exoplanetas
con.close()
print(f"Base de datos 'datos_mision.db' creada con {len(df)} registros")
