import os
import glob
import sys
sys.path.append('.Ressource/Scripts/')
import Profil_Generator


pathResult = '/.Resultats/Profiles/'
pathTemplate =  '/.Ressource/Templates'
cwd = os.getcwd()
home = os.getenv('HOME')

def pseudoMenu():
	
	
	queryPseudo=input("Choissisez un Pseudo : ")
	list = [a for a in os.listdir('Pseudo') ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if  QueryApplication == 0:
		os.chdir('Pseudo/')
		os.system('python3 facebook-Scraper.py ' + queryPseudo)
		os.chdir(cwd)		
	elif QueryApplication == 1 :
		os.system('instagram-scraper ' + queryPseudo)			
	elif QueryApplication == 2:
		os.chdir('Pseudo/')
		print("python3 myAnimeList-Script.py " + queryPseudo + ' ' + sys.argv[1])
		os.system('python3 myAnimeList-Script.py ' + queryPseudo + ' ' + sys.argv[1] )
		os.chdir(cwd)
			
	elif QueryApplication == 3:
		os.chdir('Pseudo/nexfil/')	
		os.system('python3 nexfil.py -u ' + queryPseudo )
		os.system('mv '+ home + '/.local/share/nexfil/dumps/* '+ cwd + pathResult +'nexfil_'+queryPseudo+'.txt' )
		os.chdir(cwd)		
	elif QueryApplication == 4:
		os.system('python3 Pseudo/sherlock/sherlock/sherlock.py ' + queryPseudo + ' --timeout 1 --output ' +  cwd + pathResult + 'sherlock_'+queryPseudo+'.txt')
	elif QueryApplication == 5:
		os.system('twint -u' + queryPseudo)
	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()

def emailMenu():
	
	queryEmail=input("Choissisez un Email : ")
	list = [a for a in os.listdir('Email') ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if QueryApplication == 0:
		os.system('h8mail -o '+ cwd + pathResult+'h8mail_'+queryEmail+'.txt -t '+ queryEmail)
	elif QueryApplication == 1:
		os.system('holehe ' + queryEmail+  ' --only-used --no-color >> '+  cwd + pathResult + 'holehe_'+queryEmail+'.txt' )

	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()


def commentaireMenu():
	

	list = [a for a in os.listdir('Commentaire') ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if QueryApplication == 0:
		os.system('python3 Commentaire/popularInCity.py')
	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()

def automaticMenu():
	queryPseudo=input("Choissisez un Pseudo : ")
	queryEmail=input("Choissisez un Email : ")
	folderName = queryPseudo + '_' + queryEmail
	folderGeneration(pathResult, folderName)	
	os.system('python3 Pseudo/sherlock/sherlock/sherlock.py ' + queryPseudo + ' --timeout 1 --output ' +  cwd + pathResult +folderName+ '/sherlock_'+queryPseudo+'.txt')	
	os.system('h8mail -o '+ cwd + pathResult+folderName+'/h8mail_'+queryEmail+'.txt -t '+ queryEmail)
	os.system('holehe ' + queryEmail+  ' --only-used --no-color >> '+  cwd + pathResult+folderName+ '/holehe_'+queryEmail+'.txt' )
	os.chdir('Pseudo/nexfil/')	
	os.system('python3 nexfil.py -u ' + queryPseudo )
	os.system('mv '+ home + '/.local/share/nexfil/dumps/* '+ cwd + pathResult+ folderName +'/nexfil_'+queryPseudo+'.txt' )
	os.chdir(cwd)
	print( cwd +"  pathResult  " + pathResult + "folderName" + folderName)

	Profil_Generator.main(cwd+pathResult+folderName,cwd+pathTemplate,folderName)


def folderGeneration(path, folderName):
	os.system('mkdir .Resultats/Profiles/' + folderName )


def showMenu(fileName, menuList):
	os.system('clear')
	file = open(".Ressource/"+fileName, "r")
	print(file.read())
	i = 0
	for option in menuList:
		print(str(i) + " : " + option + "\n")
		i += 1
	



def chooseMenuOption(max):
	while(True):
		try:
			option=int(input("Choisissez une option : "))
			while(option < 0 or option > max):
				option=int(input("Choisissez une option entre 0 et " + str(max) + " : "))
			break
		except ValueError:
			print("Veuillez entre un nombre entre 0 et " + str(max) + " : ")
			continue	
	return option


def mainMenu():
	os.system('clear')
	list = [a for a in os.listdir() if (os.path.isdir(a) and not a.startswith("."))]
	list.insert(0,"Exit")
	list.insert(4,"Automatic")
	showMenu("logo.txt", list)
	option=chooseMenuOption(len(list))
	if option == 0:
		exit()
	elif option == 1:
		commentaireMenu()
	elif option == 2:	
		emailMenu()
	elif option == 3:
		pseudoMenu()
	elif option == 4:
		automaticMenu()
		

if __name__ == "__main__":
    mainMenu()