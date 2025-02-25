import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_number(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def generate_round():
    random_number = random.randint(1, 100)
    correct_answer = even_number(random_number)
    return random_number, correct_answer
    
