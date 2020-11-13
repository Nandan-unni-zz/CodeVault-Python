import requests
import lxml.html as lh
import pandas as pd
import re

URL = "https://lsgkerala.gov.in/plandashboard/Plan/Topperstailors.php?cmbfinyr=23"

#Create a handle, page, to handle the contents of the website
page = requests.get(URL)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tables = doc.xpath('//tr')

data = {}
pos = 1

for line in tables:
    table = {1: []}
    print("\n")
    for word in line:
        print(word.text_content())
        table[1].append(str(word.text_content()))
    data[pos] = table
    pos = pos + 1

totBud = []
totExp = []
bSum = 0
eSum = 0
count = 0

for table in data.values():
    if table[1][0] == "Sl NO":
        totBud.append(bSum)
        totExp.append(eSum)
        eSum = 0
        bSum = 0
        count = 0
        continue
    if len(table[1]) == 6:
        count = count + 1
        bSum = bSum + float(table[1][3])
        eSum = eSum + float(table[1][4])
    else:
        bSum = bSum + float(table[1][2])
        eSum = eSum + float(table[1][3])
    if count == 250:
        totBud.append(bSum)
        totExp.append(eSum)

for tot in totBud:
    print(f"Total Budget Table {totBud.index(tot) + 1}: {tot}")

print("\n")

for tot in totExp:
    print(f"Total Expenditure Table {totExp.index(tot) + 1}: {tot}")
