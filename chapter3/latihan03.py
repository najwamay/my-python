# import library
import time
import datetime

# input username
name = input("Hello... my name is Mr. Python, what is your name? ")

# output username
print("Oh.. your name is ", name, ", such a nice name.")

# pause 3 seconds 
time.sleep(3)

# input year or birth
while True:
    try:
        birthYear = int(input("Well.. " + name + ", when were you born? "))
        break
    except ValueError:
        print("Enter your year of birth using valid numbers!")

# pause 3 seconds
time.sleep(3)

# calculate age 
timeNow = datetime.datetime.now()
age = timeNow.year - birthYear

# tampilkan usia
print("Hmmm...", name,"so you are", age," years old, aren’t you?")

# pause 3 seconds
time.sleep(3)

# show the message based on age
if (age > 40):
    print("You are too old ?")
    print("Take care of your health, OK!!")
elif (age > 17):
    print("You are still young")
    print("Don't waste your life with unimportant activities!!")
else:
    print("You are still a child?")
    print("Be a good child!!")

# pause 3 seconds
time.sleep(3)

# say goodbye
print("OK.. see you later", name, ".. nice to meet you")