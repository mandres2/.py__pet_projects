import random

# In this file, the computer will be the one to guess the selected number the user defines

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

computer_guess(1000)