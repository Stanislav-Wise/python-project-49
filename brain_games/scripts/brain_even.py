#!/usr/bin/env python3
from brain_games import cli
from random import randint


def quiz(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        # while not answer in ['yes', 'no']:
        #     answer = input('Your answer: ')
        if not number % 2 and answer == "yes" or number % 2 and answer == "no":
            print('Correct!')
            correct_answer += 1
        else:
            print(f"'{answer}'  is wrong answer ;(. Correct answer was '{'no' if answer == 'yes' else 'yes'}'.")
            print(f"Let's try again, {user_name}!")
            break

    print(f"Congratulations, {user_name}!")


def main():
    cli.print_hello()
    name = cli.enter_name()
    print(cli.welcome_user(name))
    quiz(name)


if __name__ == '__main__':
    main()
