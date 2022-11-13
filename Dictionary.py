# Write a python program for contact tracing:

# - Display a menu of options
#	Menu:
#		 1 -> Add an item
#	     2 -> Search
#		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
#		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#				   Use dictionary to store the info
#				   Use the full name as key
#				   The value is another dictionary of personal information
#		- Option 2: Search, ask full name then display the record
#		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:
# Menu:
# 1 -> Add an item
# 2 -> Search
# 3 -> Exit (y/n)
#
# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890What do you want to do? (1-3): 3
# Exit? n

#\033[1;35;1m  \033[0m

#\033[1;3m  \033[0m

#\033[1;255;1m  \033[0m

import time

user = []
UserInfo = {}


choice = ""
time.sleep(2)
print("\033[1;255;1m--------------- WELCOME TO CONTACT TRACING ---------------\033[0m\n")
while(choice != "3"):
    time.sleep(1)
    print("     \n\033[1;255;3mMenu:\033[0m  ")
    print("     \033[1;35;1mOption 1\033[0m — Check and Add your Contact Information")
    print("     \033[1;35;1mOption 2\033[0m — Search for your Contact Information")
    print("     \033[1;35;1mOption 3\033[0m — Exit the Contact Tracing")
    print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")
    time.sleep(2)
    choice = input("\n\033[1;3mWhat do you want to do? (1-3):\033[0m  ")
    
    if choice == '1':
        print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")
        time.sleep(2)
        print("\n\033[1;3mCheck first if the user exist!\033[0m")
        Out = list(UserInfo.values())
        Name = input("\n\033[1;35;1m    Full name:\033[0m ")

        if Name in Out:
            print("\n\033[1;255;1mThis name already exists!\033[0m")
            print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")

        else:
            print("\n\033[1;255;1mWait a few seconds to Check your Record.\033[0m")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(2)
            print("\n\033[1;31;1mThis name is not yet registered!\033[0m\n")
            print("\n\033[1;255;1m----------------------------------------------------------\033[0m\n")
            time.sleep(2)
            print("\n\033[1;255;1mADD A NEW RECORD\033[0m")
            time.sleep(1)
            UserInfo["\n\033[1;35;1mName\033[0m"] = input("\n\033[1;35;1m     Enter your Full name:\033[0m  ")
            UserInfo["\033[1;35;1mAge\033[0m"] = input("\033[1;35;1m     Enter your Age:\033[0m  ")
            UserInfo["\033[1;35;1mAddress\033[0m"] = input("\033[1;35;1m     Enter your Address:\033[0m  ")
            UserInfo["\033[1;35;1mNumber\033[0m"] = input("\033[1;35;1m     Enter your Phone number:\033[0m  ")
            UserInfo["\033[1;35;1mSchool\033[0m"] = input("\033[1;35;1m     Enter your School:\033[0m  ")
            UserInfo["\033[1;35;1mEmail\033[0m"] = input("\033[1;35;1m     Enter your E-mail:\033[0m  ")
            UserInfo["\033[1;35;1mBirthday\033[0m"] = input("\033[1;35;1m     Enter your Birthday:\033[0m  ")
            user.append(UserInfo)
            time.sleep(2)
            print("\n\033[1;255;1mWait a few seconds to Save your Record.\033[0m")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(2)
            print("\n\033[1;255;1mRecord Saved!\033[0m")
            print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")

    if choice == '2':
        print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")
        time.sleep(2)
        print("\n\033[1;255;1mSearch for your Contact Information\033[0m")
        check = list(UserInfo.values())
        time.sleep(1)
        find = input("\n\033[1;35;1m    Full name:\033[0m   ")

        if find in check:
            Out = None
            for key in choice:
                for key in UserInfo:
                    
                    print(key, ":", UserInfo[key])

        else:
            print("\n\033[1;31;1mThis name is not yet registered!\033[0m")
            print("\n\n\033[1;255;1m----------------------------------------------------------\033[0m\n")

    if choice == '3':
        print("\n\n\033[1;255;1m---------- THANK YOU FOR USING CONTACT TRACING! ----------\033[0m\n")
        exit()


