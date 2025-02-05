import random

import prompt

from brain_games.cli import welcome_user


def list_numbers():
    new_list = []
    start = random.randint(1, 100)
    step = random.randint(2, 5)
    lenght = random.randint(5, 10)
    for i in range(0, lenght):
        new_list.append(start + i * step)
    return new_list   
    

def str_list(number):
    return ' '.join(map(str, number))


def random_index(numbers):
    len_numbers = len(numbers)
    return random.randint(0, len_numbers - 1)


def main():
    name = welcome_user()
    game_cout = 3
    print('What number is missing in the progression?')
    while game_cout != 0:
        inv_list = list_numbers()
        index_random = random_index(inv_list)
        corect_value = inv_list[index_random]
        inv_list[index_random] = '..'
        str_numbers = str_list(inv_list)
        game_cout -= 1
        answer = prompt.integer(f'Qustion: {str_numbers}\n'
                                f'Your answer: ')
        if answer == corect_value:
            print('Correct!')
        else:
            game_cout = -1
            print(f'{answer} is wrong answer ;(. Correct answer was: '
                        f"'{corect_value}' \n"
                        f"Let's try again, {name}!")
            break
    if game_cout == 0:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()    