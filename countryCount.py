##################
# Rifatul Istiaque
# countryCount.py
##################

import requests, bs4, os

def main():
    '''
    This function will go through each press briefing and print the total
    country counts to a separate text document.
    '''
    fIn1 = open('countries.txt', 'r')
    numCountryDict = {}
    countryName = fIn1.readlines()
    fIn1.close()
    for country in countryName:
        numCountryDict[country[:-1]] = 0
    cpt = sum([len(files) for r, d, files in os.walk("./pressBriefings")]) # Get the number of items in the directory where the press briefings are stored.
    for count in range(0, cpt): # Go through each press briefing.
        fIn1 = open('pressBriefings/' + str(count) + '.html', "r")
        briefLines = fIn1.readlines()
        for lines in briefLines:
            for word in lines.split():
                for country in numCountryDict: # Increase country count per instance.
                    if country in word:
                        numCountryDict[country] += 1
        fIn1.close()

    fIn1 = open('countryCount.txt', "w")
    for country in  numCountryDict: # Write the country count to text document.
        fIn1.write(str(numCountryDict[country]) + ' ' + str(country) + '\n')
    fIn1.close()

main()
