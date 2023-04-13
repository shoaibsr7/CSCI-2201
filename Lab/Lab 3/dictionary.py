#!/usr/bin/env python

#CSCI2201 Fall 2021

# Import the datetime library to use its functions
from datetime import datetime

#Password file include with lab
FILENAME = "commonpasswords.txt"


def crackPassword(password, dictionary):

    # Initial time when the test starts and counter
    current = datetime.now()
    count = 0

    #Compare inputted password to the ones in our list
    for entry in dictionary:
        count += 1
        if entry == password:
            time = (datetime.now() - current).microseconds
            print("Found it! Took " + str(count) + " attempts and " + str(time) + " microseconds")
            return

    print("Password not in database. Use alternate cracking method")

if __name__ == "__main__":
    #Open the file
    with open(FILENAME) as f:
        #Read in passwords. Remove excess charaters
        lineList = [line.rstrip('\n') for line in f]

    pw = input("Enter a password: ")

    crackPassword(pw, lineList)
