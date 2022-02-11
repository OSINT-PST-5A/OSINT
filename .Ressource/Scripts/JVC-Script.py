import requests
import sys
from bs4 import BeautifulSoup


url = "https://www.jeuxvideo.com/profil/" + sys.argv[1] + "?mode=infos"

#Requête pour récupérer le code HTML
response = requests.get(url)

#Si le code de la page HTML a été récupérée avec succès alors...
if response.ok:
    file = open(sys.argv[1] + "_jvc.txt", "w")
    #On utilise BeautifulSoup pour pouvoir ensuite parser le code HTML
    soup = BeautifulSoup(response.text)


    #On va récupérer tout ce qui est contenu dans le block INFO
    infoBlock = soup.find("ul", {"class": "display-line-lib"})
    infoBlockLines = infoBlock.findAll('li')
    for line in infoBlockLines:
        type_data = line.find("div", {"class": "info-lib"})
        data = line.find("div", {"class": "info-value"})
        if("Pays" in type_data.text):
            file.write("\"Pays\" :" + "\"" + data.text.strip()+"\"\n")
        else:
            file.write("\"" + type_data.text.lstrip().replace(" :", "\" :") + "\"" + data.text + "\"\n")

    #On va récupérer la description mise par la personne
    descriptionBody = soup.find("div", {"class": "bloc-description-desc txt-enrichi-desc-profil"})
    if(descriptionBody != None):
        description = descriptionBody.findAll(['p', 'img'])
        file.write("\"Description\" :\"")
        for descriptionElement in description:
            if descriptionElement.name == 'img':
                if descriptionElement != description[-1]:
                    file.write(descriptionElement['src'] + " ")
                else:
                    file.write(descriptionElement['src'] + "\"\n")
            else:
                if descriptionElement != description[-1]:
                    file.write(descriptionElement.text.strip() + " ")
                else:
                    file.write(descriptionElement.text.strip().replace("\n", " ") + "\"\n")

    #On récupère la liste des consoles en sa position
    consolesProfile = soup.find("div", {"class":"info-value machine-profil"})
    consolesProfileLines = consolesProfile.findAll('span')
    file.write("\"Consoles\" :[")
    for line in consolesProfileLines[:-1]:
        file.write("\"" + line.text + "\", ")
    file.write("\"" + consolesProfileLines[-1].text + "\"]\n")

    #On récupère toutes les infos dans son profile de joueur (psn, genres de jeu, etc.)
    gamerProfile = soup.find("ul", {"class": "display-bloc-lib"})
    gamerProfileLines = gamerProfile.findAll('li')
    for line in gamerProfileLines[1:]:
        infoLib = line.find("div", {"class": "info-lib"})
        infoValue = line.find("div", {"class": "info-value"})
        file.write("\"" + infoLib.text.replace(" :", "\" :") + "\"" + infoValue.text.strip()+"\"\n")

    file.close()