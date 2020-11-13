USERNAME = "AbhinavRajesh"

import requests, sys
from bs4 import BeautifulSoup

try:
    profPage = requests.get(f"https://github.com/{USERNAME}")
    repoPage = requests.get(f"https://github.com/{USERNAME}?tab=repositories")
    followingPage = requests.get(f"https://github.com/{USERNAME}?tab=following")
    followersPage = requests.get(f"https://github.com/{USERNAME}?tab=followers")
except requests.exceptions.ConnectionError:
    print("No Internet Connection")
    sys.exit()

profPage = BeautifulSoup(profPage.content, 'html.parser')
repoPage = BeautifulSoup(repoPage.content, 'html.parser')
followingPage = BeautifulSoup(followingPage.content, 'html.parser')
followersPage = BeautifulSoup(followersPage.content, 'html.parser')

user = {}

for data in profPage.find_all("span", class_="p-name"):
    user["name"] = str(data.text)

for data in profPage.find_all("span", class_="p-nickname"):
    user["username"] = str(data.text)

for data in profPage.find_all("img", class_="avatar-user"):
    user["avatar"] = str(data.get("src"))

for data in profPage.find_all("div", class_="p-note"):
    user["bio"] = str(data.text)

for data in profPage.find_all("span", class_="p-org"):
    user["organization"] = str(data.text)

for data in profPage.find_all("span", class_="p-label"):
    user["place"] = str(data.text)

for data in profPage.find_all("div", class_="user-status-emoji-container"):
    user["status"] = str(data.text)

for data in profPage.find_all("div", class_="user-status-message-wrapper"):
    user["status-msg"] = str(data.text)

user["repos"] = []
for data in repoPage.find_all("h3", class_="wb-break-all"):
    user["repos"].append(str(data.text))

user["following"] = []
for data in followingPage.find_all("span", class_="link-gray"):
    user["following"].append(str(data.text))

user["followers"] = []
for data in followersPage.find_all("span", class_="link-gray"):
    user["followers"].append(str(data.text))

user["following"].pop(0)
user["followers"].pop(0)

for data in user:
    if type(user[data]) == str:
        if "\n" in user[data]:
            user[data] = user[data].replace("\n", "")
    else:
        user[data] = [line.replace("\n", "") for line in user[data]]
        user[data] = [line.replace(" ", "") for line in user[data]]

print(user)
