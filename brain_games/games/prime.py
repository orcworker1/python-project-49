import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numbers):
    count = 0
    if numbers == 1:
        return False
    for i in range(1, numbers + 1):
        if numbers % i == 0:
            count += 1
    if count > 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return correct_answer


def generate_round():
    random_number = random.randint(1, 100)
    correct_answer = is_prime(random_number)
    return random_number, correct_answer   





