import random
my_number = random.randint(0,20)
guess = -1
trials = 0
while(guess != my_number):
    print("Guess my number!")
    guess = int(input())
    trials += 1
    if(guess > my_number):
        print("My number is lower than Yours!")
    else:
        print("My number is higher than Yours!")
print("Correct! You have guessed my number!")
print("You have needed", trials, "trials.")



