#Ask user for name

name=input("What is your name?: ").strip()

#Ask user for age

age=input("How old are you?: ").strip()

#Ask user for city

city=input("What city do u live in?: ").strip()

#Ask user what they enjoy

love=input("What do u love doing?: ").strip()

#Create output text

string="Your name is {} and you are {} years old. You live in {} and you love {}"

output=string.format(name,age,city,love)

#Print output to screen

print(output)
