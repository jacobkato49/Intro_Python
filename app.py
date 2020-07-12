#import random module
import random



#generate a random number between 1 and 100
randnum = random.randint(1,101)

count = 0
guess = -99

while (guess != randnum):


    # Getting the users guess
    guess = int(input("Enter your guess between 1 and 100: ")) #make sure user enters integer
    if guess < randnum:
        print('higher')
    elif guess > randnum:
        print('lower')
    else:
        print('Congratulations, you guessed the number')
        break
    count = count + 1
# end the while loop

print('You took ' + str(count) + ' tries to guess the number.')
