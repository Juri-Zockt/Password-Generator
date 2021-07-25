import time
import random

numbers = ['0', '1', '2', '3'
           '4', '5', '6', '7'
           '8', '9']
randomnumber = (random.choice(numbers))
randomnumber1 = (random.choice(numbers))
randomnumber2 = (random.choice(numbers))
randomnumber3 = (random.choice(numbers))
randomnumber4 = (random.choice(numbers))
randomnumber5 = (random.choice(numbers))
randomnumber6 = (random.choice(numbers))
randomnumber7 = (random.choice(numbers))
randomnumber8 = (random.choice(numbers))
randomnumber9 = (random.choice(numbers))
letters = ['a', 'b', 'c', 'd',
           'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p',
           'q', 'r', 's', 't',
           'u', 'v', 'w', 'x',
           'y', 'z']
randomletters = (random.choice(letters))
randomletters1 = (random.choice(letters))
randomletters2 = (random.choice(letters))
randomletters3 = (random.choice(letters))
randomletters4 = (random.choice(letters))
randomletters5 = (random.choice(letters))
randomletters6 = (random.choice(letters))
randomletters7 = (random.choice(letters))
randomletters8 = (random.choice(letters))
randomletters9 = (random.choice(letters))
bigletter = ['A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X',
             'Y', 'Z']
randombigletter = (random.choice(bigletter))
randombigletter1 = (random.choice(bigletter))
randombigletter2 = (random.choice(bigletter))
randombigletter3 = (random.choice(bigletter))
randombigletter4 = (random.choice(bigletter))
randombigletter5 = (random.choice(bigletter))
randombigletter6 = (random.choice(bigletter))
randombigletter7 = (random.choice(bigletter))
randombigletter8 = (random.choice(bigletter))
randombigletter9 = (random.choice(bigletter))
sonder = ['!', '$', '%', '&',
          '/', '(', ')', '=',
          '?', '<', '>', '.',
          ',', '-', '+', '#', 
          '*']
randomsonder = (random.choice(sonder))
randomsonder1 = (random.choice(sonder))
randomsonder2 = (random.choice(sonder))
randomsonder3 = (random.choice(sonder))
randomsonder4 = (random.choice(sonder))
randomsonder5 = (random.choice(sonder))
randomsonder6 = (random.choice(sonder))
randomsonder7 = (random.choice(sonder))
randomsonder8 = (random.choice(sonder))
randomsonder9 = (random.choice(sonder))

print("Passwort Generator wird gestartet")
time.sleep(2)
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print(".")
time.sleep(2)
nummern = input("Sollen Nummern rein? ")
if 'Ja' in nummern:
    time.sleep(1)
    buchstaben = input("Sollen Kleinbuchstaben rein? ")
    if 'Ja' in buchstaben:
        time.sleep(1)
        groß = input("Sollen Großbuchstaben rein? ")
        if 'Ja' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomletters + randombigletter + randomsonder + randomnumber1 + randomletters1 + randombigletter1 + randomsonder1 + randomletters2 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomletters + randombigletter + randomnumber2 + randomnumber1 + randomletters1 + randombigletter1 + randomletters3 + randomletters2 + randombigletter2)
        if 'Nein' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomletters + randomnumber3 + randomsonder + randomnumber1 + randomletters1 + randomsonder3 + randomsonder1 + randomletters2 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomletters + randomletters4 + randomnumber2 + randomnumber1 + randomletters1 + randomnumber3 + randomletters3 + randomletters2 + randomnumber4)
    if 'Nein' in buchstaben:
        time.sleep(1)
        groß = input("Sollen Großbuchstaben rein? ")
        if 'Ja' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomnumber2 + randombigletter + randomsonder + randomnumber1 + randomsonder3 + randombigletter1 + randomsonder1 + randomnumber4 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomnumber3 + randombigletter + randomnumber2 + randomnumber1 + randombigletter3 + randombigletter1 + randombigletter4 + randomnumber4 + randombigletter2)
        if 'Nein' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomsonder4 + randomnumber3 + randomsonder + randomnumber1 + randomsonder5 + randomnumber9 + randomsonder1 + randomnumber6 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomnumber + randomnumber5 + randomnumber6 + randomnumber2 + randomnumber1 + randomnumber7 + randomnumber3 + randomnumber8 + randomnumber9 + randomnumber4)
if 'Nein' in nummern:
    time.sleep(1)
    buchstaben = input("Sollen Kleinbuchstaben rein? ")
    if 'Ja' in buchstaben:
        time.sleep(1)
        groß = input("Sollen Großbuchstaben rein? ")
        if 'Ja' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomletters3 + randomletters + randombigletter + randomsonder + randomletters4 + randomletters1 + randombigletter1 + randomsonder1 + randomletters2 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randombigletter3 + randomletters + randombigletter + randomletters4 + randombigletter4 + randomletters1 + randombigletter1 + randomletters3 + randomletters2 + randombigletter2)
        if 'Nein' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomsonder4 + randomletters + randomletters4 + randomsonder + randomletters3 + randomletters1 + randomsonder3 + randomsonder1 + randomletters2 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomletters5 + randomletters + randomletters4 + randomletters6 + randomletters7 + randomletters1 + randomletters8 + randomletters3 + randomletters2 + randomletters9)
    if 'Nein' in buchstaben:
        time.sleep(1)
        groß = input("Sollen Großbuchstaben rein? ")
        if 'Ja' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomsonder4 + randombigletter4 + randombigletter + randomsonder + randombigletter2 + randomsonder3 + randombigletter1 + randomsonder1 + randomletters2 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randombigletter5 + randombigletter6 + randombigletter + randombigletter8 + randombigletter9 + randombigletter3 + randombigletter1 + randombigletter4 + randombigletter7 + randombigletter2)
        if 'Nein' in groß:
            time.sleep(1)
            sondern = input("Sollen Sonderzeichen rein? ")
            if 'Ja' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(1)
                print(randomsonder4 + randomsonder5 + randomsonder6 + randomsonder + randomsonder7 + randomsonder8 + randomsonder3 + randomsonder1 + randomsonder9 + randomsonder2)
            if 'Nein' in sondern:
                time.sleep(1)
                print("Dein Passwort: ")
                time.sleep(2)
                print(".")
                time.sleep(2)
                print(".")
                time.sleep(2)
                print(".")
                time.sleep(2)
                print("Was erwartest du jetzt von mir?")
                time.sleep(2)
                print("Wenn du nichts willst warum nutzt du mich überhaupt?")
                time.sleep(2)
                print("BYE!")