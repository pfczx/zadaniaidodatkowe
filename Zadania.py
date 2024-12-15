import os
import re



#Dla ułatwienia sprawdzania śćieżki są wklejone w ciała metod
#Pełny projekt wraz z plikami w repozytorium Github


def zadanie1( plikWej :str, plikWyj :str,slowo :str):
    plikWej = 'plikiDoZadan/zad1Wej.txt'
    plikWyj = 'plikiDoZadan/zad1Wyj.txt'

    inputFile = open(plikWej, 'r')
    resultFile = open(plikWyj, 'w')

    line = inputFile.readline()
    lineCount = 0
    while line:
        if slowo in line:
            resultFile.write(str(lineCount)+" "+line)
        line = inputFile.readline()
        lineCount += 1
    inputFile.close()
    resultFile.close()



def zadanie2(path:str):
    path='plikiDoZadan/zad2.txt'
    inputFile = open(path, 'r')
    text = inputFile.read()
    return re.findall(r'[a-zA-Z0-9]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]{2,}', text)

def zadanie3(path:str):
    path='plikiDoZadan/zad3.txt'

    if  os.path.exists(path):
        inputFile = open(path, 'r+')
        lines = inputFile.readlines()
        lastNumber = int(lines[-1].strip('\n'))
        inputFile.write(str(lastNumber + 1))
        inputFile.write('\n')
        inputFile.close()

    else:
        inputFile = open(path, 'w')
        inputFile.write(str(1))
        inputFile.write('\n')
        inputFile.close()

def zadanie4szyfruj(pathInput:str,move:int):
    pathInput='plikiDoZadan/zad4.txt'
    encryptedText=""

    inputFile = open(pathInput, 'r')
    text = inputFile.read()
    inputFile.close()

    for char in text.lower():
        asciiChar = ord(char)
        if asciiChar >= 97 and asciiChar <= 122:
            asciiChar = asciiChar + move
            if asciiChar > 122:
                asciiChar = asciiChar - 123 + 97
        encryptedText += chr(asciiChar)

    outputPath="/_".join(pathInput.rsplit('/'))
    outputFile = open(outputPath, 'w')
    outputFile.write(encryptedText)
    outputFile.close()

def zadanie4deszyfruj(pathInput:str,move:int):
    pathInput = 'plikiDoZadan/_zad4.txt'
    decryptedText = ""

    inputFile = open(pathInput, 'r')
    text = inputFile.read()
    inputFile.close()

    for char in text.lower():
        asciiChar = ord(char)
        if asciiChar >= 97 and asciiChar <= 122:
            asciiChar = asciiChar - move
            if asciiChar < 97:
                asciiChar = asciiChar + 123 - 97
        decryptedText += chr(asciiChar)

    inputFile = open(pathInput, 'w')
    inputFile.write(decryptedText)
    inputFile.close()

def zadanie5(pathInput:str):
    pathInput = 'plikiDoZadan/zad5Wej.txt'
    pathOutputM='plikiDoZadan/zad5WyjM.txt'
    pathOutputW='plikiDoZadan/zad5WyjW.txt'

    inputFile = open(pathInput, 'r',encoding='utf-8')
    lines = inputFile.readlines()
    inputFile.close()

    womanList=[]
    manList=[]
    for person in lines:
        person = person.strip('\n').split(" ")
        if(person[2])=="M":
            manList.append(str(person[0])+" "+str(person[1])+" "+str(65-int(person[3]))+"\n")
        else:
            womanList.append(str(person[0])+" "+str(person[1])+" "+str(60-int(person[3]))+"\n")
    textM="".join(manList)
    textW="".join(womanList)
    outputM = open(pathOutputM, 'w')
    outputW = open(pathOutputW, 'w')
    outputM.write(textM)
    outputW.write(textW)

def zadanie6(pathInput:str):
    pathInput = 'plikiDoZadan/zad6.txt'
    pathOutput='plikiDoZadan/zad6wyj.txt'
    inputFile = open(pathInput, 'r')
    text = inputFile.read()
    inputFile.close()
    listOfWords=re.sub(r'[^\w\s]', '', text).split(" ")
    wordsDict = {}

    for word in listOfWords:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    sortedWordsDict = sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)

    outputFile = open(pathOutput, 'w')
    for word in sortedWordsDict:
        outputFile.write(word[0]+" "+str(word[1])+"\n")
    outputFile.close()
def zadanie10(pathInput:str):
    pathInput='plikiDoZadan/zad10.txt'
    inputFile = open(pathInput, 'r',encoding='utf-8')
    text = inputFile.read()
    inputFile.close()

    charDict = {}
    for char in text:
        if ord(char) >=97 and ord(char) <= 122 :
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
    sortedDict = dict(sorted(charDict.items()))
    listOfStarLines=[]
    for char in sortedDict:
        starsNumber=int((charDict[char] / max(charDict.values())) * 50)
        starLine="*"*starsNumber+" " * (50-starsNumber)
        listOfStarLines.append(starLine)

    counter=0
    for char in sortedDict:
        print(str(char)+" "+listOfStarLines[counter]+" "+str(charDict[char]))
        counter+=1





def confusion_matrix(pathInput:str):

    results = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for file in os.listdir('daneDoDodatkowego'):

        inputFile = open('daneDoDodatkowego/'+file, 'r',encoding='utf-8')
        lines = inputFile.readlines()
        lines.reverse()
        inputFile.close()

        selectedLines=[]
        counter=0
        line=""
        while line != "=== Confusion Matrix ===\n":
            line = lines[counter]
            selectedLines.append(line)
            counter+=1

        linesForMatrix = selectedLines[-7:-3]
        linesForMatrix.reverse()
        for i in range(len(linesForMatrix)):
            counter=0
            stringNumber=""
            for char in linesForMatrix[i]:
                if counter <4:
                    if char.isdigit():
                        stringNumber+=char
                    else:
                        if stringNumber!="":
                            results[i][counter]+=int(stringNumber)
                            stringNumber=""
                            counter+=1

    fileOutput=open('WYNIKI.txt', 'w')
    for i in range(len(results)):
        fileOutput.write(str(results[i])+"\n")
    fileOutput.close()

confusion_matrix("")






