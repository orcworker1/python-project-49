import prompt

from brain_games.cli import welcome_user , random_value


def is_prime(numbers):
    count = 0
    if numbers == 1:
        return False
    for i in range(1,numbers + 1 ):
        if numbers % i == 0:
            count += 1
    if count > 2:
        return False
    return True
    
    
def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_count = 3
    while game_count != 0:
        number = random_value()
        game_count -= 1
        answer = prompt.string(f"Question: {number}\n"
                               f'Your answer: ')
        if is_prime(number) and answer == 'yes':
            print('Correct!')
        elif not is_prime(number) and answer == 'no':
            print('Correct!')   
        else:
            if answer == 'yes':
                return  (f"'{answer}' is wrong answer ;(."
                         f"Correct answer was 'no'.\n"
                         f"Let's try again, {name}!")
            else:
                return (f"'{answer}' is wrong answer ;(."
                       f"Correct answer was 'yes'.\n"
                       f"Let's try again, {name}!")
    return f'Congratulations, {name}!'        
        



        




if __name__ == "__main__":
    main()






