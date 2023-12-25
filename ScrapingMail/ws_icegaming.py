import requests
import json
import pandas as pd
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import time

# Inicializar listas para cada columna
nombres = []
stands = []
direcciones = []
linkedins = []
website = []

# Create a Chrome WebDriver instance with the specified executable path
driver = webdriver.Chrome()
url = f'https://www.icegaming.com/exhibitor-list'
driver.get(url)
html_content = driver.page_source
# Crear un objeto BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html_content, "html.parser")
# Buscar el elemento ul con la clase específica
ul_element = soup.find('ul', class_='libraryaz__list')

# Si se encontró el elemento ul, buscar los enlaces dentro de los elementos li
if ul_element:
    li_elements = ul_element.find_all('li')
    
    for li in li_elements:
        # Buscar el enlace dentro del elemento li
        a_element = li.find('a')        
        # Construct the URL with the changing digits
        url_tabs = f"https://www.icegaming.com/{a_element.get('href')}"
        driver.get(url_tabs)
        time.sleep(2)
        html_content_tabs = driver.page_source
        soup_tabs = BeautifulSoup(html_content_tabs, "html.parser")
        ul_navegador = soup_tabs.find('ul', class_='pagination__list')
        # Si se encontró el elemento ul, buscar los enlaces dentro de los elementos li
        if ul_navegador:
            li_navegador_elements = ul_navegador.find_all('li')
            for li_navegador in li_navegador_elements:
                # Buscar el enlace dentro del elemento li
                a_navegador_element = li_navegador.find('a')   
                if a_navegador_element:
                    url_navegador_tabs = f"https://www.icegaming.com/{a_navegador_element.get('href')}"
                    driver.get(url_navegador_tabs)
                    time.sleep(2)
                    html_lista_empresas = driver.page_source
                    soup_lista_empresas = BeautifulSoup(html_lista_empresas, "html.parser")
                    ul_lista_empresas = soup_lista_empresas.find('ul', class_='m-exhibitors-list__items js-library-list')
                    if ul_lista_empresas:
                        li_lista_empresas = ul_lista_empresas.find_all('li')
                        for li_lista in li_lista_empresas:
                            a_lista_element = li_lista.find('a')
                            datos = a_lista_element.text   
                            if a_lista_element:
                                driver.execute_script(a_lista_element.get('href'))
                                time.sleep(2)
                                html_empresa = driver.page_source
                                soup_empresa = BeautifulSoup(html_empresa, "html.parser")
                                # Guardar el contenido en un archivo HTML
                                with open("pagina_resultado.html", "w", encoding="utf-8") as archivo:
                                    archivo.write(html_empresa)
                                nombre_type = soup_empresa.find('h1', class_='m-exhibitor-entry__item__header__infos__title')
                                if nombre_type:
                                    nombre = nombre_type.contents[0]
                                else:
                                    nombre = ''
                                stand_type = soup_empresa.find('div', class_='m-exhibitor-entry__item__header__infos__stand')
                                if stand_type:
                                    stand_text = stand_type.contents[0]

                                    # Utilizar una expresión regular para extraer el número del stand
                                    patron_stand = re.compile(r'Stand:\s*(\S+)')
                                    resultado = re.search(patron_stand, stand_text)

                                    if resultado:
                                        stand = resultado.group(1)
                                    else:
                                        stand = ''
                                else:
                                    stand = ''

                                direccion_type = soup_empresa.find('div', class_='m-exhibitor-entry__item__body__contacts__address')
                                if direccion_type:
                                    address_text = direccion_type.get_text(strip=True)  # Obtener el texto sin espacios adicionales
                                    # Utilizar expresiones regulares para limpiar la dirección
                                    direccion = re.sub(r'\t|\n|Address', '', address_text)
                                else:
                                    direccion = ''
                                    
                                li_linkedin = soup_empresa.find('ul', class_='m-exhibitor-entry__item__body__contacts__additional__social')
                                # Encontrar el enlace de LinkedIn
                                linkedin_link = soup.find('a', href=lambda x: x and 'linkedin' in x.lower())
                                # Imprimir el enlace de LinkedIn si se encuentra
                                if linkedin_link:
                                    linkedin = linkedin_link['href']
                                
                                # Encontrar el enlace del sitio web
                                website_link = soup_empresa.find('a', class_='p-button--primary')
                                # Imprimir el enlace del sitio web si se encuentra
                                if website_link:
                                    web = website_link['href']
                                else:
                                    web = ''                             
                            nombres.append(nombre)
                            stands.append(stand)
                            direcciones.append(direccion)
                            linkedins.append(linkedin)
                            website.append(web)
                            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                            time.sleep(2)
    # Crear un DataFrame de pandas
    df = pd.DataFrame({
            'Empresa': nombres,
            'Stand': stands,
            'Direccion': direcciones,
            'Linkedin': linkedins,
            'Website': website            
        })
# Exportar a Excel
df.to_excel('informacion_empresas_icegaming.xlsx', index=False)
