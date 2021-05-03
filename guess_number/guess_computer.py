import random

# In this file, the computer will be the one to guess the selected number the user defines

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, try again. The value was too low')
        elif guess > random_number:
            print('Sorry, try again. The value was too high')

    print(f'Congratulations! You have guessed the number {random_number} correctly!')

    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low # could also be high because low = high
            # .lower() does not capitalizes the string
            feedback = input(f'Is {guess} too high (H), too low(L), or correct(C)?').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f'Awesome! The computer has guessed the number {guess} correctly!')

guess(10)