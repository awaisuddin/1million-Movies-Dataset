import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests





filename="Vidcloud9movies300"


#Creating a file
myFile = open(str(filename)+'.csv', 'w')

myFile.write("Name"+","+"Image Link"+","+"Movie Watch link"+","+"Description"+","+"IMDB Ratings"+","+"Rotten Tomatoes Ratings"+","+"cast"+","+"Timeline"+","+"Categories"+","+"Language")

myFile.close()




#Scrapping Data


i=300

while True:
    url = "https://vidcloud9.com/movies?page=" + str(i)
    #print("                                                           counter",str(i))

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    x1 = " "
    counter = 0

    for link in soup.find_all('a'):
        if "videos" in str(link.get('href')):
            #print("\n")
            videowebsitelink="https://vidcloud9.com"+str(link.get('href'))
            #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
            
            x = "https://www.google.com/search?sxsrf=ALeKk02TepDzilhakTKiwze2e510Z-l8Mg%3A1593521030145&ei=hjP7Xpa9CMmP4-EPz5K0oAo&q="+str(link.get('href')).replace("/videos/","").replace("-","+")+"+movie+ratings"

            #print(x)

            url1 = x            

            page1 = requests.get(url1)    
            data1 = page1.text
            soup1 = BeautifulSoup(data1, 'html.parser')
            imdb = ""
            rt = ""
            for link1 in soup1.find_all('span'):
                
                if "/10" in str(link1.get_text()):
                    imdb = ""
                    #print(link1.get_text(),"  imdb")
                    imdb = link1.get_text().replace(",","")
                    break
            for link2 in soup1.find_all('span'):
                
                if "%" in str(link2.get_text()):
                    rt = ""
                    #print(link2.get_text(),"  rotten tomatoes")
                    rt = link2.get_text().replace(",","")
                    break
                
            urls = videowebsitelink

            pages = requests.get(urls)    
            datas = pages.text
            soups = BeautifulSoup(datas, 'html.parser')

            for links in soups.find_all('iframe'):
                watchlink = "https:"+str(links.get('src'))
                counter = counter + 1
                #print("Watch Link: ",watchlink.replace(' ',''))

                for nm in soups.find_all('h1'):
                    name = ""
                    #print("Name: ",str(nm.get_text()).lower())
                    name = str(nm.get_text()).upper().replace("!","").replace(",","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace(":","").replace("'","").replace(",","").replace(".","").replace("/","").replace("}","").replace("{","")                                                                                          

                for img in soups.find_all('img'):
                    if "cover" in str(img.get('src')):
                        image = ""
                        #print("Cover Link: ",str(img.get('src')))
                        image = str(img.get('src'))
                        break
                    
                for des in soups.find_all('div'):
                    if "content-more-js" in str(des.get('class')):
                        description = str(des.get_text()).replace("\n						","").replace(",","coma%")
                        #print(description)
                        break
            print("name: ",name)
            print("image: ",image)
            print("movie link: ",watchlink)
            print("Description: ",description)
            print("IMDB Ratings: ",imdb)
            print("Rottentomatoes: ",rt)
            print("cast :")
            print("timeline : ")
            print("categories :")
            print("language: ","English")
            # make the htmll player file

            
            myFile = open(str(filename)+'.csv', 'a+')

            myFile.write("\n"+str(name)+","+str(image)+","+str(watchlink)+","+str(description)+","+str(imdb)+","+str(rt)+","+"cast :"+","+"timeline : "+","+"categories :"+","+"English")

            myFile.close()

            print('Stop When 500 Pages are Complete! do the math======================================================================Count( ',str(i),' )========================================================================================' )
                

    i=i+1
print("MISSION COMPLETED")
                

