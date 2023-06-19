#Password Checker
import string
import tkinter
import customtkinter


#Set TK Window
customtkinter.set_appearance_mode("System")
app = customtkinter.CTk()
app.geometry("500x300")
app.title("Password Check")
app.grid_columnconfigure(0, weight=1)


#Check the password for specific characters

def checkPassword():
    password = pwbox.get()
    global score 
    score = 0
    
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

    #Score 
    if lowercase and uppercase == True:
        score = score + 10
    if lowercase and uppercase and number == True:
        score = score + 10
    if punctuation == True:
        score = score + 10
    if lenght == True:
        score = score + 10

    #ProgressBar
    if score <= 10:
        progressbar.set(value=0.25)
        progressbar.configure(progress_color="red")
    elif score <= 20:
        progressbar.set(value=0.5)
        progressbar.configure(progress_color="yellow")
    elif score <= 30:
        progressbar.set(value=0.75)
        progressbar.configure(progress_color="lightgreen")
    elif score <= 40:
        progressbar.set(value=1)
        progressbar.configure(progress_color="green")
    


#Define Buttons/Labels
label = customtkinter.CTkLabel(app, text="Passwordcheck - created by Axel", fg_color="transparent")
label.grid(row=0, column=0, padx=20, pady=20)

pwbox = customtkinter.CTkEntry(master=app, placeholder_text="Password")
pwbox.grid(row=1, column=0, padx=5, pady=5)

analyze_button = customtkinter.CTkButton(app, text="Analyze PW", command=checkPassword)
analyze_button.grid(row=2, column=0, padx=20, pady=20)

progressbar = customtkinter.CTkProgressBar(app, width=250, height=30)
progressbar.grid(row=3, column=0, padx=20, pady=50)
progressbar.set(value=0)

app.mainloop()