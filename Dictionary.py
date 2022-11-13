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


UserInfo = {}

print("WELCOME TO CONTACT TRACING")

#menu option
print("Menu:")
print("Option 1 — Check and Add your contact information")
print("Option 2 — Search for your contact information")
print("Option 3 — Exit the contact tracing")

choice = input("What do you want to do? ")

UserInfo["name"] = input("Enter your Full Name: ")
UserInfo["age"] = input("Enter your Age: ")
UserInfo["address"] = input("Enter your Address: ")
UserInfo["number"] = input("Enter your Phone number: ")
UserInfo["school"] = input("Enter your School: ")
UserInfo["email"] = input("Enter your E-mail: ")
UserInfo["bday"] = input("Enter your Birthday: ")

