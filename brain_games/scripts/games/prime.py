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
        return False
    return True


def generate_round():
    random_number = random.randint(1, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer   





