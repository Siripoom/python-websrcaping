import requests
from bs4 import BeautifulSoup

url = "https://www.borntodev.com/blog/"
web_data = requests.get(url)


soup = BeautifulSoup(web_data.text,'html.parser')
find_word = soup.find_all("h3",{"class":"title"})

print("Articles on https://www.borntodev.com/blog/")
for i in find_word:
    i = str(i).split('<h3 class="title">')
    i = str(i).split('</h3>')[0]
    print(i,'\n')