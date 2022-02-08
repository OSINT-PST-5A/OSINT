import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
import getpass

#Arg1: Cible, arg2: pathToDownloadedPhotos, arg3: id_connexion, arg4: mdp_connexion

#Email, mdp, cible
print(os.getcwd())

#Get user informations
nbArgument = len(sys.argv)
if nbArgument == 3: 
    facebook_user_targeted=sys.argv[1]
    facebook_id=input("Veuillez insérer votre identifiant facebook : ")
    facebook_password=getpass.getpass(prompt="Veuillez insérer votre mot de passe facebook : ")
elif nbArgument == 5:
    facebook_user_targeted=sys.argv[1]
    facebook_id=sys.argv[3]
    facebook_password=sys.argv[4]
else:
    sys.exit()

pathToDownloadedPhotos=sys.argv[2]

#Path to the chrome driver
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
#Options to hide chrome
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")

#activate chromedriver
chromeService = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=chromeService, options=chrome_options)

#Open the target webpage
driver.get("http://fr-fr.facebook.com")

#Accept cookies
cookie = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-cookiebanner='accept_button']"))).click()

#logs we will to connect to facebook
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#Enter the logs into the website
username.clear()
username.send_keys(facebook_id)
password.clear()
password.send_keys(facebook_password)

#Simulate the login button click
logginButton=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)

#Accept cookies
#time.sleep(5)
#cookie3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Autoriser tous les cookies']"))).click()

#https://www.facebook.com/flash.flash.5496/photos_of
images = []
for i in ['photos_by']:
    driver.get("https://www.facebook.com/" + facebook_user_targeted + "/" + i + "/")
    time.sleep(5)

    n_scrolls = 2
    for j in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        anchors = driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]

        for a in anchors:
            driver.get(a)
            time.sleep(5)
            img = driver.find_elements_by_tag_name("img")
            images.append(img[0].get_attribute("src"))

#create the directory
os.mkdir(pathToDownloadedPhotos)

counter=0
for image in images:
    save_as = os.path.join(pathToDownloadedPhotos, str(counter) + '.png')
    wget.download(image, save_as)
    counter += 1

print("Images saved in " + pathToDownloadedPhotos)