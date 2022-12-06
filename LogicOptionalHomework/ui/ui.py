import LogicOptionalHomework.functions.conversions as conversion
import LogicOptionalHomework.functions.operations as operation


def find_command_type(command):
    command = command.split(' ')
    command_type = command[2]
    command_arguments = command[:2] + command[3:]
    return command_type, command_arguments


def menu():
    commands = {
        '+': execute_command_add,
        '-': execute_command_subtract,
        '*': execute_command_multiply,
        '/': execute_command_divide,
        '=': execute_command_convert
    }
    print("""
Welcome to base converter and calculator!

Commands:
1. Add two numbers in a base : <<base first_number + second_number>>
2. Subtract two numbers in a base : <<base first_number - second_number>>
3. Multiply a number by a digit in a base : <<base number * digit>>
4. Divide a number by a digit in a base : <<base number / digit>>
5. Convert a number between two bases: <<source_base destination_base = number>>
6. Exit: <<x>>
    """)
    available_command_types = ('+', '-', '*', '/', '=')
    command = None
    while True:
        if command is None:
            print('Choose a command from above: ', end='')
        command = input()
        command_type, command_arguments = find_command_type(command)
        if command_type == '':
            print("You haven't entered a command! Enter one now: ", end='')
        elif command_type not in available_command_types:
            print('No command is recognized here! Please try again: ', end='')
        else:
            command = None
            if command == 'x':
                print('Have a nice day!')
                break
            try:
                commands[command_type](command_arguments)
            except (ValueError, AttributeError, AssertionError, IndexError, TypeError, SyntaxError) as error:
                print(error)


def execute_command_add(command_arguments):
    if len(command_arguments) == 3:
        try:
            base = int(command_arguments[0])
            if base == 16:
                first_number = command_arguments[1].upper()
                second_number = command_arguments[2].upper()
            else:
                first_number = int(command_arguments[1])
                second_number = int(command_arguments[2])
        except (ValueError, IndexError):
            raise SyntaxError("Syntax error")
        print(f' {first_number} + {second_number} = '
              f'{operation.add_two_numbers_in_base(base, first_number, second_number)} (base {base})')
    else:
        raise SyntaxError('Too many arguments for your command')


def execute_command_subtract(command_arguments):
    if len(command_arguments) == 3:
        try:
            base = int(command_arguments[0])
            if base == 16:
                first_number = command_arguments[1].upper()
                second_number = command_arguments[2].upper()
            else:
                first_number = int(command_arguments[1])
                second_number = int(command_arguments[2])
        except (ValueError, IndexError):
            raise SyntaxError("Syntax error")
        print(f' {first_number} - {second_number} = '
              f'{operation.subtract_two_numbers_in_base(base, first_number, second_number)} (base {base})')
    else:
        raise SyntaxError('Too many arguments for your command')


def execute_command_multiply(command_arguments):
    if len(command_arguments) == 3:
        try:
            base = int(command_arguments[0])
            if base == 16:
                number = command_arguments[1].upper()
                digit = command_arguments[2].upper()
            else:
                number = int(command_arguments[1])
                digit = int(command_arguments[2])
        except (ValueError, IndexError):
            raise SyntaxError("Syntax error")
        print(f' {number} * {digit} = '
              f'{operation.multiply_number_with_digit_in_base(base, number, digit)} (base {base})')
    else:
        raise SyntaxError('Too many arguments for your command')


def execute_command_divide(command_arguments):
    if len(command_arguments) == 3:
        try:
            base = int(command_arguments[0])
            if base == 16:
                number = command_arguments[1].upper()
                digit = command_arguments[2].upper()
            else:
                number = int(command_arguments[1])
                digit = int(command_arguments[2])
        except (ValueError, IndexError):
            raise SyntaxError("Syntax error")
        quotient, remainder = operation.divide_number_with_digit_in_base(base, number, digit)
        print(f' {number} / {digit} = '
              f'{quotient} remainder {remainder} (base {base})')
    else:
        raise SyntaxError('Too many arguments for your command')


def execute_command_convert(command_arguments):
    if len(command_arguments) == 3:
        try:
            source_base = int(command_arguments[0])
            destination_base = int(command_arguments[1])
            if source_base == 16:
                number = command_arguments[2].upper()
            else:
                number = int(command_arguments[2])
            if source_base and destination_base in (2, 4, 8, 16):
                print(f'{number} converted from base {source_base} to {destination_base} is: '
                      f'{conversion.conversion_number_from_source_base_to_destination_base_rapid_conversions(number, source_base, destination_base)}')
            elif source_base < destination_base:
                print(f'{number} converted from base {source_base} to {destination_base} is: '
                      f'{conversion.convert_number_from_source_base_to_destination_base_substitution_method(number, source_base, destination_base)}')
            elif source_base > destination_base:
                print(f'{number} converted from base {source_base} to {destination_base} is: '
                      f'{conversion.convert_number_from_source_base_to_destination_base_successive_divisions(number, source_base, destination_base)}')
            else:
                raise ValueError('Your source base is the same as the destination base')
        except (ValueError, IndexError):
            raise SyntaxError('Syntax error')
    else:
        raise SyntaxError('Too many arguments for your command')
