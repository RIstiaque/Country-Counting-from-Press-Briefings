##################
# Rifatul Istiaque
# getBriefings.py
##################

import requests
import bs4
import os

def dlPressBriefs():
    urlPart = 'http://csweb.millersville.edu/~sschwartz/mirror/www.whitehouse.gov/'
    file1 = 'a'
    counter = 0 # Current page number.
    briefCounter = 0 # Current brief number
    file1 = open('indexPages/' + str(counter) + '.html', "r")
    cpt = sum([len(files) for r, d, files in os.walk("./indexPages")])
    while (counter != cpt):
        soup = bs4.BeautifulSoup(file1, "lxml")
        links = soup.find('div', class_="view-content")
        numLinks = len(links.find_all('a'))
        for a in range(0, numLinks):
            print(briefCounter)
            file2 = open('pressBriefings/' + str(briefCounter) + '.html', "w")
            content = links.contents[(2*a) + 1].find('a', href=True)['href']
            response = requests.get(urlPart + content[2:])
            soup = bs4.BeautifulSoup(response.text, "lxml")
            title = soup.find('div', class_="panel-pane pane-node-title").find('h1')
            file2.write(str(title) + '\n')                        
            body = soup.find('div', class_="field field-name-field-forall-body field-type-text-long field-label-hidden forall-body")
            file2.write(str(body.encode('utf-8')))
            file2.close()
            briefCounter += 1
        counter += 1
        file1.close()
        try:
            file1 = open('indexPages/' + str(counter) + '.html', "r")
        except:
            a = 0
    file1.close()

        
        

def main():
    try:
        os.mkdir('pressBriefings')
    except:
        print()
    dlPressBriefs()

main()
