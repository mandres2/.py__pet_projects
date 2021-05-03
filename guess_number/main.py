import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, try again. The value you guessed was low')
        elif guess > random_number:
                print('Sorry, try again. The value you guessed was too high')
    print(f'Congratulations! You have guessed the number {random_number} correctly!')
# The function where x is equal to the limit
# Output: Guess a number between 1 and x
guess(10)

