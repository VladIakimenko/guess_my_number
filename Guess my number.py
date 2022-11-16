from math import log2, ceil
from random import randrange, uniform

def error(s, e, lt, dir):
    print("Wough... wough! This can't be true! You must have mistaken!")
    if e == lt and dir == '+':
        print(f'You can not choose a number over "{lt}"!')
    elif s < 1:
        print(f'''You can't choose "0" as your number.'''
              f'We played from "1" to "{lt}".')
    else:
        print(f'There is no valid number between "{s}" and "{e}".')
    print()
    input('''Let's start over again, press "enter" to proceed...''')
    main()

def comp_guesses_number(lv, lmt, record=0):
    comp_name = {1: "Dumbass", 2: "Hither-thither", 3: "Dr. Nerd"}
    guess = 0
    attempt = 0
    start = 0
    end = (lmt + 1) if lv == 1 else lmt
    guess_list = [0]

    input(f'{comp_name[lv]}: '
          f'Ready with your number? Press "enter" and I start guessing...')

    while True:
        if record:
            print(f"The record is {record} {'try' if record == 1 else 'tries'}")
        print(f'Attempt: {attempt + 1}')
        attempt += 1

        if lv == 3:
            guess = ceil(start + (end - start) / 2)
        elif lv == 2:
            while guess in guess_list or not start <= guess <= end:
                guess = int(ceil(start + (end - start) / 2) * uniform(0.1, 1.1))
            guess_list.append(guess)
        elif lv == 1:
            guess = randrange(start + 1, end)

        print(f'{comp_name[lv]}: You think of the number {guess}?'
              f' (type "y" or "n" for answer)')

        while True:
            answer = input().replace("'", '').replace('"', '')
            answer = answer.replace(' ', '').lower()
            if answer in ('y', 'n'):
                break
            else:
                print('"y" or "n", just one letter...')

        if answer == 'y':
            print(f'{comp_name[lv]}: Good! So your number was {guess}')
            break
        else:
            print(f'{comp_name[lv]}: is your number higher'
                  f' or lower than {guess}?'
                  f' Type "+" if your number is higher or'
                  f' "-" if your number is lower')
            while True:
                answer = input().replace("'", '').replace('"', '')
                answer = answer.replace(' ', '')
                if answer in ('+', '-'):
                    break
                else:
                    print('"+" or "-", no other choice...')
            if answer == '+':
                start = guess
            elif answer == '-':
                end = guess

        if (start == end or (end - start == 1 and end != lmt) or
                            (end - start == 1 and answer == '-')):
            error(start, end, lmt, answer)

    if record:
        print()
        calculate_result(attempt, record)
    else:
        print()
        user_guesses_number(lv, lmt, attempt)

def user_guesses_number(lv, lmt, record=0):
    number = randrange(1, lmt + 1)
    guess = 0
    attempt = 0
    comp_name = {1: "Dumbass", 2: "Hither-thither", 3: "Dr. Nerd"}

    print(f'{comp_name[lv]}: Try to guess what number is on my mind?\n')

    while guess != number:
        if record:
            print(f"The record is {record} "
                  f"{'try' if record == 1 else 'tries'}")
        print(f'Attempt: {attempt + 1}')

        while True:
            print('enter your guess:\t')
            guess = input().replace("'", '').replace('"', '').replace(' ', '')
            if guess.isdigit() and 1 <= int(guess) <= lmt:
                guess = int(guess)
                attempt += 1
                break
            else:
                print(f'Enter number from 1 to {lmt}\t')

        if guess == number:
            print(f"{comp_name[lv]}: That's correct! My number was {number}")

            if record:
                print()
                calculate_result(record, attempt)
            else:
                print()
                comp_guesses_number(lv, lmt, attempt)
        elif guess < number:
            print(f'{comp_name[lv]}: No! My number is higher!')
        elif guess > number:
            print(f'{comp_name[lv]}: Miss! My number is lower!')

def calculate_result(att, rec):
    print(f'You guessed my number in {rec} {"try" if rec == 1 else "tries"}')
    print(f'I guessed your number in {att} {"try" if att == 1 else "tries"}')
    print()
    if att > rec:
        print('You win!')
    elif att < rec:
        print('You lose!')
    else:
        print("It's a draw!")

    print()
    print('Would you like to play again? Type "y" or "n"\t')
    while True:
        restart = input().replace("'", '').replace('"', '')
        restart = restart.replace(' ', '').lower()
        if restart == 'y':
            main()
        elif restart == 'n':
            exit()
        else:
            print('"y" or "n", just one letter...')

def main():
    print("""
    Welcome to "Guess my number" game!
    In this game I think of a number and you try to guess it.
    Then I will be guessing your number. We count attempts. The lesser - wins!
    Or we can switch it vice versa.

    Who would you like to be guessing first?

    Type "1" for: - You think, I guess!
    Type "2" for: - Try to guess what's on my mind!
    """)
    while True:
        game_choice = input().replace("'", '').replace('"', '')
        if game_choice in ('1', '2'):
            break
        else:
            print()
            print('''Just "1" or "2", come on! That's not too difficult!\t''')

    while True:
        print()
        print("Ok, let's set the high limit. "
              "We'll be guessing from 1 to what?\t")
        limit = input().replace("'", '').replace('"', '').replace(' ', '')
        if limit.isdigit() and int(limit) > 1:
            limit = int(limit)
            break
        else:
            print("""
            What is wrong with you? Just put in one number.
            It has to be > 1.
            It should be an integer. 
            Use numbers, not words.
            No garbage symbols.
            
            Come on, you can make it!
            """)

    print(f"""
            Please choose difficulty level:
            1 - for "Dumbass" (uses no logic, just random guesses)
            2 - for "Hither and thither" (uses logic, but acts human)
            3 - for "Dr. Nerd" (uses {ceil(log2(limit))} tries maximum)
            """)
    while True:
        level = input().replace("'", '').replace('"', '')
        if level in ('1', '2', '3'):
            level = int(level)
            break
        else:
            print("""
                    Once, again!
                    "1" for "Dumbass"
                    "2" for "Hither-thither"
                    "3" for "Dr. Nerd"
                    """)

    if game_choice == '1':
        user_guesses_number(level, limit)

    elif game_choice == '2':
        comp_guesses_number(level, limit)

main()

