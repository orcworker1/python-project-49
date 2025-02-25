import random

DESCRIPTION = 'What is the result of the expression?'


def calculated(num_1, nume_2, operand):
    if operand == '+':
        result = num_1 + nume_2
    elif operand == '-':
        result = num_1 - nume_2
    elif operand == '*':
        result = num_1 * nume_2
    return str(result)


def generate_round():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operand = random.choice(['+', '-', '*'])
    question = f'{number_one} {operand} {number_two}'
    result = calculated(number_one, number_two, operand)
    return question, result
