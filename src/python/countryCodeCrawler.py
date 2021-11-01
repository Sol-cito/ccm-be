import requests
from bs4 import BeautifulSoup


def handleSpecialCharacter(input):
    output = ""
    for i in range(len(input)):
        if input[i] == "'": continue
        output += input[i]
    return output


print("----- Crawling Start..-----")
URL = 'https://www.iban.com/country-codes'
flyway_fileName = 'V1_101__insert_into_country_code_table.sql'

htmlResponse = requests.get(URL).text

newFile = open(flyway_fileName, 'w', encoding='UTF-8')

countryCodeRows = BeautifulSoup(htmlResponse, 'html.parser').find_all('tr')
for i in range(1, len(countryCodeRows)):
    eachItem = countryCodeRows[i].find_all('td')
    row = "INSERT INTO country_code (country_name, alpha2_code, alpha3_code, numeric_code) VALUES (" \
          + "'" + handleSpecialCharacter(eachItem[0].text) \
          + "', " \
          + "'" + eachItem[1].text \
          + "', " \
          + "'" + eachItem[2].text \
          + "', " \
          + "" + eachItem[3].text \
          + " );"
    newFile.write(row)

print("----- END -----")
