import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests


filename="dataset/adventure"

i=1

counter = 0

#Creating a file
myFile = open(str(filename)+'.csv', 'w')

myFile.write("Name"+","+"Image Link"+","+"Movie Watch link"+","+"Description"+","+"IMDB Ratings"+","+"Rotten Tomatoes Ratings"+","+"cast"+","+"Timeline"+","+"Categories"+","+"Language")

myFile.close()



#Scrapping Data

while True: 
    url = "https://www1.123moviesto.to/allmovies/adventure/" + str(i)

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')



    for link in soup.find_all('a'):
        if "ml-mask" in str(link.get('class')):
            #print("\n")
            videowebsitelink="https://www1.123moviesto.to/"+str(link.get('href'))
            name = str(link.get('href').replace(".html","")).replace("/","")
            #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
            #print(name)

            for img in link.find_all('img'):
                #print("https://www1.123moviesto.to/"+str(img.get("data-original")))
                image = "https://www1.123moviesto.to/"+str(img.get("data-original"))

            url1 = str(videowebsitelink)
            page1 = requests.get(url1)    
            data1 = page1.text
            soup1 = BeautifulSoup(data1, 'html.parser')

            for desc in soup1.find_all('div'):
                if "desc" in str(desc.get("class")):
                    description = str(desc.get_text()).replace("!","").replace(",","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace(":","").replace("'","").replace(",","").replace(".","").replace("/","").replace("}","").replace("{","").replace("\n","")
                    #print(description)

            for link1 in soup1.find_all('a'):
                if "first-ep last-ep" in str(link1):
                    if "vidcloud" in str(link1.get('data-file')):
                        #print(link1.get('data-file'))

                        watchlink= str(link1.get('data-file'))
                        break


            '''print("Full Name: ",name)
            print("image: ",image)
            print("movie link: ",watchlink)
            print("Description: ",description)
            print("IMDB Ratings: ","")
            print("Rottentomatoes: ","")
            print("cast :")
            print("timeline : ")
            print("categories : Action")
            print("language: ","English")'''

            print("Action Movie Number: "+str(counter)+"     Page Number:  "+str(i))

            counter= counter+1

            myFile = open(str(filename)+'.csv', 'a+',encoding='utf8')

            myFile.write("\n"+str(name)+","+str(image)+","+str(watchlink)+","+str(description)+","+" "+","+" "+","+"cast :"+","+"timeline : "+","+"Action"+","+"English")

            myFile.close()
    i=i+1
                    



                
                

        
