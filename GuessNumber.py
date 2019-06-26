

names = ['George', 'Gary', 'Greg', 'Grant']

for x in names:
    for character in x:
        print(character)


# Guess a number 


n = 5
guess = int(input("Guess a secret number "))
while n != "guess":
    if guess < 5:
        print("Guess is low")
        guess = int(input("Guess a secret number "))
    elif guess > 5:
        print("Guess is high")
        guess = int(input("Guess a secret number "))
    else:
        print("You Win")
        break






# Guess a number part 2
import random 

my_random_number = random.randint(1, 10)
guess = int(input("Guess a secret number "))
while my_random_number != "guess":
    if guess < my_random_number:
        print("Guess is low")
        guess = int(input("Guess a secret number "))
    elif guess > my_random_number:
        print("Guess is high")
        guess = int(input("Guess a secret number "))
    else:
        print("You Win")
        break
   

# Guess a number Part 3

import random

secret_number = random.randint(1, 10)
trys = 0

print("I am thinking of a number between 1 and 10.")

while trys < 5:
    try:
        print("You have " + str(5 - trys) + " guesses left.")
        number = int(input("Guess a number? "))
        if number == secret_number:
            print("Yes! You win!")
            trys = 5
            cont = input("Do you want to play again (Y or N)? ").upper()
            if cont == "Y":
                trys = 0
            elif cont == "N":
                print("Bye! See you Next time")
                break
        elif number < secret_number:
            trys += 1
            print("%d is too low." % (number))
        elif number > secret_number:
            trys += 1
            print("%d is too high." % (number))
        while trys == 5:
            print("Sorry you ran out of guesses!")
            cont = input("Do you want to play again (Y or N)? ").upper()
            if cont == "Y":
                trys = 0
            elif cont == "N":
                print("Bye!")
                break
    except:
        pass
        