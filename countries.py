##################
# Rifatul Istiaque
# countries.py
##################

import bs4
import requests

def listCountries(fIn, soup):
    """
    Input: fIn - file to write to, soup - BeautifulSoup object.
    Write the names of the soverign countries to fIn.
    """
    countryName = soup.find('tr', style = "background:Darkgrey;")
    for a in range(3):
        countryName = countryName.find_next_sibling();
    name = ''
    countryList = []
    while (countryName != None): # Iterate through the table until we reach the last name.
        while (countryName != None and countryName.get('style') != None): # Makes sure NoneTypes and Irrelevent sections don't get mixed in.         
            countryName = countryName.find_next_sibling()
        if countryName != None:
            name = countryName.find('id')
            if (name is None): # If Id is not available then it will use the text in the link.
                name = countryName.find('a').text
            if (name.find(',') != -1): # Takes care of countries with commas in their name.
                part1 = name[0:name.find(',')]
                part2 = name[name.find(',') + 2:]
                name = (part2 + ' ' + part1)
            if (name.find(' and ') != -1): # Makes countries from concatenated phrases.
                partLst = []
                if (name.find(' and the ') != -1):
                    partLst.append(name[0:name.find(' and the ')])
                    partLst.append(name[name.find(' and the ') + 9:])
                else:
                    partLst.append(name[0:name.find(' and ')])
                    partLst.append(name[name.find(' and ') + 5:])
                for country in partLst:
                    if country not in countryList:
                        countryList.append(country)
                        fIn.write(country + '\n')
            elif name not in countryList: # Takes care of duplicates.
                countryList.append(name)
                fIn.write(name + '\n')
            countryName = countryName.find_next_sibling()

def main():
    """
    This program will retrieve a list of sovereign states from Wikipedia and
    store them in a list called countires.txt.
    """
    response = requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states')
    soup = bs4.BeautifulSoup(response.text, "lxml")
    fIn = open('countries.txt', 'w') # Open file for writing.
    listCountries(fIn, soup)
    fIn.close() # Close the file.

main()
