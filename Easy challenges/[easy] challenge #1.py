import os

filename = "data.txt"

if os.path.isfile(filename):
    data = open("data.txt").readlines()
    name = data[0].rstrip()
    age = data[1].rstrip()
    username = data[2].rstrip()
    print("Your name is %s, you are %s years old, and your username is %s" % (name, age, username))

else:
    name = input("What is your name? ")
    age = input("What is your age? ")
    username = input("What is your username? ")
    print("Your name is %s, you are %s years old, and your username is %s" % (name, age, username))
    with open("data.txt", "w") as data:
        data.write("%s\n%s\n%s" % (name, age, username))
