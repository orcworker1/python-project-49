import prompt

from brain_games.cli import random_value, welcome_user


def gcd(a, b):
    list_ = []
    while b != 0:
        a, b = b, a % b
        list_.append(a)    
    return min(list_)


def main():
    name = welcome_user()
    game_count = 3
    print('Find the greatest common divisor of given numbers')
    while game_count != 0:
        number_1 = random_value()
        number_2 = random_value()
        game_count -= 1
        result = gcd(number_1, number_2)
        answer = prompt.integer(f'Question: {number_1} {number_2}\n'
                                f'Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            return (f"'{answer}' is wrong answer ;(."
                    f"Correct answer was '{result}'.\n"
                    f"Let's try again, {name}!") 
    return f'Congratulations, {name}!'    


if __name__ == '__main__':
    main()            