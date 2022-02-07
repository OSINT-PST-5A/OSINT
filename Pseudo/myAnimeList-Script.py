from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json

#Essais avec les utilisateurs: limosaee, moumous95, EmreH


class Anime:
    def __init__(self, title, score, type, progress, tag):
        self.title = title
        self.score = score
        self.type = type
        self.progress = progress
        self.tag = tag


url = "https://myanimelist.net/animelist/" + sys.argv[1] + "?status=7"

#Path to the chrome driver
CHROMEDRIVER_PATH = sys.argv[2]
#Options to hide chrome
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")

#activate chromedriver
chromeService = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=chromeService, options=chrome_options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, features="html.parser")
allAnime = soup.findAll('tbody', {"class": "list-item"})
watching = []
completed = []
planToWatch = []
onHold = []
dropped = []
for anime in allAnime:
    animeInformation = anime.find("tr", {"class" : "list-table-data"})
    #Récupération du titre de l'animé
    animeTitleLocation = animeInformation.find("td", {"class" : "data title clearfix"})
    animeTitle = animeTitleLocation.find("a", {"class" : "link sort"})
    #Récupération de la note attrbuée par l'utilisateur
    animeScoreLocation = animeInformation.find("td", {"class" : "data score"})
    animeScore = animeScoreLocation.find("span")
    #Récupération du type de l'animé (TV, Special, Movie)
    animeType = animeInformation.find("td", {"class" : "data type"})
    #Récupération de la progression de l'utilisateur (intéressant pour le statut watching)
    animeProgress = animeInformation.find("td", {"class" : "data progress"})
    #Récupération d'un éventuel Tag de l'utilisateur sur un animé
    animeTag = animeInformation.find("td", {"class" : "data tags"})
    #On enregistre l'objet Json dans la bonne liste
    animeStatus = animeInformation.select("td[class^=\"data status\"]")
    anime = Anime(
        animeTitle.text,
        animeScore.text.strip(),
        animeType.text.strip(),
        animeProgress.text.replace(" ", "").replace("\n", ""),
        animeTag.text
    )
    if( animeStatus[0]["class"][2] == "plantowatch"):
        planToWatch.append(anime)
    if (animeStatus[0]["class"][2] == "completed"):
        completed.append(anime)
    if (animeStatus[0]["class"][2] == "watching"):
        watching.append(anime)
    if (animeStatus[0]["class"][2] == "dropped"):
        dropped.append(anime)
    if (animeStatus[0]["class"][2] == "onhold"):
        onHold.append(anime)


file = open("myAnimeList_" + sys.argv[1] + ".json", "w")
#Conversion des lists au format json et écriture du fichier json
file.write(
    "{\"Watching\":" + json.dumps([ob.__dict__ for ob in watching]) +
    ", \"Completed\":" + json.dumps([ob.__dict__ for ob in completed]) +
    ", \"onHold\":" + json.dumps([ob.__dict__ for ob in onHold]) +
    ", \"dropped\":" + json.dumps([ob.__dict__ for ob in dropped]) +
    ", \"planToWatch\":" + json.dumps([ob.__dict__ for ob in planToWatch]) +
    "}"
)
file.close()

"""animeLists = []
animeLists.append(watching)
animeLists.append(completed)
animeLists.append(onHold)
animeLists.append(dropped)
animeLists.append(planToWatch)
jsonStr = json.dumps([[ob.__dict__ for ob in subList] for subList in animeLists], indent=4)"""