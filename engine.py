from random import randint

_number = ''


def guess_number():
    first_number = randint(1, 9)
    global _number
    _number = str(first_number)
    while True:
        next_number = str(randint(0, 9))
        if next_number not in _number:
            _number += next_number
        if len(_number) == 4:
            break


def check_number(number):
    animals_dict = {'bulls': 0, 'cows': 0}
    for i in range(len(number)):
        if number[i] in _number:
            animals_dict['cows'] += 1
            if number[i] == _number[i]:
                animals_dict['bulls'] += 1
                animals_dict['cows'] -= 1
    return animals_dict
