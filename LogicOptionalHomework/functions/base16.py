def convert_string_base_16_to_digit(base_16_number):
    base16 = {
        'F': 15,
        'E': 14,
        'D': 13,
        'C': 12,
        'B': 11,
        'A': 10
    }
    try:
        return base16[base_16_number]
    except KeyError:
        return int(base_16_number)


def convert_digit_to_base_16(number):
    base16 = {
        'F': 15,
        'E': 14,
        'D': 13,
        'C': 12,
        'B': 11,
        'A': 10
    }
    for key in base16.keys():
        if number == base16[key]:
            return key
    return str(number)


def convert_number_from_base_16_to_base_10(number):
    number = str(number)
    converted_number = 0
    digit_index = 0
    while number != '':
        converted_number += convert_string_base_16_to_digit(number[-1]) * (16 ** digit_index)
        number = number[:-1]
        digit_index += 1
    return converted_number


def convert_number_from_base_10_to_base_16(number):
    converted_number = ''
    power = 0
    while number != 0:
        converted_number = convert_digit_to_base_16(number % 16) + converted_number
        power += 1
        number //= 16
    return converted_number
