"""
File: webcrawler.py
Name: Louis
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        # print(tags)
        for tag in tags:
            data = tag.tbody.text.split()
        # print(data)

        men_total = 0
        women_total = 0
        for i in range(len(data)):
            if i % 5 == 2:
                new_string = data[i].replace(',', '')
                if new_string.isdigit():
                    men_total += int(new_string)
            elif i % 5 == 4:
                new_string = data[i].replace(',', '')
                if new_string.isdigit():
                    women_total += int(new_string)
        print('Male Number: ', men_total)
        print('Female Number: ', women_total)


if __name__ == '__main__':
    main()
