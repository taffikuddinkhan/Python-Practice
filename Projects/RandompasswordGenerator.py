import random
import string
from random import randint

length = int(input("Enter the length of your password "))
while True:

    print("Generating password......")


    char_value = string.ascii_uppercase+string.digits+string.punctuation

    # password = ""                 #This 3 lines of code can be done in a single line
    # for i in range(length):
    #     password+=random.choice(char_value)

    password ="".join([random.choice(char_value) for i in range(length)])  # join is use to concadinate strings , before jion u pass any sybol that will be present  at the exact union of string point


    print("Do you want to use this password ",password)
    choice = input("Y/N")
    if choice == "Y":
        print("Thank u for your interest ,  Here is your password ",password)
        break
    if choice == "N":
        print("Generating again ur password ")
    else:
        print("Choose a valid option")