#!/usr/bin/env python

#CSCI2201 Fall 2021

# Import the datetime library to use its functions
from datetime import datetime
import itertools
import string

#Upper limit for password length
PASSLEN = 12

class PasswordCracker:

    attempts = 0
    potentialCharacters = ""

    def crackPassword(self, userPassword, complexity):

        if complexity == 1:
            self.potentialCharacters = string.ascii_lowercase  # Only lowercase
        if complexity == 2:
            self.potentialCharacters = string.ascii_letters  # Upper and lowercase
        if complexity == 3:
            self.potentialCharacters = string.printable  # Any printable character

        size = len(userPassword)

        for generatedPassword in itertools.product(self.potentialCharacters, repeat=size):
                # Increase attempt by 1 for every iteration, then join the new generated password
                    self.attempts += 1
                    generatedPassword = ''.join(generatedPassword)

                    if generatedPassword == userPassword:
                        print(generatedPassword)
                        return self.attempts, True

        return self.attempts, False

    def getUserPassword(self):
        """
        Simple method to get the user's password. If it's incorrect, we ask the user to input again.
        """

        userPassword = ""
        complexity = 1

        while (True):
            print("DEMO BRUTEFORCE CRACKER")
            # Prompt the user to enter their chosen password
            userPassword = input("Enter a password (warning long passwords may take awhile): ")

            if len(userPassword) > PASSLEN:
                print("Password should be shorter than " + str(PASSLEN) + "! Try again.\n")
            else:
                break


        for character in userPassword:

            # If we have an uppercase letter, we're testing the 2nd password strength
            if character.isupper() and complexity != 3:
                complexity = 2
            # If we have symbols or numbers, we're testing the 3rd password strength
            if not character.isalpha():
                complexity = 3

        return userPassword, complexity


if __name__ == "__main__":
    # Initialize our password cracker class
    cracker = PasswordCracker()

    # Get the password from the user and the complexity of the password we're testing
    password, complexity = cracker.getUserPassword()
    print("Complexity is: " + str(complexity) + ". Beginning cracking...\n")
    # Initial time when the test starts
    timerStart = datetime.now()

    attempts, success = cracker.crackPassword(password, complexity)

    # Get the current time after your program runs, subtract it from the initial time
    timerEnd = datetime.now()
    totalTime = (timerEnd - timerStart).total_seconds()

    # Output will be the difference in seconds
    print("Password successfully cracked in " + str(totalTime) + " seconds and took " + str(attempts) + " attempts")
