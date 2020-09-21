import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests


filename="Vidcloud9serials300"


#Creating a file



#Scrapping Data








i=326

while True:
    url = "https://vidcloud9.com/series?page=" + str(i)
    #print("                                                           counter",str(i))

    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    x1 = " "
    counter = 0
    seriallink = ""

    for link in soup.find_all('a'):
        if "videos" in str(link.get('href')):
            #print("\n")
            videowebsitelink="https://vidcloud9.com"+str(link.get('href'))
            #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
            #print("\n \n \n",videowebsitelink,"\n \n \n")

            url0 = videowebsitelink
            
            page0 = requests.get(url0)    
            data0 = page0.text
            soup0 = BeautifulSoup(data0, 'html.parser')

            for link0 in soup0.find_all('div'):
                if "video-info-left" in str(link0.get("class")):

                    for episode in link0.find_all('a'):
                        if "javascript:" not in episode.get('href'):
                            

                            #print("https://vidcloud9.com"+str(episode.get('href')))
                            mainname = str(episode.get('href')).replace("/videos/","").replace("-"," ").replace(",","")
                            seriallink = "https://vidcloud9.com"+str(episode.get('href'))
                            #print(seriallink)

                            x = "https://www.google.com/search?sxsrf=ALeKk02TepDzilhakTKiwze2e510Z-l8Mg%3A1593521030145&ei=hjP7Xpa9CMmP4-EPz5K0oAo&q="+str(episode.get('href')).replace("/videos/","").replace("-","+")+"+movie+ratings"

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
                                
                            url5 = str(seriallink)


                            page5 = requests.get(url5)    
                            data5 = page5.text
                            soups = BeautifulSoup(data5, 'html.parser')

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
                            '''print("Main name: ",name)
                            print("Full Name: ",name)
                            print("image: ",image)
                            print("movie link: ",watchlink)
                            print("Description: ",description)
                            print("IMDB Ratings: ",imdb)
                            print("Rottentomatoes: ",rt)
                            print("cast :")
                            print("timeline : ")
                            print("categories :")
                            print("language: ","English")'''
                            # make the htmll player file
                            

                            
                            myFile = open(str(filename)+'.csv', 'a+',encoding='utf8')

                            myFile.write("\n"+str(name)+","+str(image)+","+str(watchlink)+","+str(description)+","+str(imdb)+","+str(rt)+","+"cast :"+","+"timeline : "+","+"categories :"+","+"English")

                            myFile.close()
                            

                            print('Stop When 400 Pages are Complete! do the math======================================================================Count( ',str(i),' )========================================================================================' )

                #if i==40:
                    #break

    i=i+1
print("MISSION COMPLETED")

                    



        
