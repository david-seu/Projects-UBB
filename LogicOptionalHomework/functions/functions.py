from math import sqrt


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


def convert_number_from_base_different_from_16_to_base_10(number, source_base):
    converted_number = 0
    digit_index = 0
    while number != 0:
        converted_number += number % 10 * (source_base ** digit_index)
        number //= 10
        digit_index += 1
    return converted_number


def convert_number_from_base_10_to_base_different_from_16(number, destination_base):
    converted_number = 0
    power = 0
    while number != 0:
        converted_number += (number % destination_base) * (10 ** power)
        power += 1
        number //= destination_base
    return converted_number


def add_two_numbers_in_base(base, number_1, number_2):
    if base == 10:
        return number_1 + number_2
    if base == 16:
        return convert_number_from_base_10_to_base_16(convert_number_from_base_16_to_base_10(number_1)
                                                      + convert_number_from_base_16_to_base_10(number_2))
    return convert_number_from_base_10_to_base_different_from_16(
        convert_number_from_base_different_from_16_to_base_10(number_1, base)
        + convert_number_from_base_different_from_16_to_base_10(number_2, base), base)


def subtract_two_numbers_in_base(base, number_1, number_2):
    if base == 10:
        return number_1 - number_2
    if base == 16:
        return convert_number_from_base_10_to_base_16(convert_number_from_base_16_to_base_10(number_1)
                                                      - convert_number_from_base_16_to_base_10(number_2))
    return convert_number_from_base_10_to_base_different_from_16(
        convert_number_from_base_different_from_16_to_base_10(number_1, base)
        - convert_number_from_base_different_from_16_to_base_10(number_2, base), base)


def multiply_number_with_digit_in_base(base, number, digit):
    if base == 10:
        return number * digit
    if base == 16:
        return convert_number_from_base_10_to_base_16(convert_number_from_base_16_to_base_10(number) *
                                                      convert_number_from_base_16_to_base_10(digit))
    return convert_number_from_base_10_to_base_different_from_16(
        convert_number_from_base_different_from_16_to_base_10(number, base)
        * convert_number_from_base_different_from_16_to_base_10(digit, base), base)


def divide_number_with_digit_in_base(base, number, digit):
    if base == 10:
        return number * digit
    if base == 16:
        return convert_number_from_base_10_to_base_16(convert_number_from_base_16_to_base_10(number) //
                                                      convert_number_from_base_16_to_base_10(digit)), \
               convert_number_from_base_10_to_base_16(convert_number_from_base_16_to_base_10(number) %
                                                      convert_number_from_base_16_to_base_10(digit))
    return convert_number_from_base_10_to_base_different_from_16(
        convert_number_from_base_different_from_16_to_base_10(number, base)
        // convert_number_from_base_different_from_16_to_base_10(digit, base), base),\
           convert_number_from_base_10_to_base_different_from_16(
               convert_number_from_base_different_from_16_to_base_10(number, base),
               convert_number_from_base_different_from_16_to_base_10(digit, base), base)


def convert_number_from_base_2_to_destination_base(number, destination_base, correspondence_table_base_2, base_index):
    power = 0
    converted_number = ''
    while number != 0:
        converted_number = str(
            correspondence_table_base_2[number % 10000][base_index[destination_base]]) + converted_number
        power += 1
        number //= 10000
    return converted_number


def convert_number_from_base_power_of_2_to_base_2(number, source_base, correspondence_table_base_2, base_index):
    power = 0
    converted_number = 0
    while number != '':
        for base_2_number, power_of_2_base_number in correspondence_table_base_2.items():
            if number[0] == str(power_of_2_base_number[base_index[source_base]]):
                converted_number = converted_number * (10 ** int(sqrt(source_base))) ** power + base_2_number
                power += 1
                break
        number = number[1:]
    return converted_number


def conversion_number_from_source_base_to_destination_base_rapid_conversions(number, source_base, destination_base):
    correspondence_table_base_2 = {
        0: [0, 0, 0],
        1: [1, 1, 1],
        10: [2, 2, 2],
        11: [3, 3, 3],
        100: [10, 4, 4],
        101: [11, 5, 5],
        110: [12, 6, 6],
        111: [13, 7, 7],
        1000: [20, 10, 8],
        1001: [21, 11, 9],
        1010: [22, 12, 'A'],
        1011: [23, 13, 'B'],
        1100: [30, 14, 'C'],
        1101: [31, 15, 'D'],
        1110: [32, 16, 'E'],
        1111: [33, 17, 'F']
    }
    base_index = {
        4: 0,
        8: 1,
        16: 2
    }
    if source_base == 2:
        converted_number = convert_number_from_base_2_to_destination_base(number, destination_base,
                                                                          correspondence_table_base_2, base_index)
    elif destination_base == 2:
        converted_number = convert_number_from_base_power_of_2_to_base_2(number, source_base,
                                                                         correspondence_table_base_2, base_index)
    else:
        converted_number = convert_number_from_base_power_of_2_to_base_2(number, source_base,
                                                                         correspondence_table_base_2, base_index)
        converted_number = convert_number_from_base_2_to_destination_base(converted_number, destination_base,
                                                                          correspondence_table_base_2, base_index)
    return converted_number


def convert_number_from_source_base_to_destination_base_substitution_method(number, source_base, destination_base):
    converted_number = 0
    digit_index = 0
    while number != 0:
        scalar = 1
        for _ in range(digit_index):
            scalar = multiply_number_with_digit_in_base(destination_base, scalar, source_base)
        converted_number = add_two_numbers_in_base(destination_base, converted_number,
                                                   multiply_number_with_digit_in_base(destination_base, scalar,
                                                                                      number % 10))
        number //= 10
        digit_index += 1
    return converted_number


def convert_number_from_source_base_to_destination_base_successive_divisions(number, source_base, destination_base):
    converted_number = 0
    power = 0
    while number != 0:
        number, residue = divide_number_with_digit_in_base(source_base, number, destination_base)
        converted_number += residue * 10 ** power
        power += 1
    return converted_number


print(convert_number_from_source_base_to_destination_base_substitution_method(1021, 6, 8))
print(convert_number_from_source_base_to_destination_base_successive_divisions(1222, 6, 4))
