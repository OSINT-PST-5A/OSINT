import os

def pseudoChoiced():
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
	elif QueryApplication == "nexfil":		
		os.system('python3 nexfil.py -u ' + QueryPseudo)
	elif QueryApplication == "instagram-scraper":
		os.system('instagram-scraper ' + QueryPseudo)

	QueryPseudo=input("Appuyer sur entrée pour retourné au menu")
	informationRetrieved()

def emailChoiced():
	print("2 Email")
	print(os.listdir())
	QueryPseudo=input("Appuyer sur entrée pour retourné au menu")
	informationRetrieved()


def commentaireChoiced():
	print("3 Commentaire")
	print(os.listdir())
	QueryPseudo=input("Appuyer sur entrée pour retourné au menu")
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




