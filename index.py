"""
get items from sustc download page
"""
from bs4 import BeautifulSoup
import requests

html = requests.get('http://sustc.edu.cn/communication_4_4_5').text
soup = BeautifulSoup(html, 'lxml')

target = soup.find_all("div", "contentP")
p = soup.find_all("p", "menu")
ul = soup.find_all("ul", "table")
if len(p) != len(ul):
    print("Wrong")
    exit(0)
for i in range(0, len(p)):
    print(p[i].find_all('span')[1].get_text())
    lis = ul[i].find_all('li')
    for li in lis:
        a = li.find_all('a')[0]
        print("{ title: '%s', src: 'http://sustc.edu.cn%s'}" % (a.get_text(), a.get('href')))
