import bs4
import requests

def main():
    """
    Return the total # of execution in Texas between the starting year
    and the ending year.
    """
    numExec = 0
    response = requests.get('http://www.tdcj.state.tx.us/death_row/dr_executions_by_year.html')
    soup = bs4.BeautifulSoup(response.text, "lxml")
    startYear = int(input('Enter starting year: '))
    endYear = int(input('Enter ending year: '))                    
    years = endYear - startYear + 1
    if (startYear == 1982):
        years -= 1
    row = soup.find('tr').next_sibling.next_sibling
    while (int(row.find('th').text.strip()) != endYear):
        row = row.next_sibling.next_sibling
    for i in range(0, years):
        numExec += int(row.find_all('td')[-2].text.strip())
        row = row.next_sibling.next_sibling
    print('Total executions:', numExec)

main()  
