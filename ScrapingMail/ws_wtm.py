""" import requests

headers = {
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wtm.com',
    'Referer': 'https://www.wtm.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'x-algolia-agent': 'Algolia for vanilla JavaScript 3.27.1',
    'x-algolia-application-id': 'XD0U5M6Y4R',
    'x-algolia-api-key': 'd5cd7d4ec26134ff4a34d736a7f9ad47',
}

data = '{"params":"query=&hitsPerPage=2&facets=*&highlightPreTag=&highlightPostTag="}'

response = requests.post(
    'https://xd0u5m6y4r-dsn.algolia.net/1/indexes/event-edition-eve-260c67fa-6cec-4d2a-9985-d5c6396d1577_en-gb/query',
    params=params,
    headers=headers,
    data=data,
) """

import requests
import json
import pandas as pd

headers = {
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wtm.com',
    'Referer': 'https://www.wtm.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
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

# Outside the loop
all_data_frames = []
for page in range(0, 2): 
    #data = '{"params":"query=&page=0&facetFilters=&optionalFilters=%5B%5D"}'
    data = '{"params":"query=&page='+str(page)+'&facetFilters=&optionalFilters=%5B%5D"}'

    response = requests.post(
        'https://xd0u5m6y4r-dsn.algolia.net/1/indexes/event-edition-eve-260c67fa-6cec-4d2a-9985-d5c6396d1577_en-gb/query',
        params=params,
        headers=headers,
        data=data,
    )

    #print(response.json())
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

# Create a DataFrame
data_dict = {
    'Nombre': nombres,
    'Empresa': empresas,
    'Correo electrónico': correos,
    'Teléfono': telefonos,
    'Website': website,
    'País': countryName,
    'Stand': standReference
}

df = pd.DataFrame(data_dict)

# Save to Excel
excel_filename = 'output_data1.xlsx'
df.to_excel(excel_filename, index=False)

# Confirmation message
print(f'Data has been saved to {excel_filename}')