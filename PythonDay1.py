# Make name all capitalize when enter

name = input("What is your name? ")
print("%s, %s!" % ("Hello", name))

name_upper = input("What is your name? ".upper())
print("%s, %s!" % ("Hello".upper(), name.upper()))
print("Your name has ".upper() + str(len(name_upper))
+ " letters in it! awesome!".upper())


# Madlib
print("Please fill in the blanks below: ")
print("___(name)___'s favorite subject in school is ___(subject)___")
name = input("What is name? ")
subject = input("What is subject? ")   
print("%s's favorite subject in school is %s." % (name, subject))




# Day of the Week
day = int(input('Day (0-6)? ')) 

if day == 0: 
    print("%d Sunday" % (day))

elif day == 1: 
    print("%d Monday" % (day))

elif  day == 2: 
    print("%d Tuesday" % (day))

elif day == 3: 
    print("%d Wedesday" % (day))

elif  day == 4: 
    print("%d Thurday" % (day))

elif  day == 5: 
    print("%d Friday" % (day))

elif  day == 6: 
    print("%d Sunday" % (day))



# 5. Work or Sleep In?

day = int(input('Day (0-6)? ')) 

if (day <= 4):
    print("%d Go to work" % (day))
else: print("%d Sleep In" % (day))



# 6. Celsius to Fahrenheit
C = input("What is the Temperature in  in C ")
F = float(C) * 1.8 + 32
print("%d F" % (F))

# 7. Tip Calculator

total = float(input("Total bill amount? "))
service = input("Level of service? ")
tip = 0
if service == "good":
    tip = float(total) * 0.2
elif service == "fair":
    tip = float(total) * 0.15
elif service == "bad":
    tip = float(total) * 0.1
else:
    print("good, fair, or bad")
total_amount = total + tip
print("Tip amount: $%.2f\nTotal amount: $%.2f" % (tip, total_amount))


# Exercise 8: Tip Calculator 2

total = float(input("Total bill amount? "))
service = input("Level of service? ")
people = float(input("How many Ways"))
tip = 0
if service == "good":
    tip = float(total) * 0.2
elif service == "fair":
    tip = float(total) * 0.15
elif service == "bad":
    tip = float(total) * 0.1
else:
    print("good, fair, or bad")
total_amount = total + tip
Amount = float(total_amount/people)
print("Tip amount: $%.2f\nTotal amount: $%.2f" % (tip, total_amount))

print("Tip Amount: $%.2f\nTotal amount: $%.2f\nAmount per person: $%.2f" % (tip, total_amount, Amount))


# exercise 9

count = 1
while count < 11 :
    print(count)
    count = count + 1


#  exercise 10

coins = 0

no_stop = True

while no_stop:
    print("You have %d coins." % (coins))
    ask_coins = input("Do you want another? ")
    if ask_coins == "yes":
        coins = coins + 1
    elif ask_coins =="no":
        print("Bye")
        stop = False










# Bonus Question 1

name = input("What is your Name")
if (len(name) < 10):
        print("Hello %s"  % (name))
else:
        print("Your Name is Too Long")




# Bonus Question 2

name = input("Give Me a name")
name1 = input("Give Me a second name")
name2 = input("Give Me a third name")

if len(name1) and len(name2) > len(name):
    print("Hello, %s " %(name))

elif len(name) and len(name2) > len(name1) :
        print("Hello, %s " % (name1))

elif len(name) and len(name1) > len(name2):
    print ("Hello, %s " % (name2))




# Bonus Question 3

num = int(input("Pick a number 1 through 3"))

if (num == 1):
    print("Apples are delicious!")

elif (num == 2):
    print("Oranges are very good for you!")

elif (num == 3):
    print("Androids are better than iPhones.")

else: print("Sorry...Enter Something Valid")