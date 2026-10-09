
import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
# 23.
datos23 = {
    'distancia_km': [1.7, 3.4, 5.6, 2.5, 4.2],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [24, 38, 29, 34, 26],
    'tiempo_entrega_min': [13, 30, 44, 18, 39]
}

df = pd.DataFrame(datos23)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
