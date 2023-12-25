import pandas as pd
import json

# Especifica la ruta completa del archivo si no está en el mismo directorio que tu script
file_path = 'mdShow23.json'

# Lee el contenido del archivo
with open(file_path, 'r', encoding='utf-8') as file:
    json_content = json.load(file)

# Cargar el contenido JSON en un DataFrame de pandas
df = pd.DataFrame(json_content['stands'])

# Exportar el DataFrame a un archivo Excel
df.to_excel('stands_info_mdShow23.xlsx', index=False)