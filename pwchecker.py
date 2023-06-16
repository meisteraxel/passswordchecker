#Password Checker
import string

password = input("Type your password! ")
score = 0

#Check the password for specific characters
lowercase = False
uppercase = False
punctuation = False
number = False
lenght = False

#Check for Characters
for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True
    elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True
    elif character in "0123456789":
        number = True
    elif character in string.punctuation:
        punctuation = True

#Atleast 8 Characters long
if len(password) > 8:
    lenght = True
else:
    lenght = False


if lowercase  == True:
    print("Your password contains lowercase characters.")
if uppercase  == True:
    print("Your password contains uppercase characters.")
if punctuation == True:
    print("Your password contains Punctuations.")
if number == True:
    print("Your password contains a number.")
if lenght == True:
    print("Your password is at least 8 characters long.")

#Score 
if lowercase and uppercase == True:
    score = score + 10
if lowercase and uppercase and number == True:
    score = score + 10
if punctuation == True:
    score = score + 5
if lenght == True:
    score = score + 5

print("You achieved " + str(score) + "/30 points!")
