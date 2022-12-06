from math import sqrt
from LogicOptionalHomework.functions.operations import add_two_numbers_in_base,\
    multiply_number_with_digit_in_base, divide_number_with_digit_in_base


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
    number = str(number)
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
    while number != 0 and number != '':
        number, remainder = divide_number_with_digit_in_base(source_base, number, destination_base)
        converted_number += int(remainder) * 10 ** power
        power += 1
    return converted_number
