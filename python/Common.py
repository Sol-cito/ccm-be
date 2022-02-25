import os

PATH_DIR = './src/flyway/sql/'


def handleSpecialCharacter(input):
    output = ""
    for i in range(len(input)):
        if input[i] == "'":
            continue
        output += input[i]
    return output


def checkIfFileExists(fileName):
    file_list = os.listdir(PATH_DIR)
    return fileName in file_list
