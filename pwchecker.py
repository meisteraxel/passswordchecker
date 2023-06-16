#Password Checker

password = input("Type your password!")
score = 0

#Check the password for specific characters
lowercase = False
for character in password:
    if character in "abcdefghijklmnopqrstuvwxyz":
        lowercase = True

if lowercase  == True:
    print("Your password contains lowercase characters.")