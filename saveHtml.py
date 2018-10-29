def saveUrl(urlIncomming):
    import requests
    from bs4 import BeautifulSoup
    import urllib
    import os
    import datetime
    import time
    url = urlIncomming
    response = requests.get(url)
    dateAndtime = str(time.strftime("%d%m%y_%H%M%S"))
  
    #Hier wird die Hauptseite in einem Cacheorder gespeichert. Zudem wir einem .txt file die angelegten Filenamen gespeichert. Trennungzeichen zwischen den Namen ist ein ";"

    #Brauch ich um Ordner anzulegen   
        
    if not os.path.exists("./cache"):
        cacheDir = os.mkdir("./cache")
       
    found_text = []
    if response.status_code == 200:
        
            doc = BeautifulSoup(response.text,"html5lib")

            text = doc.find_all("p")

            for texte in text:
                found_text.append(texte)
    else:
        print("Seite offline")

    filecache = "./cache/"+dateAndtime+".txt"
    filelist = "./cache/"+"filelist.txt"

    with open (filecache,"w") as file:
        file.write(str(found_text))
        file.close()
        # print(dateAndtime + ".txt")
 
    
    with open(filelist,"a") as file:
        file.write(str(dateAndtime+".txt\n"))
        file.close()

    pass