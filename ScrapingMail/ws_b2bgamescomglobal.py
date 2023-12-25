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
url = f'https://b2b.gamescom.global/gamescom-exhibitors/list-of-exhibitors/'
driver.get(url)
# Encuentra el botón por su ID
time.sleep(3)
accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_button.click()
#time.sleep(5)
#cookie_button = driver.find_element(By.ID, "cleverpush-confirm-btn cleverpush-confirm-btn-allow")
#cookie_button.click()
html_content = driver.page_source
# Crear un objeto BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html_content, "html.parser")
# Buscar el elemento ul con la clase específica
div_elements = soup.find('div', class_='esr search-results')

if div_elements:
    #for div_element in div_elements:
        # Buscar todos los elementos div con la clase 'item' dentro del div 'esr search-results'
        items = div_elements.find_all('div', class_='item')

        # Iterar sobre los elementos encontrados
        for item in items:
           # Utilizar expresiones regulares para encontrar las tres primeras palabras
            match = re.search(r'\b(\w+)\b.*\b(\w+)\b.*\b(.*Stand: [^\n]+)\n', item.text)
            
            # Verificar si se encontraron coincidencias y obtener las palabras
            if match:
                empresa = match.group(1).strip()
                pais = match.group(2).strip()
                stand = match.group(3).strip()
            url_empresa = item.get('href')
            # Realizar las operaciones que necesites con cada elemento 'item'
            print(item)
