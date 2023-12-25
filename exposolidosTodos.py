import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://exposolidos.com/expositores-2024/"

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la respuesta
    html_content = response.text

    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar la lista de elementos <li> dentro del contenedor <ul>
    lista_elementos_li = soup.select('.nav-tabs.nav-justified li')

    # Crear una lista de objetos que contienen href y texto de cada elemento <a>
    lista_resultados = []
    for elemento_li in lista_elementos_li:
        a_tag = elemento_li.find('a', class_='tab-link')
        if a_tag:
            href = a_tag.get('href')
            texto = a_tag.find('h4', class_='fusion-tab-heading').text
            lista_resultados.append({'href': href, 'tab': texto})

    # URL base
    base_url = 'https://exposolidos.com/expositores-2024'

    # Crear listas para almacenar datos
    nombres_empresas = []
    numeros_stand = []
    direcciones = []
    telefonos = []
    correos = []
    paginas_web = []
    
    # Supongamos que 'html_content' es el contenido HTML que tienes
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todos los elementos <div class="tab-pane fade fusion-clearfix in active">
    #Todos
    #elementos_tab_pane = soup.find_all('div', class_='tab-pane fade fusion-clearfix')
    #El primero
    elementos_tab_pane = soup.find_all('div', class_='tab-pane fade fusion-clearfix active in')

    # Imprimir o trabajar con los elementos encontrados
    for elemento_tab_pane in elementos_tab_pane:
        for lista in elemento_tab_pane:
            # Crear un objeto BeautifulSoup
            if lista != '\n':
                elementos_empresas = lista.find_all('div', class_="expositores")
                for elemento_empresa in elementos_empresas:    
                    # Extraer el nombre de la empresa
                    patron_nombre = re.compile(r'\n(.+?)\nStand', re.DOTALL)
                    nombre_empresa = re.search(patron_nombre, elemento_empresa.text).group(1).strip()

                    # Extraer el número de stand
                    patron_stand = re.compile(r'Stand (\w+)')
                    numero_stand = re.search(patron_stand, elemento_empresa.text).group(1)
                    # Buscar el nombre de la empresa
                    #nombre_empresa = soup.find('h2', class_='fusion-responsive-typography-calculated').find('a').text.strip()

                    # Buscar el número de stand
                    #numero_stand_tag = soup.find('h4', style="margin: 0")
                    #if numero_stand_tag:
                        #numero_stand = numero_stand_tag.text.strip()
                    #else:
                        #numero_stand = "No disponible"
                    href_empresa = elemento_empresa.contents[3].contents[0].attrs.get('href', 'No disponible')
                    #href_empresa = elementos_div.get('href')
                    # Hacer la solicitud HTTP
                    if href_empresa == 'No disponible':
                        telefono = 'No disponible'
                        correo = 'No disponible'
                        pagina_web = 'No disponible'
                    else:
                        
                        response_empresa = requests.get(href_empresa)
                        # Obtener el contenido HTML de la respuesta
                        html_empresa = response_empresa.text
                        # Crear un objeto BeautifulSoup
                        soup_empresa = BeautifulSoup(html_empresa, 'html.parser')
                        # Buscar la dirección
                        # Buscar el teléfono, correo y página web
                        detalles_contacto = soup_empresa.find('ul', class_='fusion-checklist-1')
                        contacto_items = detalles_contacto.text
                        # Eliminar \t y \n del inicio
                        texto_sin_tabs_nls = re.sub(r'^[\t\n]+', '', contacto_items)

                        # Dividir el texto en partes
                        partes = re.split(r'\n+', texto_sin_tabs_nls)

                        # Eliminar espacios al inicio y final de cada parte
                        partes_formateadas = [parte.strip() for parte in partes]

                        # Unir las tres primeras partes (dirección) con comas
                        direccion = ', '.join(partes_formateadas[:3])

                        # Extraer teléfono, correo electrónico y página web
                        telefono = partes_formateadas[3] if len(partes_formateadas) > 3 else None
                        correo = partes_formateadas[4] if len(partes_formateadas) > 4 else None
                        pagina_web = partes_formateadas[5] if len(partes_formateadas) > 5 else None

                        # Imprimir los resultados
                        print("Dirección:", direccion)
                        print("Teléfono:", telefono)
                        print("Correo electrónico:", correo)
                        print("Página web:", pagina_web)
                        # Almacenar los datos en las listas
                        nombres_empresas.append(nombre_empresa)
                        numeros_stand.append(numero_stand)
                        direcciones.append(direccion)
                        telefonos.append(telefono)
                        correos.append(correo)
                        paginas_web.append(pagina_web)

    # Crear un DataFrame con los datos
    df = pd.DataFrame({
        'Nombre Empresa': nombres_empresas,
        'Número de Stand': numeros_stand,
        'Dirección': direcciones,
        'Teléfono': telefonos,
        'Correo': correos,
        'Página Web': paginas_web
    })

    # Guardar el DataFrame en un archivo Excel
    df.to_excel('informacion_expositores.xlsx', index=False)
    print("Datos guardados correctamente en 'informacion_expositores.xlsx'")
else:
    print(f"Error al obtener la página. Código de estado: {response.status_code}")
