# Obtaining Python system version
# import sys
# print("Python version")
# print(sys.version)
# print("Version info")
# print(sys.version.info)

###########################################################################################


# Print out current date and time 
# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

###########################################################################################


# Write a Python program which accepts the radius of a circle from the user and compute the area.
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


###########################################################################################

# Print first and last name in reverse order with a space between them
# In python there are two functions designed to accept data directly from a user.
    # Python 2.x -> raw_input()
    # Python 3.x -> input()

# raw_input() asks the user for a string of data and simply returns the string, the string data ended with a 
# newline. It can als take an argument, which is displayed as a prompt before the user enters the data

#input():
# In 3.x. raw_input() is renamed to input(). input() function reads a line from sys.stdin and returns it with the trailing newline stripped. To assign the user's name to a variable "y" use the command:

# y = input('Input your name')

# fname = input("Input your first name : ")
# lname = input("Input your last name : ")
# print("Hello " + lname + " " + fname)

###########################################################################################

# Check name application 
# name = "Micah"

# if/else statement
# if name == "Micah":
#     print("Hello", name)
# else:
#     print("Oh, well what is your name then?")

# Simple Function
# def checkName(name):
    # checkName = input("Is your name " + name + "? ")

    # if checkName.lower() == "yes":
    #     print("Hello,", name)
    # else:
    #     name = input("Sorry about that. What is your name again?")
    #     print("Welcome" ,name + ".")

# checkName("Keenan")

###########################################################################################

# Simple calculator program

# This function adds two numbers
# def add(x, y):
#     return x + y

# This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # Take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     # Check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")

###########################################################################################

# Write a Python program to create an Enum object and display a member name and value. 
# Sample data :
# Afghanistan = 93
# Albania = 355
# Algeria = 213
# Andorra = 376
# Angola = 244
# Antarctica = 672
# Expected Output :
# Member name: Albania
# Member value: 355

# from enum import Enum
# class Country(Enum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# print('\nMember name: {}'.format(Country.Albania.name))
# print('\nMember value: {}'.format(Country.Albania.value))
# Output:
# Member name: Albania
# Member value: 355

###########################################################################################

# Write a Python program to iterate over an enum class and display individual member and their value.

# from enum import Enum
# class Country(Enum):
#     Afghanistan = 93
#     Albania = 355
#     Algeria = 213
#     Andorra = 376
#     Angola = 244
#     Antarctica = 672
# for data in Country:
#     print('{:15} = {}'.format(data.name, data.value))

# Output:
# Afghanistan     = 93
# Albania         = 355
# Algeria         = 213
# Andorra         = 376
# Angola          = 244
# Antarctica      = 672

###########################################################################################

# Print even numbers in a list

# list1 = [10, 21, 4, 45, 66, 93]

# iterate through each number on the list
# for num in list1:
    # Set the condition so that any number that is divisible by 2, let the application print   that data as a string type

    # if num %2 == 0:
    #     print(num, end = " ")
    
    # Sample Output
    # 10, 4, 66 

###########################################################################################
