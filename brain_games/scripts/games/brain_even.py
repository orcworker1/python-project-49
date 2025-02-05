import prompt

from brain_games.cli import random_value, welcome_user


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    game_count = 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while game_count != 0:
        game_count -= 1
        number = random_value()
        answer = prompt.string(f'Question: {number}\n'
                                f'Your answer: ')
        if is_even(number) and answer == 'yes':
            print('Correct!')
        elif not is_even(number) and answer == 'no':
            print('Correct!')
        else:
            if answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                      f"Let's try again, {name}!")
                game_count = -1
                break
            else:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                      f"Let's try again, {name}!")
                game_count = -1
                break
    if game_count == 0:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()