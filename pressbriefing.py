#########################
# Rifatul Istiaque
# pressbriefing.py
#########################

import bs4
import requests


def retrieveTime(tag, site):
    """
    Finds the class the time is located in and then returns the formated time.
    """
    start = tag.find('a', href=True)['href']
    response2 = requests.get(site + start[2:])
    pressSite = bs4.BeautifulSoup(response2.text, "lxml")
    time = pressSite.find('div', class_="field-item even")
    time = retrieveCorrectP(time)
    return(fixTime(str(time.encode('utf-8'))))


def retrieveCorrectP(tag):
    """
    This function will find and return the time in a string.
    """
    for p in range(0, len(tag.find_all('p'))):
        temp = str(tag.find_all('p')[p].next_element.encode('utf-8'))
        if (48 <= ord(temp[6]) <= 59):
            return temp
    print("Failed to retrieve correct time stamp.")
    return 0
    

def fixTime(time):
    """
    This function will cut the string to display the correct time and return it.
    """
    while (48 > ord(time[0]) or 59 < ord(time[0])):
        time = time[1:]
    while (ord(time[-1]) != 84):
        time = time[:-1]
    return time


def main():
    """
    The purpose of this program is to print the press conference's time of release
    """
    site = 'http://csweb.millersville.edu/~sschwartz/mirror/www.whitehouse.gov'
    part = '/briefing-room/press-briefings'
    response = requests.get(site + part)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    start = soup.find('div', class_="view-content")
    print(retrieveTime(start, site))

main()
    
    
    
    
    
    
