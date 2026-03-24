echo "Descargando datos de NASA Exoplanet Archive"
wget -q -O exoplanets.csv "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+pl_bmasse+IS+NOT+NULL&format=csv"
echo "Se han guardado los datos en el archivo exoplanets.csv"
echo "Procesando los datos"
python3 constructor_db.py
echo "Generando gráfico: identificación de planetas rocosos y gaseosos"
python3 analisis_visual.py
echo "Proceso finalizado, revisar el archivo resultados.png y el README.md"









