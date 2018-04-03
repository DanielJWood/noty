import csv
import requests
from BeautifulSoup import BeautifulSoup
from time import gmtime, strftime
time = strftime("%m/%d/%y %H:%M")

print time

# with open('/home/ec2-user/names2018/bulltron_regional.csv', 'rb') as f:
with open('./fruithandler_regional.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

# url = 'http://www.nameoftheyear.com/2018/04/2018-name-of-year-bulltron-regional.html'
url = 'http://www.nameoftheyear.com/2018/04/2018-name-of-year-fruithandler-regional.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
# print soup

# links = soup.findAll('noscript')

# print links;
links = []

# print(soup.findAll('noscript'))

for link in soup.findAll('noscript'):
    if str(link)[:12] == "<noscript><a":
        links.append(link.find('a').get('href'))    

dataRow = [time]
# print dataRow

for link in links:
    appendix = "?view=results"
    results = requests.get(link + appendix)
    html = results.content
    soup = BeautifulSoup(html)
    names = soup.findAll('div', attrs={'class': 'label'})
    votes = soup.findAll('div', attrs={'class': 'votes'})
    for vote in votes:
        vote = vote.text
        votesCut = vote.find(' votes')
        vote = vote[:votesCut]
        # print vote
        dataRow.append(vote)
    #for name in names:
        #name = name.text
        # votesCut = vote.find(' votes')
        # vote = vote[:votesCut]
        #print name


# print dataRow
your_list.append(dataRow)

# outfile = open("/home/ec2-user/names2018/temp.csv", "wb")
outfile = open("./temp2.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(your_list)








