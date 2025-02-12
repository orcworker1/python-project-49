import prompt

GAME_COUNT = 3


def run(game):
    count = GAME_COUNT
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    while count != 0:
        count -= 1
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was" 
                  f" '{correct_answer}'.\n"
                  f"Let's try again, {name}!") 
            return
    print(f'Congratulations, {name}!')    




    

    
    

