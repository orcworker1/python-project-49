import random

DESCRIPTION = 'What is the result of the expression?'

def generate_round():
    number_one = random.randint(1,100)
    number_two = random.randint(1,100)
    operand = random.choice(['+','-','*'])
    qustion = f'{number_one} {operand} {number_two}'
    if operand == '+':
        result = number_one + number_two
    elif operand == '-':
        result = number_one - number_two
    elif operand == '*':
        result = number_one * number_two
    return qustion , str(result)
