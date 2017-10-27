###########################
# Rifatul Istiaque
# datagov.py
###########################

import bs4
import requests


def main():
    """
    The purpose of this program is to print back the desired dataset title to the user.
    """
    response = requests.get('https://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
    soup = bs4.BeautifulSoup(response.text, "lxml")
    start = soup.find('li', class_="dataset-item has-organization") # Get the class that has the datasets.
    num = int(input("Which dataset? "))
    cur = start
    for sibling in range(1, num): # Used for selecting the right tag.
        for tag in range(0, 6):
           cur = cur.next_sibling # Uniform number of other tags in between list elements to skip.
    print(cur.find('a').text)
        
main()



