import random
def guess_the_number():
    left_limit, right_limit = 1, 100
    Num = random.randint(left_limit, right_limit)
    print('Guess the number.')
    while True:
        test_num = int(input(f'Guess the number form {left_limit} to {right_limit}.\nOr enter 0 if You want to exit the game: '))
        if test_num == 0:
            break
        elif left_limit <= test_num < Num:
            print('The hidden number is bigger than the entered one.')
            left_limit = test_num + 1
        elif Num < test_num <= right_limit:
            print('The hidden number is smaller than the entered one.')
            right_limit = test_num - 1
        elif test_num > right_limit or test_num < left_limit:
            print('Please, enter a number within the given limits.')
        else:
            print('You guessed the number!')
            break
