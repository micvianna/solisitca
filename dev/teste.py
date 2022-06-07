
"""
import datetime
from datetime import timedelta, date, timezone
import time
hoje = (date.today() + timedelta(days=21))
amanha = hoje.strftime('%d/%m/%Y')
print('Depois ', amanha, datetime.time(hour=0, minute=0))

hora = datetime.timedelta(hours=4)
print(hora)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke #actual browser
driver = webdriver.Edge(executable_path="../bin/msedgedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#to refresh the browser
#driver.refresh()
# identifying the link with the help of Javascript executor
time.sleep(5)
javaScript = "document.getElementsByClassName('tp-logo')[0].click();"
print(javaScript.__contains__(''))
# driver.execute_script(javaScript)
#to close the browser
#driver.quit()

f = open("../parametros/ids.txt", "a")
f.writelines(["nline1", "nline2", "nline3"])
f.close()

with open('../parametros/ids.txt', 'r') as arq:
    palavras = arq.readlines()

    for line in palavras:
        print(line)

import xml.etree.ElementTree as et
tree = et.parse('../parametros/ProgramacaoViagem.xml')
# Grava Id da Viagem em um arquivo de texto
root = tree.getroot()

teste = tree.find('IdViagem')
print(teste.text)

for rank in root.iter('IdViagem'):
    new_rank = '15688'
    rank.text = str(new_rank)

tree.write('../parametros/ProgramacaoViagem.xml')

teste = tree.find('IdViagem')
print(teste.text)

import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
content = response.content

site = BeautifulSoup(content, 'html.parser')

#print(site.prettify())
#Html da noticia
#noticia = site.find('div', attrs={'feed-post bstn-item-shape type-materia'})

noticia = site.find('div', attrs={'feed-post-body'})
titulo = noticia.find('a', attrs={'feed-post-link'})
subtitulo = noticia.find('div', attrs={'feed-post-body-resumo'})


print(noticia.text)
#print(titulo.text)
#print(subtitulo.text)
#print('este link veio isso:', noticia.prettify())
print('')
#print(titulo.prettify())
print('')
print(titulo.text )
print('')
print('aqui ', noticia)
print(content)


"""
from selenium import webdriver

driver = webdriver.Firefox(executable_path="[driver path]/geckodriver")
driver.get("[URL to open]")

# To simply click on checkbox regardless of the status
driver.find_element_by_id("privacypolicy").click()

# To find whether the element is a checkbox or not
if driver.find_element_by_id("privacypolicy").get_attribute("type") == "checkbox":
    print("Element is a checkbox")
else:
    print("Element is not a checkbox")

# To find whether the checkbox element is selected or not
isChecked = driver.find_element_by_id("privacypolicy").get_attribute("checked")
if isChecked is not None:
    print("Element checked - ", isChecked)
else:
    print("Element checked - false")

# To find whether the checkbox element is selected or not
result = driver.find_element_by_id("privacypolicy").is_selected()
print("Checkbox status - ", result)

# Select checkbox only when it is not selected
result = driver.find_element_by_id("privacypolicy").is_selected()
if result:
    print('Checkbox already selected')
else:
    driver.find_element_by_id("privacypolicy").click()
    print('Checkbox selected')

# Deselect checkbox only when it is selected
result = driver.find_element_by_id("privacypolicy").is_selected()
if result:
    driver.find_element_by_id("privacypolicy").click()
    print('Checkbox deselected')
else:
    print('Checkbox already deselected')