import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser
#Francisco Javier Valerio Lara
#Lo que el siguiente scrip hace es mostrar noticias de las facultades de la UANL dandonos un link y entrando directamente a la pagina de noticias. 


print("Este script navega en las páginas de noticas de la UANL")
try :
    inicioRango = int(input("Pagina inicial para buscar: "))
except ValueError:
    print("Solo se permiten numeros.")
    print("vuelve a ejecutar el programa.")

try:
    finRango = int(input("Pagina final para buscar: "))
except ValueError:
    print("Solo se permiten numeroa.")
    print("vuelve a ejecutar el programa.")
    
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
    
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
