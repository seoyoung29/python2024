import requests
from bs4 import BeautifulSoup
url="https://www.melon.com/chart/index.htm"
hearers={"User-Agent":"like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"}
response = requests.get(url,headers=hearers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
result_list = soup.select(".lst50")
print(response)
data=[]
print(len(result_list[0]))
for res in result_list:
    r=res.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a")   
    data.append(r.text)
    print(data)
import csv
with open("melon.csv", mode="w", newline="\n", encoding='utf-8') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow([d])
import csv
with open("melon.csv", mode="w", newline="\n", encoding='utf-8') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow([d])





