#import random module
import random

# Getting the users guess
guess = int(input("Enter your guess between 1 and 100: ")) #make sure user enters integer

#generate a random number between 1 and 100
randnum = random.randint(1,101)

if guess < randnum:
    print('higher')
elif guess > randnum:
    print('lower')
else:
    print('Congratulations, you guessed the number')
