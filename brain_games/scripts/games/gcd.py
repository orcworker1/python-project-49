import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    list_ = []
    while b != 0:
        a, b = b, a % b
        list_.append(a)    
    return min(list_)


def generate_round():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    question = f'{number_one} {number_two}'
    correct_answer = gcd(number_one, number_two)
    return question, str(correct_answer)


