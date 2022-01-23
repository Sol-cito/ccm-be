from json.tool import main
import requests
import os
from bs4 import BeautifulSoup

path_dir = './src/flyway/sql/'
flyway_fileName = 'V1_101__insert_into_country_code_table.sql'
URL = 'https://www.iban.com/country-codes'


def handleSpecialCharacter(input):
    output = ""
    for i in range(len(input)):
        if input[i] == "'":
            continue
        output += input[i]
    return output


def checkIfFileExists(fileName):
    file_list = os.listdir(path_dir)
    return fileName in file_list


def startCrawlingAndMakeFile(flyway_fileName):
    print("----- START -----")

    htmlResponse = requests.get(URL).text

    newFile = open(path_dir + flyway_fileName, 'w', encoding='UTF-8')

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
            + " ); \n"
        newFile.write(row)

    print("----- END -----")


if __name__ == '__main__':
    if not checkIfFileExists(flyway_fileName):
        startCrawlingAndMakeFile(flyway_fileName)