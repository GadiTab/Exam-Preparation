#!/usr/bin/python
import random
from os import system
import sys

shuffle = "Shuffled"
no = ""
userInput = ""


def word(order):
    global userInput
    if order == "Shuffled":
        random.shuffle(questionsList)
    for line in questionsList:
        if userInput.lower() == "exit":
            return
        platformCheck()
        usuageOf(line)


def defini(order):
    global userInput
    if order == "Shuffled":
        random.shuffle(questionsList)
    for line in questionsList:
        if userInput.lower() == "exit":
            return
        platformCheck()
        doesItDescribe(line)


def mix(order):
    global userInput
    if order == "Shuffled":
        random.shuffle(questionsList)
    for line in questionsList:
        if userInput.lower() == "exit":
            return
        platformCheck()
        splitNumber = random.randint(0,1)
        if splitNumber == 0:
            usuageOf(line)
        elif splitNumber == 1:
            doesItDescribe(line)


def doesItDescribe(line):
    global userInput
    print "Here is a description, what does it describe? Type 'Exit' to leave.\n\n" + line.split(" - ")[1]
    userInput = raw_input("Press enter to show the answer...")
    if userInput.lower() == "exit":
        leave()
        return
    print line.split(" - ")[0]
    raw_input("\nPress enter to continue...")


def usuageOf(line):
    global userInput
    print "What is the usage of: '" + line.split(" - ")[0] + "'? Type 'Exit' to leave."
    userInput = raw_input("Press enter to show the answer...\n")
    if userInput.lower() == "exit":
        leave()
        return
    print line.split(" - ")[1]
    raw_input("Press enter to continue...")


def leave():
    print "Closing the program."


def wrong():
    print "Quiz type choice is not existed"
    raw_input("Press enter to continue...")
    menu()


def menu():
    platformCheck()
    print """
What type of quiz would you like to take?
1. Guess each word definition.
2. Read the definition and guess the word it describes.
3. Mixed. Guess words and definitions randomly.
4. Exit the program
"""
    quizType = raw_input("Quiz type number: ")
    if quizType == "4":
        print "Good bye :)"
        return
    platformCheck()
    print """
What order will be the questions?
1. Normal
2. Shuffled
3. Back
"""
    quizOrder = raw_input("Quiz order number: ")
    if quizOrder == "3":
        menu()
        return
    userQuizChoice = quizType + quizOrder
    quizOptions = {
        "11": (lambda : word(no)),
        "12": (lambda : word(shuffle)),
        "21": (lambda : defini(no)),
        "22": (lambda : defini(shuffle)),
        "31": (lambda : mix(no)),
        "32": (lambda : mix(shuffle)),
    }
    quizOptions.get(userQuizChoice, wrong)()


def platformCheck():
    if sys.platform.startswith('win32'):
        windowsClear()
    elif sys.platform.startswith("linux2"):
        linuxClear()


def windowsClear():
    system("cls")


def linuxClear():
    system("clear")


platformCheck()
print """
*** Exam Preparation v1.1 ***  By GadiTab"""
print "\nType the path of your questions files."
path = raw_input("Path: ")
try:
    userFile = open(path, 'r')
    questionsList = userFile.readlines()
    userFile.close()
except:
    print "Wrong file path. File does not exist."
    exit()
menu()