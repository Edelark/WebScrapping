'''Autor: Antoni Cobos 
   GitHub: https://github.com/Edelark'''
from bs4 import BeautifulSoup
import requests
def find(book):
    url = url_generator(book) #get the casa del libro's url 
    html = web_scrapping(url) #webscrapping to these url
    url_posible = html.find(class_='title-link') #we find the url in the html
    url = url_posible.get('href') #book's url
    url_complete = "https://www.casadellibro.com"+url #complete book url
    #print("url total: "+url_complete)
    page = web_scrapping(url_complete)#get the book page's html
    theme = page.find(class_='expmat').a.text
    title = page.find(class_="book-header-2-title").text
    pos_isbn = title.find('ISBN')
    title = title[:pos_isbn].strip()
    description = page.find(class_='acortar').text
    print("Title -> "+title)
    print("Theme -> "+theme)
    print("Description -> "+description)
    
    
    
    
    
    
def url_generator(book): #finder's url
    little=book.split()
    str1 = '+'.join(little)
    return ("https://www.casadellibro.com/busqueda-generica?busqueda="
    +str1+"&nivel=5")
    
def web_scrapping(url):#extract the html 
    request = requests.get(url)
    return BeautifulSoup(request.text, "html.parser")
