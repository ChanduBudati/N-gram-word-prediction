#!/usr/bin/env python3

'''
Chandu Budati
CSCI 6350-001
Project 1
Due: 02/12/18
'''

#Ngrams program


import sys
import copy
import random
import time
import math

exclude = {';', '?', ':', '.', '!', ','} #lookup string to clean corpus

#processing input data into a list, lines
traindata = []
with open("tsdc_train.txt") as TrainingFile:
    for line in TrainingFile:
        line = line.strip()
        line = ''.join(ch for ch in line if ch not in exclude)
        traindata.append(line)

# processing test data into a list, testlines
testdata = []
with open("tsdc_test.txt") as TestingFile:
    for line in TestingFile:
        line = line.strip()
        line = ''.join(ch for ch in line if ch not in exclude)
        testdata.append(line)

def createbigram(lines):#create bigrams from train corpus
    bigrams = []
    for line in lines:
        line = '<s> ' + line + ' </s>'
        line = line.split(" ")
        for i in range(len(line)-1):
            bigrams.append((line[i], line[i+1]))
    return bigrams

def createtrigram(lines):#create trigrams from train corpus
    trigrams = []
    for line in lines:
        line = '<s> <s> ' + line + ' </s> </s>'
        line = line.split(" ")
        for i in range(len(line)-2):
            trigrams.append((line[i], line[i+1], line[i+2]))
    return trigrams

def predictBigram(ugram, bigrammodel):#bigram prediction function
#predictBigram(ugram, bigrammodel, bigrams, uniquetokens, utokens):
    if ugram in bigrammodel.keys():
        return bigrammodel[ugram][0]
    else:
        return ""

def predictTrigram(bgram, trigrammodel, bigrammodel):#trigram prediction function
#predictTrigram(bgram, trigrammodel, trigrams, uniquebigrams, btokens, bigrammodel, bigrams, uniquetokens, utokens)
    if bgram in trigrammodel.keys():
        return trigrammodel[bgram][0]
        #initially i ignore equal probabilities and return failure but now i am returning 1st word with max probalility

    else:
        return predictBigram(bgram[1], bigrammodel)

def test(testlines, trigrammodel, bigrammodel):
    random.seed(1000)

    correct = 0
    incorrect = 0
    failed = 0

    for line in testlines:
        line = '<s> <s> ' + line + ' </s> </s>'
        line = line.split(" ")
        rand = random.uniform(2, len(line)-2)
        rand = math.floor(rand)
        #predictoin using trigram

        bgram = (line[rand-2], line[rand-1])

        p = predictTrigram(bgram, trigrammodel, bigrammodel)#predictTrigram(bgram, trigrammodel, trigrams, uniquebigrams, btokens, bigrammodel, bigrams, uniquetokens, utokens)
        if(p == line[rand]):
            correct += 1
        elif(p != ""):
            incorrect += 1
        else:
            failed += 1


    print("correct prediction: " + str(correct))
    print("incorrect prediction: " + str(incorrect))
    print("failed prediction: " + str(failed))

def main():
    #creating bigrams
    ugrams = []
    trainlines = traindata[:] #1st 900 lines in train data
    for line in trainlines:
        line = "<s> " + line + " </s>"
        line = line.split(" ")
        for i in range(len(line)):
            ugrams.append(line[i])


    uniqueugrams = []
    for i in ugrams:
        if i not in uniqueugrams:
            uniqueugrams.append(i)

    bigrams = createbigram(trainlines)

    uniquebigrams= []
    for i in bigrams:
        if i not in uniquebigrams:
            uniquebigrams.append(i)

    # creating bigrammodel
    bigrammodel = dict()
    start = time.time()
    for i in uniquebigrams:
        bcount = bigrams.count(i)
        if i[0] not in bigrammodel.keys():
            bigrammodel[i[0]] = ((i[1], bcount / ugrams.count(i[0])))
        elif (bcount / ugrams.count(i[0])) > bigrammodel[i[0]][1]:
            bigrammodel[i[0]] = (i[1], bcount / ugrams.count(i[0]))
        elif (bcount / ugrams.count(i[0])) == bigrammodel[i[0]][1]:
            bigrammodel[i[0]] = ("", bcount / ugrams.count(i[0]))        
    print(time.time() - start)

    #creating trigrams
    trigrams = createtrigram(trainlines)

    btokens = []
    for line in trainlines:
        line = "<s> <s> " + line + " </s> </s>"
        line = line.split(" ")
        for i in range(len(line)-1):
            btokens.append((line[i],line[i+1]))

    uniquebtokens = []
    for i in btokens:
        if i not in uniquebtokens:
            uniquebtokens.append(i)

    uniquetrigrams = []
    for i in trigrams:
        if i not in uniquetrigrams:
            uniquetrigrams.append(i)

    #creating trigrammodel
    trigrammodel = dict()
    start = time.time()
    for i in uniquetrigrams:
        bcount = trigrams.count(i)
        if (i[0],i[1]) not in trigrammodel.keys():
            trigrammodel[(i[0], i[1])] = (i[2], bcount / btokens.count((i[0], i[1])))
        elif bcount / uniquebtokens.count((i[0],i[1])) > trigrammodel[(i[0],i[1])][1]:
            trigrammodel[(i[0],i[1])] = (i[2], bcount / btokens.count((i[0],i[1])))
        elif bcount / uniquebtokens.count((i[0],i[1])) == trigrammodel[(i[0],i[1])][1]:
            trigrammodel[(i[0],i[1])] = ("", bcount / btokens.count((i[0],i[1])))
    print(time.time() - start)

    print("bigrams extracted: " + str(len(bigrams)))
    print("trigrams extracted: " + str(len(trigrams)))

    #testing
    print("traindata[350:600]")
    testlines = traindata[350:600]
    test(testlines, trigrammodel, bigrammodel)

    print("traindata[:600]")
    testlines = traindata[:600]
    test(testlines, trigrammodel, bigrammodel)

    print("traindata[700:900]")
    testlines = traindata[700:900]
    test(testlines, trigrammodel, bigrammodel)

    print("testdata[:]")
    testlines = testdata[:]
    test(testlines, trigrammodel, bigrammodel)

    print("testdata[:300]")
    testlines = testdata[:300]
    test(testlines, trigrammodel, bigrammodel)

    print("testdata[100:470]")
    testlines = testdata[100:470]
    test(testlines, trigrammodel, bigrammodel)



main()
