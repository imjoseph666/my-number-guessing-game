import random
attempt = 0
count = 0

print('Hello! This is the number guessing game!')
print('I am thinking of a number between 1 and 100')
print('You have 5 chances to guess the correct number\n')

print('Please select the difficulty level:')

print('1. Easy (10 chances)')
print('2. Medium (5 chances)')
print('3. Hard (3 chances)\n')

diff = input('Enter your choice:')      

if diff == '1':
    print("Great! You have selected the Easy difficulty level.\nLet's start the game")
    attempt =+ 10
if diff == '2':
    print("Great! You have selected the Medium difficulty level.\nLet's start the game")
    attempt =+ 5
if diff == '3':
    print("Great! You have selected the Hard difficulty level.\nLet's start the game")
    attempt =+ 3
    
random_number = random.randint(1,100)

while attempt > 0:
    num = input('Enter your guess!:')
    count =+ 1
    try:
        user_guess = int(num)
    except:
        print('PLEASE ENTER A VALID INTEGER')

    if user_guess > random_number:
        print(f'Incorrect! The number is smaller than {user_guess}')
        attempt = attempt - 1
        count =+ 1

    elif user_guess < random_number:
        print(f'Incorrect! The number is bigger than {user_guess}')
        attempt = attempt - 1
        count =+ 1

    elif user_guess == random_number:
        print(f'Congratulations! You guessed the correct number in {count} attempts')
        break

if attempt == 0:
    print('Try again!')