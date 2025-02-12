import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = random.randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
        
    return random_number, correct_answer
    
