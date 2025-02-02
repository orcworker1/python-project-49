import prompt

from brain_games.cli import random_operand, random_value, welcome_user


def calc():
    name = welcome_user()
    game_count = 3
    while game_count != 0:
        number_1 = random_value()
        number_2 = random_value()
        operand = random_operand()
        game_count -= 1
        answer = prompt.integer(f'What is the result of the expression?\n'
               f'Question: {number_1} {operand} {number_2}\n'
               f'Your answer: ')
        if operand == '+':
            result = number_1 + number_2
        elif operand == '-':
            result = number_1 - number_2
        elif operand == '*':
            result = number_1 * number_2
        if result == answer:
            print('Correct!')
        else: 
            return print(f'{answer} is wrong answer ;(. Correct answer was.'
                        f"{result} \n"
                        f"Let's try again, {name} ")
    print(f'Congratulations, {name}!')


def main():
    calc()
    

if __name__ == '__main__':
    main()    