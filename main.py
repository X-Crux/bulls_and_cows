from engine import check_number, guess_number
from termcolor import cprint, colored


def start_game():
    choise = ''
    move = 0

    while choise.lower() != 'н':
        if move == 0:
            choise = ''
            guess_number()
            cprint('Программа загадала 4-х значное число. Попробуйте отгадать!', color='green')
        number = str(input(colored('Введите 4-х значное целое число: ', color='green')))
        move += 1
        animals_dict = check_number(number=number)

        print(colored('Быков:', color='blue'), colored(animals_dict['bulls'], color='blue'))
        print(colored('Коров:', color='blue'), colored(animals_dict['cows'], color='blue'))

        if animals_dict['bulls'] == 4:
            print(colored('Победа! Вы угадали число! Количество ходов:', color='magenta'),
                  colored(move, color='magenta'), colored('\nХотите еще партию?', color='magenta'))

            while choise.lower() != 'д':
                choise = str(input(colored('Введите команду Д/н: ', color='cyan')))
                if choise.lower() == 'н':
                    cprint('Ждем вас снова!', color='magenta')
                    break
                elif choise.lower() == 'д':
                    move = 0
                    break
                else:
                    cprint('Не известная команда.', color='red')


if __name__ == '__main__':
    start_game()
