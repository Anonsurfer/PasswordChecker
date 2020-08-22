# Written in python
# I have explain each and every line of code in the program ! so, enjoy ;) 
import os # using os
import time # using time 
def welcome_page(): # defining a function
    os.system('cls') # clearning the screen 
    print("Hello World, Welcome to my program!") # simple print code use
    print("1.Set a new user name and password") # simple print code use
    print("2.Login") # simple print code use
    print("3.Read-Me") # simple print code use
    print("4.Exit") # simple print code use
    user_value = input("Enter your choice: ")  # taking input from user
    if user_value == "1": # using if condition
        Creating_file() # calling creating_file() function
    elif user_value == "2": # using if condition
        Login() # calling login() function
    elif user_value == "3": # using if condition
        Readme() # calling Readme() function
    elif user_value == "4": # using if condition
        exit() # Directly exiting the program.
    else: # using else condition
        print("Sorry, We didn't understood you !") # simple print code use
        print("Restarting the program...........!") # simple print code use
        time.sleep(2) # using sleep 
        welcome_page() # calling welcome_page
def Creating_file(): # new function defined 
    os.system('cls')   # clearing screen
    file = open("C:\\Users\Admin\Documents\pass.txt",'w') # Creating file
    user_name = input("Enter new username: ") # Asking the user with username
    file.write(user_name)  # Adding the username in the file
    file.write('\n') # Going to next line
    password = input("Enter new password: ") # Asking the user with the password
    print("Enter the new password once again to set it as the new password ") # Instructing the user with some of the rules in the program
    print("Or type common 'sys.restart' to restart the process from the beginning !") # Instructing the user with some of the rules in the program
    user_choice = input() # Asking with the users choice !
    if user_choice == password: # Applying if condition
        file.write(password)# Adding the password in the file
        os.system('cls') # clearning screen
        print("Congratulations, your new user name and password were added to the system!")# Congratulating the user for getting new user name and password !
        file.close() # closing the file
        print("Sending you back to main-page!") # simple print code use
        time.sleep(3) # using sleep 
        welcome_page() # calling function
    elif user_choice == "sys.restart": # Again applying condition.
        print("Restarting the service again !") # Printing the message
        time.sleep(2) # Making it look real !
        os.system('cls') # Clearing the screen
        Creating_file() # Calling the function !
    else:# using else condition
        os.system('cls') # clearing the screen
        print("Sorry, we didn't understood you !") # simple print code use
        print("1. To Restart the program ") # simple print code use
        print("2. To Exit the program ") # simple print code use
        user_choice2 = input("Enter your choice: ") # taking input from user 
        if user_choice2 == "1": # using if condition
            os.system('cls') # clearning the screen
            print("Restarting the program!") # simple print code use
            time.sleep(2) # sleep
            os.system('cls') # clearing the screen
            Creating_file() # calling creating_file() function 
        elif user_choice2 == "2": # using if condition
            print("Exiting from the program!") # simple print code use
            exit() # exiting...........
        else: # using else condition
            os.system('cls') # clearning the screen
            print("Sorry, we didn't understood you !")# simple print code use
            print("1. To Restart the program ")# simple print code use
            print("2. To Exit the program ")# simple print code use
            user_choice3 = input("Enter your choice: ") # taking input from the user
            if user_choice3 == "1": # using if condition
                os.system('cls') # clearing the screen
                print("Restarting the program!")# simple print code use
                time.sleep(2) # sleep (to pause the screen for certain secs - like 2 seconds in the code!)
                os.system('cls')  # clearing the screen 
                Creating_file() # calling the function
            elif user_choice3 == "2": # using if condition
                os.system('cls') # clearing the screen
                print("Exiting....")# simple print code use
                exit() # Closing the file !
            else: # using else condition
                os.system('cls') # clearing the screen
                print("Sorry, we didn't understood you again! ")# simple print code use
                os.system('cls') # clearing the screen
                print("Restarting the program for you !")# simple print code use
                time.sleep(2) # using sleep
                os.system('cls') # clearing the screen
                Creating_file() # calling the function
def Login(): # new function defined !
    import os.path # using os.path 
    from os import path # using os from import path
    os.system('cls') # clearing the screen
    print("Welcome verifying you...........!") # simple print code use
    print("Let's first check whether you have set username and password or not!")# simple print code use
    print("Checking.............")# simple print code use
    time.sleep(3) # using sleep
    os.system('cls')# clearing the screen
    is_there = path.exists("C:\\Users\Admin\Documents\pass.txt") # checking if the path exists ? 
    if is_there == 0: # if condition
        print("You didn't went to first page")# simple print code use
        print("First goto first page!")# simple print code use
        print("Setup your new username and password there then come back to this [login page] !")# simple print code use
        print('Sending you to first page')# simple print code use
        time.sleep(6) # using sleep
        input("Hit enter to goto first page: ") # waiting for user to hit enter key
        Creating_file() # calling function 
    elif is_there == 1: # using if condition
        reading_the_file = open("C:\\Users\Admin\Documents\pass.txt",'r') # locating file
        reading_data = reading_the_file.read() # reading data from the file
        if reading_data == '': # using if condition
            print("Error the file is created but there's no data presented inside" )# simple print code use
            print("Sending you back to first page!")# simple print code use
            time.sleep(2)  # using sleep
            input("Hit enter to goto first page, where the program will ask you to input some data !") # waiting for user to hit enter key
            Creating_file() # calling the function 
        else: # else code !
            Real_Login() # calling the function
def Real_Login(): # defining a new function 
    os.system('cls')# clearing the screen
    print("Verficaiton completed successfully!")# simple print code use
    print("Welcome to the real login page!") # simple print code use   
    asking_user_name() # calling a funtion 

def asking_user_name(): # defining a new function 
    counter = 3 # creating a variable 
    file_open = open("C:\\Users\Admin\Documents\pass.txt",'r') # locating the file location to the program
    user_name = file_open.read().split('\n')[0] # Real_User_Name_which was stored in the file!
    user_name_input = input("Enter your user name: ") # Asking with user!
    while user_name != user_name_input: # using while loop
        if counter == 0: # using if condition 
            break # breaking out of the loop and condition !
        os.system('cls') # clearing the screen
        print("Error, entered username was incorrect! ")# simple print code use
        print("You have {} chance left !".format(counter)) # simple print code use 
        user_name_input = input("Enter your user name: ") # taking input from the user
        counter = counter - 1  # subtracting 1 value each time the loop runs
    if user_name == user_name_input: # using if condition
        os.system('cls')# clearing the screen
        print("Welldone! the entered username was correct!")# simple print code use
        password_() # calling the function
        time.sleep(2) # using sleep
    else: # else code
        os.system('cls')# clearing the screen
        print("Sorry, you were unable to enter the correct password !")# simple print code use
        print("Sending you back to the main page...........!")# simple print code use
        time.sleep(2) # using sleep 
        welcome_page() # calling function
def password_(): # defining a new funtion
    import os # using os
    counter = 3 # create a variable named counter 
    print("\t\t\tPassword Verification") # using print function 
    file_open2 = open("C:\\Users\Admin\Documents\pass.txt",'r') # reading the file 
    password_read = file_open2.read().split('\n')[1] # Real Password which was stored in the file !
    password_ = input("Enter your password: ") # User_input password
    while password_read != password_: # using while loop
        if counter == 0: # using if condition 
            break # breaking out of loop and if condition 
        os.system('cls') # clearing the screen
        print("Error, password entered was incorrect! ")# simple print code use
        print("You have {} chance left !".format(counter))# simple print code use
        password_ = input("Enter your password: ") # taking input from the user
        counter = counter - 1 # subtracting counter value by 1 each time the loop runs
    if password_ == password_read: # using if condition 
        os.system('cls')# clearing the screen
        print("Welldone!")# simple print code use
        print("Username and password were correct!")# simple print code use
        print("Access Gained!")# simple print code use
        print("Thank you for using the program !")# simple print code use
    else: # using else condition
        os.system('cls')# clearing the screen
        print("Sorry, you were unable to enter the correct password !")# simple print code use
        print("Sending you back to the main page...........!")# simple print code use
        time.sleep(2) # using sleep
        #main_page()
def Readme(): # creating a new function named readme
    os.system('cls')# clearing the screen
    print("Hello World!")# simple print code use
    print("This is a simple program written in python !")# simple print code use
    print("Just to show programmer how you can create a file and store it a specific place you want and how you can add data into it")# simple print code use
    print("Then how you can check that data line by line using some file handling codes of python! ")# simple print code use
    print("Thank you for using this software")# simple print code use
    print("Good luck, Focus on your studies ;)")# simple print code use
welcome_page() # calling the welcome_page