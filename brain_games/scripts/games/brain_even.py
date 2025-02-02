import prompt

from brain_games.cli import welcome_user , random_value


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False




def main():
    count = 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 0:
        number = random_value()
        answer = prompt.string(f'Question: {number}\n'
                                f'Your answer: ')
        if is_even(number) and answer == 'yes':
            print('Correct!')
        elif not is_even(number) and answer == 'no':
            print('Correct!')
        else:
            if answer == 'yes':
                return (f"'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                       f"Let's try again, {name}")
            else:
                return (f"'no' is wrong answer ;(. Correct answer was 'yes'.\n"
                       f"Let's try again, {name}")
        count -= 1
    return f'Congratulations, {name}!'


if __name__ == "__main__":
    main()