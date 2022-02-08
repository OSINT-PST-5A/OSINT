from bs4 import BeautifulSoup
import os
import json as jason
from json2html import *
from lxml import etree


def copytemplate(profilPath,templatePath,profilName):
	os.system('cp '+ templatePath + '/template.html ' + profilPath +'/'+ profilName+'.html')



def fillDocument(profilPath, profilName):
	#Lister tous les fichiers du profil qui n'ont pas pour extension .html
	filelist = [a for a in os.listdir(profilPath) if not os.path.isdir(a)  and not a.endswith(".html")]
	dictionary = {} 
	#Pour chaque fichier dans le dossier profil:
	# - on récupère son contenu
	# - on l'associe à une clé dictionnaire
	# - on rempli le dictionnaire en faisant juste un ajout des élements manquants si besoin
	for fileName in filelist :
		#On récupère le contenu du fichier
		temporaryList = getFileContent(fileName,profilPath)
		if( ("nexfil" in fileName) or ("sherlock" in fileName) ):
			dictionaryKey = "links"
		elif ("myAnimeList" in fileName):
			dictionaryKey = "animeList"
		else:
			dictionaryKey = "mail"
		#Si la clé existe bien
		if (dictionaryKey in dictionary):
			#On vérifie si le contenu du fichier a des éléments différents de ce qui existe déjà dans le dictionnaire et si oui on les ajoute
			if (sorted(dictionary[dictionaryKey]) != sorted(temporaryList)):
				for element in dictionary[dictionaryKey]:
					if(element not in temporaryList):
						temporaryList.append(element)
				dictionary[dictionaryKey] = temporaryList
		#Si la clé n'existe pas alors on la crée et on lui associe le contenu du fichier
		else:
			dictionary[dictionaryKey] = temporaryList

	fillWebPageContent(dictionary,profilPath+'/'+profilName+'.html', profilName)

		
def getFileContent(fileName,profilPath):
	
	file = open(profilPath+'/'+fileName, "r")
	linksList = []
	new_list = [] 
	linksList  = file.readlines()
		
	for fileData in linksList :
		if fileData not in new_list: 
			fileData = fileData.replace('\n', '')
			new_list.append(fileData) 
	
	return new_list




def fillWebPageContent(filesContent, fileName, profilName):	
	os.system('pwd')
	file = open(fileName, "w")
	profileTitle = profilName.split('_')
	#Top container 
	file.write("<!DOCTYPE html><html><head><meta charset=\"utf-8\" /><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin><link href=\"https://fonts.googleapis.com/css2?family=Merriweather&family=Montserrat&family=Sacramento&display=swap\" rel=\"stylesheet\"><link rel=\"stylesheet\" href=\"../../../.Ressource/Templates/css/style.css\" /><title>Profil</title></head><body><div class=\"top-container\"><img class=\"top-cloud\" src=\"../../../.Ressource/Templates/images/cloud.png\" alt=\"cloud-img\">")
	file.write("<h1>" + profileTitle[0] +"</h1><h2>"+ profileTitle[1] + "</h2><img class=\"bottom-cloud\" src=\"../../../.Ressource/Templates/images/cloud.png\" alt=\"cloud-img\"><img src=\"../../../.Ressource/Templates/images/mountain.png\" alt=\"mountain-img\"></div>")
	#Middle container
	file.write("<div class=\"middle-container\"><div class=\"profile\"><h2>Présentation</h2><p class=\"intro\"><p>")
	file.write("TO REPLACE BY JV PRESENTATION")
	file.write("</p></div><hr><div class=\"informations\"><h2>Informations Additionnelles</h2><div class=\"skill-row\"><h3>Anime</h3><p class=\"web-skill-description\">")
	#make it beautiful great again
	#if ("animeList" in filesContent):
	jsonString = ''.join(filesContent["animeList"])
	file.write(json2html.convert(json = jason.loads(jsonString)))
	#else:
	file.write("Not found")
	file.write("</p></div><div class=\"skill-row\"><h3>photos</h3><p class=\"java-skill-description\">")
	file.write("TO REPLACE BY PHOTOS")
	file.write("</p></div><div class=\"skill-row\"><h3>Où le pseudo est-il utilisé ?</h3><p class=\"java-skill-description\">")
	for content in filesContent["links"] :
		file.write(content + "<br>")
	file.write("</p></div><div class=\"skill-row\"><h3>Où l'adresse email est-elle utilisée ?</h3><p class=\"java-skill-description\">")
	for content in filesContent["mail"] :
		file.write(content + "<br>")


	#for content in filesContent:
	#	file
	file.write("</p></div></div></div></body></html>")
	file.close()

	"""for i in filesContent :
		if(i.startswith("http")):
			file.write("<a href="+i+">"+i+"</a><br>")
	file.write("<h1>Picture</h1> <br>")
	for i in filesContent :
		if(i.endswith('.png') or i.endswith('.jpg')):
			file.write("<img src=../../.Resultats/Profiles/"+i+"><br>")
	file.write("<h1>Mail</h1> <br>")
	for i in filesContent :
		if(i.endswith('.com') or i.endswith('.fr')):
			file.write("<a href="+i+">"+i+"</a><br>")"""
	
	#todo rajouté la liste dans le fichier html

def main(profilPath,templatePath,profilName):
	copytemplate(profilPath,templatePath,profilName)
	fillDocument(profilPath,profilName)

if __name__ == "__main__":
	main(profilPath,templatePath,profilName)