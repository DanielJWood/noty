import csv
import requests
from BeautifulSoup import BeautifulSoup

# url = 'http://www.nameoftheyear.com/2018/04/2018-name-of-year-bulltron-regional.html'
url = 'http://www.nameoftheyear.com/2018/04/2018-name-of-year-fruithandler-regional.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
# print soup

# links = soup.findAll('noscript')

# print links;
links = []
nameList = []

# print(soup.findAll('noscript'))

for link in soup.findAll('noscript'):
    if str(link)[:12] == "<noscript><a":
        links.append(link.find('a').get('href'))    

# dataRow = [time]
# print dataRow

for link in links:
    appendix = "?view=results"
    results = requests.get(link + appendix)
    html = results.content
    soup = BeautifulSoup(html)

    for names in soup.findAll('div', attrs={'class': 'label'}):        
        print names.string
        nameList.append(names.string)    

        
# print nameList

# print dataRow
# your_list.append(dataRow)

# outfile = open("/home/ec2-user/names2018/temp.csv", "wb")
# outfile = open("./temp2.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerows(nameList)








