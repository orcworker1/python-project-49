import random

DESCRIPTION = 'What number is missing in the progression?'

def generate_round():
    new_list = []
    start = random.randint(1, 100)
    step = random.randint(2, 5)
    lenght = random.randint(5, 10)
    for i in range(0, lenght):
        new_list.append(start + i * step)
    random_index = random.randint(0,len(new_list) - 1)
    correct_answer = new_list[random_index]
    new_list[random_index] = '..'
    qestion = ' '.join(map(str, new_list)) 
    return qestion, str(correct_answer)