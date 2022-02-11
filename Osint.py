import os
import glob
import sys
sys.path.append('.Ressource/Scripts/')
import Profil_Generator
import getpass

#Global variables
pathResult = '/.Resultats/'
pathProfilResult = pathResult + 'Profiles/'
pathTemplate =  '/.Ressource/Templates'
cwd = os.getcwd()
home = os.getenv('HOME')


def deleteUnnecessaryDataFromFile(completeFilePath, programName):

	#On ouvre le fichier pour récupérer 
	file = open(completeFilePath, "r")
	lines = file.readlines()
	file = open(completeFilePath, "w")
	#sherlock
	if (programName == "sherlock"):
		for line in lines:
			if line != lines[-1]:
				file.write(line)
	#nexfil
	if (programName == "nexfil"):
		for line in lines:
			if line.startswith('http'):
				file.write(line)
	#holehe
	if (programName == "holehe"):
		for line in lines:
			if line.startswith('[+]') and "Email used" not in line:
				file.write(line.replace("[+] ", ""))
	file.close()
	#h8mail
	if (programName == "h8mail"):
		if len(lines) == 1:
			print("Fichier h8mail vide, il va donc être supprimé")
			os.system("rm " + completeFilePath)
		for line in lines:
			if line != lines[0]:
				file.write(line)






def pseudoMenu():
	
	queryPseudo=input("Choissisez un Pseudo : ")
	list = [a for a in sorted(os.listdir('Pseudo')) ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if  QueryApplication == 0:
		os.chdir('Pseudo/')
		os.system('python3 facebook-Scraper.py ' + queryPseudo + " " + cwd + pathResult + '/facebook_scraper_'+queryPseudo)
		os.chdir(cwd)		
	elif QueryApplication == 1 :
		os.system('instagram-scraper ' + queryPseudo)			
	elif QueryApplication == 2:
		os.chdir('Pseudo/')
		os.system('python3 myAnimeList-Script.py ' + queryPseudo + ' ' + sys.argv[1])
		os.system('mv ./myAnimeList_' + queryPseudo +".json " + cwd + pathResult +'myAnimeList_'+queryPseudo+'.json' )
		os.chdir(cwd)
			
	elif QueryApplication == 3:
		os.chdir('Pseudo/nexfil/')	
		os.system('python3 nexfil.py -u ' + queryPseudo )
		os.system('mv '+ home + '/.local/share/nexfil/dumps/* '+ cwd + pathResult +'nexfil_'+queryPseudo+'.txt' )
		deleteUnnecessaryDataFromFile(cwd + pathResult +'nexfil_'+queryPseudo+'.txt', "nexfil")
		os.chdir(cwd)		
	elif QueryApplication == 4:
		os.system('python3 Pseudo/sherlock/sherlock/sherlock.py ' + queryPseudo + ' --timeout 1 --output ' +  cwd + pathResult + 'sherlock_'+queryPseudo+'.txt')
		deleteUnnecessaryDataFromFile(cwd + pathResult + 'sherlock_'+queryPseudo+'.txt', "sherlock")
	elif QueryApplication == 5:
		os.system('twint -u' + queryPseudo)
	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()



def emailMenu():
	
	queryEmail=input("Choissisez un Email : ")
	list = [a for a in sorted(os.listdir('Email'))]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if QueryApplication == 0:
		os.system('h8mail -o '+ cwd + pathResult+'h8mail_'+queryEmail+'.txt -t '+ queryEmail)
		deleteUnnecessaryDataFromFile(cwd + pathResult+'h8mail_'+queryEmail+'.txt', "h8mail")
	elif QueryApplication == 1:
		os.system('holehe ' + queryEmail+  ' --only-used --no-color >> '+  cwd + pathResult + 'holehe_'+queryEmail+'.txt' )
		deleteUnnecessaryDataFromFile(cwd + pathResult + 'holehe_'+queryEmail+'.txt', "holehe")


	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()

def commentaireMenu():
	
	list = [a for a in sorted(os.listdir('Commentaire')) ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if QueryApplication == 0:
		os.system('python3 Commentaire/popularInCity.py')
	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()

def googleDorksMenu():
	list = [a for a in sorted(os.listdir('Google-dorks')) ]
	showMenu("logo.txt", list)
	QueryApplication=chooseMenuOption(len(list))
	if QueryApplication == 0:
		os.system('python3 Google-dorks/dorks-eye/dorks-eye.py')
	Query=input("Appuyer sur entrée pour retourné au menu")
	mainMenu()

def automaticMenu():
	queryPseudo=input("Choissisez un Pseudo : ")
	queryEmail=input("Choissisez un Email : ")
	queryUserWill=input("Souhaitez récupérer les photos d'un compte Facebook lié à la personne ? (Si oui vous devrez entrer les identifiants de votre compte pour que la récupération s'opère) - y/n : ")
	folderName = queryPseudo + '_' + queryEmail
	folderGeneration(pathProfilResult, folderName)

	if queryUserWill == 'y':
		queryUserTargeted=input("Donner le nom de l'utilisateur inscrit dans l'url : ")
		queryPseudoLog=input("Veuillez donner votre identifiant de connexion (mail/téléphone) : ")
		queryPasswordLog=getpass.getpass(prompt="Veuillez insérer votre mot de passe facebook : ")
		os.system('python3 Pseudo/facebook-Scraper.py ' + queryUserTargeted + " " + cwd + pathProfilResult +folderName+ '/facebook_scraper_'+queryPseudo + " " + queryPseudoLog + " " + queryPasswordLog)

		
	os.system('python3 Pseudo/sherlock/sherlock/sherlock.py ' + queryPseudo + ' --timeout 1 --output ' +  cwd + pathProfilResult +folderName+ '/sherlock_'+queryPseudo+'.txt')	
	os.system('h8mail -o '+ cwd + pathProfilResult+folderName+'/h8mail_'+queryEmail+'.txt -t '+ queryEmail)
	os.system('holehe ' + queryEmail+  ' --only-used --no-color >> '+  cwd + pathProfilResult+folderName+ '/holehe_'+queryEmail+'.txt' )
	os.chdir('Pseudo/nexfil/')	
	os.system('python3 nexfil.py -u ' + queryPseudo )
	os.system('mv '+ home + '/.local/share/nexfil/dumps/* '+ cwd + pathProfilResult+ folderName +'/nexfil_'+queryPseudo+'.txt' )
	os.chdir(cwd)
	
	#Delete uncessary data
	deleteUnnecessaryDataFromFile(cwd + pathProfilResult +folderName+ '/sherlock_'+queryPseudo+'.txt', "sherlock")
	deleteUnnecessaryDataFromFile(cwd + pathProfilResult+ folderName +'/nexfil_'+queryPseudo+'.txt', "nexfil")
	deleteUnnecessaryDataFromFile(cwd + pathProfilResult+folderName+ '/holehe_'+queryEmail+'.txt', "holehe")
	deleteUnnecessaryDataFromFile(cwd + pathProfilResult+folderName+'/h8mail_'+queryEmail+'.txt', "h8mail")

	nexfilFile = open(cwd + pathProfilResult + folderName +"/nexfil_" + queryPseudo + ".txt", "r")
	sherlockFile = open(cwd + pathProfilResult + folderName + "/sherlock_" + queryPseudo + ".txt", "r")

	if ( ('https://myanimelist.net/profile/' + queryPseudo in nexfilFile.read()) or 'https://myanimelist.net/profile/' + queryPseudo in sherlockFile.read()):
		print("Lancement du script myAnimeList !")
		os.system("python3 ./Pseudo/myAnimeList-Script.py " + queryPseudo + " " + sys.argv[1])
		print("Le script myAnimeList a fini son travail avec succès !")
		os.system("mv myAnimeList_" + queryPseudo +".json " + cwd + pathProfilResult+ folderName)

	Profil_Generator.main(cwd+pathProfilResult+folderName,cwd+pathTemplate,folderName)


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
	list = [a for a in sorted(os.listdir()) if (os.path.isdir(a) and not a.startswith("."))]
	print(list)
	list.insert(0,"Exit")
	list.insert(5,"Automatic")
	showMenu("logo.txt", list)
	option=chooseMenuOption(len(list))
	if option == 0:
		exit()
	elif option == 1:
		commentaireMenu()
	elif option == 2:	
		emailMenu()
	elif option == 3:
		googleDorksMenu()
	elif option == 4:
		pseudoMenu()	
	elif option == 5:
		automaticMenu()
		

if __name__ == "__main__":
    mainMenu()
