'''
Build a python application to see restaurants near me. Given a location by the
user, the application shall show restaurants rating wise from highest to
lowest. Couple of reviews about the restaurant, the best mode of travel and
timings shall also be displayed. Contact details of the restaurants like phone
number, email ID should also be mentioned.

'''
def time():
    print("This restaurant is open 24/7, you can go at any time!")
def choice():
    print("Restaurant A: 5 stars \n Restaurant B: 4 stars \n Restaurant C: 3 stars")
    choice = input("Which of these places would you like to eat at?")
    if choice=="A":
        print("Reviews:")
        print("John S")
        print("9/10 Stars")
        print("This is a very nice place, the food is really nice!")
    elif choice=="B":
        print("Reviews:")
        print("Tom K")
        print("7/10 Stars")
        print("This is a decent place, the food is nice but a bit expensive!")
    elif choice=="C":
        print("Reviews:")
        print("Max C")
        print("5/10 Stars")
        print("The food is terrible and cold, DO NOT RECCOMEND!")
    else:
        print("Please just enter the letter of the hospital!")
def transport():
    distance = int(input("How many minutes away do you live"))
    if distance>10:
        print("We reccomend taking car")
    if distance<10:
        print("We reccomend walking there")
    if distance==10:
        print("You can walk or take car if you are in a rush")
location = input("Enter where you live")
age = input("How old are you")
name = input("Enter your name")
amount = input("How many people are coming?")
choice()
time()
transport()
print("The contact details are as follows")
print("Email: restaurant@gmail.com")
print("Phone no.: 048309734856748")
