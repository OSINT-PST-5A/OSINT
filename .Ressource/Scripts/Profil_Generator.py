from bs4 import BeautifulSoup
import os
from lxml import etree


def copytemplate(profilPath,templatePath,profilName):
	os.system('cp '+ templatePath + '/template.html ' + profilPath +'/'+ profilName+'.html' )

def fillDocument(profilPath, profilName):
	#list = os.system('ls -p '+profilPath+' | grep -v /')
	filelist = [a for a in os.listdir(profilPath) if not os.path.isdir(a)  and not a.endswith(".html")]
	linkslist = [] 
	for i in filelist :
		temporaryList = getLink(i,profilPath)
		for j in temporaryList:
			linkslist.append(j)
	print(linkslist)
	fillLink(linkslist,profilPath+'/'+profilName+'.html')

		
def getLink(fileName,profilPath):
	
	file = open(profilPath+'/'+fileName, "r")
	linksList = []
	new_list = [] 
	if(fileName.endswith('.png') or fileName.endswith('.jpg')):
		linksList.append(fileName)
	else : 
		linksList  = file.readlines()
		
	for i in linksList :
		if i not in new_list: 
			i = i.replace('\n', '')
			new_list.append(i) 

	
	return new_list

def fillLink(linksList, fileName):	
	os.system('pwd')
	print(fileName)
	file = open(fileName, "w")
	file.seek(0,2)
	file.write("<h1>Pseudo</h1> <br>")
	for i in linksList :
		if(i.startswith("http")):
			file.write("<a href="+i+">"+i+"</a><br>")
	file.write("<h1>Picture</h1> <br>")
	for i in linksList :
		if(i.endswith('.png') or i.endswith('.jpg')):
			file.write("<img src=../../.Resultats/Profiles/"+i+"><br>")
	file.write("<h1>Mail</h1> <br>")
	for i in linksList :
		if(i.endswith('.com') or i.endswith('.fr')):
			file.write("<a href="+i+">"+i+"</a><br>")
	
	#todo rajouté la liste dans le fichier html

def main(profilPath,templatePath,profilName):

	copytemplate(profilPath,templatePath,profilName)
	fillDocument(profilPath,profilName)

if __name__ == "__main__":
	#profilPath = '/mnt/d/ESIEA/5A/PST/OSINT/.Resultats/Profiles'
	#templatePath = '/mnt/d/ESIEA/5A/PST/OSINT/.Ressource/Templates'
	#profilName = 'ragzdazdazogoa'
	main(profilPath,templatePath,profilName)