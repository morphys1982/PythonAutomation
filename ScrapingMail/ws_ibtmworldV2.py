import requests
import json
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.ibtmworld.com/',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.ibtmworld.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = {
    'x-algolia-agent': 'Algolia for vanilla JavaScript 3.27.1',
    'x-algolia-application-id': 'XD0U5M6Y4R',
    'x-algolia-api-key': 'd5cd7d4ec26134ff4a34d736a7f9ad47',
}
   
# Inicializar listas para cada columna
nombres = []
empresas = []
correos = []
telefonos = []
website = []
countryName = []
standReference = []
    
for page in range(0, 22): 
    data = '{"params":"query=&page='+str(page)+'&facetFilters=&optionalFilters=%5B%5D"}'

    response = requests.post(
        'https://xd0u5m6y4r-3.algolianet.com/1/indexes/event-edition-eve-95aab551-da88-4515-ac46-d34847537578_en-gb/query',
        params=params,
        headers=headers,
        data=data,
    )

    # Obtén el contenido JSON
    json_content = response.json()

    if response.status_code == 200:
        # Iterar sobre los registros en "hits"
        for hit in json_content['hits']:
            nombres.append(hit['mainStandHolderName'])
            empresas.append(hit['companyName'])
            correos.append(hit['email'])
            telefonos.append(hit['phone'])
            website.append(hit['website'])
            countryName.append(hit['countryName'])
            standReference.append(hit['standReference'])

        # Crear un DataFrame de pandas
        df = pd.DataFrame({
            'Nombre': nombres,
            'Empresa': empresas,
            'Correo electrónico': correos,
            'Teléfono': telefonos,
            'Website': website,
            'País': countryName,
            'Stand': standReference            
        })

# Exportar a Excel
df.to_excel('informacion_empresas.xlsx', index=False)

# Especifica la ruta del archivo donde deseas guardar el JSON
#file_path = r'H:\My Drive\python\Nuevos\hoteles\archivo.json'

# Abre el archivo en modo de escritura y escribe el contenido JSON
#with open(file_path, 'w') as json_file:
    #json.dump(json_content, json_file)

#print(f'El JSON se ha guardado en {file_path}')