# String concatenation
# Suppose we want to create a string that says "Hello my name is ____"

# name = "Micah Andres" # Some string variables

# A few ways to do this:

# print("Hello my name is " + name)
# print("Hello my name is {}".format(name))

# This is probably the most clean way at the moment in Python3 to show string contatenation
# print(f"Hello my name is {name}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)