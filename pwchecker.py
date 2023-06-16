#Password Checker
import string

password = input("Type your password! ")
score = 0

#Check the password for specific characters

#Lowercase
lowercase = False
for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True

if lowercase  == True:
    print("Your password contains lowercase characters.")

#Lowercase
uppercase = False
for character in password:
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True

if uppercase  == True:
    print("Your password contains uppercase characters.")

#Punctuation Sign
punctuation = False
for character in password:
    if character in string.punctuation:
        punctuation = True

if punctuation == True:
    print("Your password contains Punctuations.")
