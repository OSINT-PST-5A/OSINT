import os

def pseudoChoiced():
	cwd = os.getcwd()
	QueryPseudo=input("Choissisez un Pseudo : ")
	os.chdir("Pseudo")
	list = os.listdir();
	print(list)
	QueryApplication=input("Choissisez votre application : ")
	os.chdir(QueryApplication)
	if QueryApplication == "twint":
		os.system('twint -u' + QueryPseudo)
	elif QueryApplication == "sherlock":
		os.chdir(QueryApplication)
		os.system('python3 sherlock.py ' + QueryPseudo + ' --timeout 10')
		os.system('cd ../')
	elif QueryApplication == "nexfil":		
		os.system('python3 nexfil.py -u ' + QueryPseudo)
	elif QueryApplication == "instagram-scraper":
		os.system('instagram-scraper ' + QueryPseudo)

	
	Query=input("Appuyer sur entrée pour retourné au menu")
	os.chdir(cwd)
	informationRetrieved()

def emailChoiced():
	cwd = os.getcwd()
	QueryEmail=input("Choissisez un Email : ")
	os.chdir("Email")
	list = os.listdir();
	print(list)
	QueryApplication=input("Choissisez votre application : ")
	if QueryApplication == "holehe":
		os.chdir(QueryApplication)
		os.system('holehe ' + QueryEmail)
	if QueryApplication == "h8mail":
		os.chdir(QueryApplication)
		os.system('h8mail -t ' + QueryEmail)


	Query=input("Appuyer sur entrée pour retourné au menu")
	os.chdir(cwd)
	informationRetrieved()


def commentaireChoiced():
	cwd = os.getcwd()
	os.chdir("Commentaire")
	print(os.listdir())
	QueryApplication=input("Choissisez votre application : ")
	if QueryApplication == "popularInCity" or "popularInCity.py":
		os.system('python3 popularInCity.py')
	Query=input("Appuyer sur entrée pour retourné au menu")
	os.chdir(cwd)
	informationRetrieved()

def informationRetrieved():
	os.system('clear')
	print("0 : Exit\n1 : Pseudo\n2 : Email\n3 : Commentaire\n")
	Query=int(input("Choissisez un chiffre : "))
	if Query == 0:
		exit()
	elif Query == 1:
		pseudoChoiced()
	elif Query == 2:
		emailChoiced()
	elif Query == 3:	
		commentaireChoiced()




print("Bonjour, quelles informations disposez-vous ?")
informationRetrieved()




