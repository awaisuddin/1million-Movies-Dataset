import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests


filename="123"

i=1

url = "https://www1.123moviesto.to/allmovies/" + str(i)

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, 'html.parser')



for link in soup.find_all('a'):
    if "ml-mask" in str(link.get('class')):
        #print("\n")
        videowebsitelink="https://www1.123moviesto.to/"+str(link.get('href'))
        #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
        #print(videowebsitelink)

        url1 = str(videowebsitelink)
        page1 = requests.get(url1)    
        data1 = page1.text
        soup1 = BeautifulSoup(data1, 'html.parser')

        for link1 in soup1.find_all('a'):
            if "first-ep last-ep" in str(link1):
                print(link1.get('data-file'))
                



                
                

        
