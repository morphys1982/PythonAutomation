import requests
import json
import pandas as pd
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

base_url = 'https://8vvb6vr33k-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.60.0)%3B%20react%20(17.0.2)%3B%20react-instantsearch%20(7.3.0)%3B%20react-instantsearch-core%20(7.3.0)%3B%20JS%20Helper%20(3.15.0)&x-algolia-api-key=00422c3d9f3484bccfae011262fcf49a&x-algolia-application-id=8VVB6VR33K'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.mwcbarcelona.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mwcbarcelona.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

# Inicializar listas para cada columna
nombres = []
empresas = []
correos = []
telefonos = []
websites = []
countryName = []
standReference = []
direcciones = []

# Create a Chrome WebDriver instance with the specified executable path
driver = webdriver.Chrome()

# Iterar por cada letra del alfabeto
for letra in string.ascii_uppercase:
    # Construir el filtro para la letra actual
    filtro_letra = f'letter:{letra}'

    # Construir la cadena JSON para la solicitud
    data = {
        "requests": [
            {
                "indexName": "exhibitors-default",
                "params": f"clickAnalytics=true&facetFilters=%5B%5B%22{filtro_letra}%22%5D%5D&facets=%5B%22attributes%22%2C%22building%22%2C%22externalId%22%2C%22interests%22%2C%22letter%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=24&maxValuesPerFacet=500&page=0&query=&tagFilters=&userToken=web"
            },
            {
                "indexName": "exhibitors-default",
                "params": "analytics=false&clickAnalytics=false&facets=%5B%22letter%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=0&maxValuesPerFacet=500&page=0&query=&userToken=web"
            }
        ]
    }

    # Realizar la solicitud POST
    response = requests.post(base_url, headers=headers, data=json.dumps(data))

    # Obtén el contenido JSON
    json_content = response.json()

    if response.status_code == 200:
        
        # Iterar sobre los registros en "hits"
        for hit in json_content['results'][0]['hits']:
            countryName.append(hit['country'])
            standReference.append(hit['stands'])
            #nombres.append(hit['mainStandHolderName'])
            empresas.append(hit['name'])
            web = ''
            telefono = ''
            nombre = ''
            email = ''
            direccion = '' 
            try:
                # Construct the URL with the changing digits
                url = f'https://www.mwcbarcelona.com/{hit["url"]}'
            
                # Open the URL in the browser
                driver.get(url)
                # Extract the HTML content after the page has loaded
                html_content = driver.page_source
                # Expresiones regulares para extraer la información
                url_pattern = re.compile(r'"@id"\s*:\s*"(.*?)"')
                #url_pattern = re.compile(r'"url":"(.*?)"')
                telephone_pattern = re.compile(r'"telephone":"(.*?)"')
                name_pattern = re.compile(r'"name":"(.*?)"')
                email_pattern = re.compile(r'"email":"(.*?)"')
                address_pattern = re.compile(r'"address":\s*{\s*"@type":\s*"PostalAddress",\s*"addressCountry":"(.*?)",\s*"addressRegion":"(.*?)",\s*"postalCode":"(.*?)",\s*"streetAddress":"(.*?)"\s*}')

                # Aplicar las expresiones regulares al texto
                url_match = url_pattern.search(html_content)
                telephone_match = telephone_pattern.search(html_content)
                name_match = name_pattern.search(html_content)
                email_match = email_pattern.search(html_content)
                address_match = address_pattern.search(html_content)

                # Obtener los resultados
                web = url_match.group(1) if url_match else ""
                telefono = telephone_match.group(1) if telephone_match else ""
                nombre = name_match.group(1) if name_match else ""
                email = email_match.group(1) if email_match else ""
                address_country = address_match.group(1) if address_match else ""
                address_region = address_match.group(2) if address_match else ""
                postal_code = address_match.group(3) if address_match else ""
                street_address = address_match.group(4) if address_match else ""
                direccion = address_region+', '+postal_code+', '+street_address
            except Exception as e:
                print(f"Error loading page for {url}: {e}")            
            websites.append(web)
            telefonos.append(telefono)
            nombres.append(nombre)
            correos.append(email)
            direcciones.append(direccion)
            
            

        # Crear un DataFrame de pandas
        df = pd.DataFrame({
            'Nombre': nombres,
            'Empresa': empresas,
            'Correo electrónico': correos,
            'Teléfono': telefonos,
            'Dirección': direcciones,            
            'Website': websites,
            'País': countryName,
            'Stand': standReference,                        
        })

# Exportar a Excel
df.to_excel('informacion_empresas_mwcbarcelona.xlsx', index=False)

""" response = requests.post(
    'https://8vvb6vr33k-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.60.0)%3B%20react%20(17.0.2)%3B%20react-instantsearch%20(7.3.0)%3B%20react-instantsearch-core%20(7.3.0)%3B%20JS%20Helper%20(3.15.0)&x-algolia-api-key=00422c3d9f3484bccfae011262fcf49a&x-algolia-application-id=8VVB6VR33K',
    headers=headers,
    data=data,
) """
