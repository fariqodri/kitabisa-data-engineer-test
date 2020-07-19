from command import FirstPrimesCommand, SortAndCombineCommand
from invoker import Invoker

if __name__ == '__main__':
    print('Please select:')
    print('1. First N prime numbers')
    print('2. Sort and combine')
    try:
        invoker = Invoker()
        user_input = int(input('>> '))
        if user_input != 1 and user_input != 2:
            raise ValueError
        elif user_input == 1:
            n = int(input('N = '))
            invoker.set_command(FirstPrimesCommand(n))
            invoker.execute_command()
        else:
            first = input('First array (separated by comma without square brackets): ').split(',')
            second = input('Second array (separated by comma without square brackets): ').split(',')
            invoker.set_command(SortAndCombineCommand(first, second))
            invoker.execute_command()
    except ValueError:
        print('Invalid input')
