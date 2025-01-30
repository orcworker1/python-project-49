import random

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def random_value():
    return random.randint(1, 100)


def random_operand():
    return random.choice('+-*')