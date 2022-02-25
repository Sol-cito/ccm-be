from json.tool import main
from operator import le
import requests
import Common
from bs4 import BeautifulSoup

path_dir = './src/flyway/sql/'
flyway_fileName = 'V1_101__insert_into_country_code_table.sql'
URL = 'https://www.iban.com/country-codes'


def startCrawlingAndMakeFile(flyway_fileName):
    print("----- START -----")

    htmlResponse = requests.get(URL).text

    newFile = open(path_dir + flyway_fileName, 'w', encoding='UTF-8')

    countryCodeRows = BeautifulSoup(htmlResponse, 'html.parser').find_all('tr')
    startLine = "INSERT INTO country_code (country_name, alpha2_code, alpha3_code, numeric_code) VALUES \n"
    for i in range(1, len(countryCodeRows)):
        eachItem = countryCodeRows[i].find_all('td')
        row = ""
        if (i - 1) % 50 == 0:
            row += startLine
        row += "(" \
            + "'" + Common.handleSpecialCharacter(eachItem[0].text) \
            + "', " \
            + "'" + eachItem[1].text \
            + "', " \
            + "'" + eachItem[2].text \
            + "', " \
            + "" + eachItem[3].text \
            + " ) \n"
        if i % 50 == 0 or i == len(countryCodeRows) - 1:
            row += "; \n"
        elif i % 50 != 0:
            row += ", \n"
        newFile.write(row)

    print("----- END -----")


if __name__ == '__main__':
    if not Common.checkIfFileExists(flyway_fileName):
        startCrawlingAndMakeFile(flyway_fileName)
