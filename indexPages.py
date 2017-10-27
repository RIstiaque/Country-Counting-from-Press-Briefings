##################
# Rifatul Istiaque
# indexPages.py
##################
import bs4
import requests
import os, sys, os.path

def dlPage(url, pgNum):
    '''
    Stores each page of the press briefing into the directory.
    '''
    try: # Create a directory
        os.mkdir('indexPages')
    except: # Do nothing if the directory already exists.
        print()
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    counter = 0 # Keep count of the page number.
    while (soup.h2.text != 'Error 404'): # Stop when a page gives a 404 error.
        file1 = open('indexPages/' + str(counter) + '.html', "w")
        file1.write(str(soup))
        file1.close()
        counter += 1
        response = requests.get(url + pgNum + str(counter)) # Create new resposne and soup object.
        soup = bs4.BeautifulSoup(response.text, "lxml")
    
        
    

def main():
    '''
    This program will store the index pages of the press briefings.
    '''
    url = 'http://csweb.millersville.edu/~sschwartz/mirror/www.whitehouse.gov/briefing-room/press-briefings'
    pgNum = '%3fpage=' # Beings on Page 2.
    dlPage(url, pgNum)

main()
    
    
    
    
