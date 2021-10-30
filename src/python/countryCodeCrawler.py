import requests
from bs4 import BeautifulSoup

print("----- Crawling Start..-----")
URL = 'https://www.iban.com/country-codes'

htmlResponse = requests.get(URL).text

countryCodeRows = BeautifulSoup(htmlResponse, 'html.parser').find_all('tr')
for i in range(1, len(countryCodeRows)):
    eachItem = countryCodeRows[i].find_all('td')
    print()
    print("INSERT INTO country_code VALUES (",
          "country_name = '", eachItem[0].text + "', ",
          "alpha2_code = '", eachItem[1].text + "', ",
          "alpha3_code = '", eachItem[2].text + "', ",
          "numeric_code = ", eachItem[3].text,
          " );", sep="")

print("----- END -----")
