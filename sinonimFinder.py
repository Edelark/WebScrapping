'''Autor: Antoni Cobos 
   GitHub: https://github.com/Edelark'''
from bs4 import BeautifulSoup
import requests
def find(word):
        url = "http://www.wordreference.com/sinonimos/"+word
        reques = requests.get(url)
        html = BeautifulSoup(reques.text, "html.parser")
        sinonim = html.find(class_='trans clickable').ul.li.text
        print(sinonim)
        