import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('vehicles_us.csv')  # asegúrate de que el archivo esté en la misma carpeta que este script

# Mostrar las primeras filas
print(df.head())