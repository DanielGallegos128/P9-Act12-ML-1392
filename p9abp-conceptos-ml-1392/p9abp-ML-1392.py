import pandas as pd

# 1. Crear un dataset de ejemplo
datos23 = {
    'id_paciente': [1, 2, 3, 4, 5],
    'edad': [45, 32, 56, 28, 61],
    'nivel_glucosa': [140, 95, 180, 88, 160],
    'presion_arterial': [85, 75, 95, 70, 90],
    'indice_masa_corporal': [30, 22, 34, 24, 32],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(datos23)

# 2. Separar Features (X) y Target (y)
X = df[['edad', 'nivel_glucosa',
        'presion_arterial', 'indice_masa_corporal']]

y = df['diagnostico_diabetes']

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))