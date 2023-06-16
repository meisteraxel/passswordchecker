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

#Atleast 8 Characters long
lenght = False
if len(password) > 8:
    lenght = True
else:
    lenght = False

if lenght == True:
    print("Your password is at least 8 characters long.")

