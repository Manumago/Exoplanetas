import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Cargamos los datos de los exoplanetas de SQL 
# Las columnas son pl_name,pl_rade,pl_bmasse
con = sqlite3.connect('datos_mision.db')
query = "SELECT pl_name, pl_rade, pl_bmasse FROM exoplanetas" #Conexión y extracción
df = pd.read_sql(query, con)
con.close()

#Calculmos densidad relativa a la Tierra
# Si p > 1, es más denso que la Tierra
# Si p < 1, es menos denso que la TIerra
# rho/rho_tierra = (M/M_tierra) / (R/R_tierra)^
df['densidad relativa'] = df['pl_bmasse'] / (df['pl_rade']**3)
rho_tierra = 5.51 # g/cm³
# Convertimos a g/cm³
df['densidad'] = df['densidad relativa'] * 5.51 # En unidades de densidad terrestre

# Determinamos una frontera visual
rho_max = 2.5 #g/cm³
rho_relativo = rho_max / rho_tierra
masas = np.logspace(-1, 4, 100) # masas teóricas
r_limite = (masas / rho_relativo)**(1/3)

plt.figure(figsize=(10,6))
scatter = plt.scatter(df['pl_bmasse'], df['pl_rade'], c=df['densidad'], cmap='berlin', alpha=0.7, s=20, norm=colors.LogNorm(vmin=0.1, vmax=20)) # Usar colors.LogNorm() 
plt.colorbar(scatter, label = 'Densidad')
# Determinamos una línea teórica de transición de rocoso a gaseoso (~3.5 g/cm3)
plt.plot(masas, r_limite, color = 'crimson', linestyle='--', label='Límite densidad  (3.5 $g/cm^3$)')
# REferencia observacional
plt.axhline(y = 1.5, color = 'dodgerblue', linestyle = '--', label = 'Límite rocoso (1.5R⊕ )')
# Escalamos
plt.xscale('log')
plt.yscale('log')
plt.title('Transición planetaria: límite de planetas rocosos a gaseosos')
plt.xlabel('Masa del planeta (M⊕)')
plt.ylabel('Radio del planeta (R⊕)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.15)
plt.savefig('resultado.png')
plt.show()
