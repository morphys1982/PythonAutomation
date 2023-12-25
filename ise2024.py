import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

cookies = {
    'CFID': '6715511',
    'CFTOKEN': '4012cabee958bb5c-19CBE6FC-D5CA-73A5-7203F9807211CB0F',
    '_gcl_au': '1.1.711583910.1702997829',
    '_gid': 'GA1.2.900021486.1702997830',
    '___c3_tid': 'none',
    '_lfa': 'LF1.1.f6a2785767565e4d.1702997832077',
    '___c3_fingerprint31': 'fp3_d4d27b52bdd5afa2c5505e3e6a242e7e',
    '__tcl': '1250165447.1702997836',
    '_fbp': 'fb.1.1702997838476.319018858',
    '_ga_N77RQK6L8Y': 'GS1.1.1702997828.1.1.1702999505.0.0.0',
    '_ga': 'GA1.2.1626826809.1702997828',
    '_ga_BH61S8XYEG': 'GS1.1.1702997831.1.1.1702999505.60.0.0',
    '_gat_UA-3264304-1': '1',
}

headers = {
    'authority': 'ise2024.mapyourshow.com',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'CFID=6715511; CFTOKEN=4012cabee958bb5c-19CBE6FC-D5CA-73A5-7203F9807211CB0F; _gcl_au=1.1.711583910.1702997829; _gid=GA1.2.900021486.1702997830; ___c3_tid=none; _lfa=LF1.1.f6a2785767565e4d.1702997832077; ___c3_fingerprint31=fp3_d4d27b52bdd5afa2c5505e3e6a242e7e; __tcl=1250165447.1702997836; _fbp=fb.1.1702997838476.319018858; _ga_N77RQK6L8Y=GS1.1.1702997828.1.1.1702999505.0.0.0; _ga=GA1.2.1626826809.1702997828; _ga_BH61S8XYEG=GS1.1.1702997831.1.1.1702999505.60.0.0; _gat_UA-3264304-1=1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://ise2024.mapyourshow.com/8_0/explore/exhibitor-gallery.cfm?featured=false',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'search',
    'searchtype': 'exhibitorgallery',
    'searchsize': '1365',
    'start': '50',
}

# Inicializar listas para cada columna
nombres = []
empresas = []
correos = []
telefonos = []
website = []
countryName = []
standReference = []

# Create a Chrome WebDriver instance with the specified executable path
driver = webdriver.Chrome()

response = requests.get(
    'https://ise2024.mapyourshow.com/8_0/ajax/remote-proxy.cfm',
    params=params,
    cookies=cookies,
    headers=headers,
)

# Obtén el contenido JSON
json_content = response.json()

if response.status_code == 200:
        # Iterar sobre los registros en "hits"
        for hit in json_content["DATA"]["results"]["exhibitor"]["hit"]:
            nombres.append(hit["fields"]["exhname_t"])
            empresas.append(hit["fields"]["exhid_l"])
            telefono = ""  # Inicializar la variable fuera del bloque try
            website = ""  # Inicializar la variable fuera del bloque try           
            try:
                 # Construct the URL with the changing digits
                url = f'https://ise2024.mapyourshow.com/8_0/exhibitor/exhibitor-details.cfm?exhid={hit["fields"]["exhid_l"]}'
            
                # Open the URL in the browser
                driver.get(url)
                 # Extract the HTML content after the page has loaded
                html_content = driver.page_source

                # Encontrar el elemento <p> con la clase "showcase-addres # Encontrar el elemento por su id
                #element_by_id = driver.find_element_by_id('newfloorplanlink')
                element_by_id = driver.find_element(By.ID,'newfloorplanlink')

                # Obtener el texto del elemento
                stand = element_by_id.text
                            
                 # Encontrar el elemento <p> con la clase "showcase-address" e imprimir su texto
                address_element = driver.find_element(By.CSS_SELECTOR, 'p.showcase-address.tc')
                address_text = address_element.text
                # Dividir el texto usando '\n' como separador
                address_lines = address_text.split('\n')

                # Extraer la dirección y el país si hay suficientes líneas
                if len(address_lines) >= 2:
                    direccion = address_lines[0]
                    pais = address_lines[-1]

                # Encontrar el elemento <ul> con la clase "showcase-web-phone" e imprimir su texto
                web_phone_element = driver.find_element(By.CSS_SELECTOR, 'ul.showcase-web-phone.ml0.mb3.list.tc')
                web_phone_text = web_phone_element.text
                # Dividir el texto usando el espacio como separador
                #parts = web_phone_text.split(' ')
 
                # Extraer la información del sitio web y el número de teléfono si hay suficientes partes
                #if len(parts) >= 3 and parts[0].lower() == 'www':
                    #website = parts[0]
                    #telefono = f"{parts[2]} {parts[3]}" if len(parts) >= 4 else parts[2]
                
                #correos.append(hit['email'])
                telefonos.append(web_phone_text)
                #website.append(website)
                countryName.append(pais)
                standReference.append(stand)
            except Exception as e:
                print(f"Error loading page for {url}: {e}")
           
        # Crear un DataFrame de pandas
        df = pd.DataFrame({
            'Nombre': nombres,
            'Empresa': empresas,
            #'Correo electrónico': correos,
            'Contacto': telefonos,
            #'Website': website,
            'País': countryName,
            'Stand': standReference            
        })

# Exportar a Excel
df.to_excel('informacion_empresasise2024.xlsx', index=False)