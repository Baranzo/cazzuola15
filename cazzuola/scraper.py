from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import html



def get_dlib_doc_list():

    doc_list = []

    url = "http://www.dlib.org/title-index.html"

    page = urllib2.urlopen(url)
    page = page.read()

    soup = BeautifulSoup(page, 'lxml')

    tags = soup.find_all('p', class_='archive')

    for tag in tags:
        dict = {}

        a = tag.find_all('a')[0]

        dict['title'] = a.text
        dict['url'] = 'http://www.dlib.org/' + a['href']

        doc_list.append(dict)

    return doc_list

def get_dlib_doc_list_xpath():

    doc_list = []

    page = requests.get('http://dlib.org/title-index.html')
    tree = html.fromstring(page.content)
    texts = tree.xpath('//p[@class="archive"]//a/text()')
    links = tree.xpath('//p[@class="archive"]//a/@href')

    print len(texts)
    print len(links)

    for i in range(len(texts)):
        dict = {}

        dict['title'] = texts[i]
        dict['url'] = links[i]

        doc_list.append(dict)

    return doc_list
