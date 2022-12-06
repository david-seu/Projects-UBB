from LogicOptionalHomework.functions.base16 import convert_number_from_base_10_to_base_16, \
    convert_number_from_base_16_to_base_10


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
        number_1 = convert_number_from_base_16_to_base_10(number_1)
        number_2 = convert_number_from_base_16_to_base_10(number_2)
        return convert_number_from_base_10_to_base_16(number_1 + number_2)
    number_1 = convert_number_from_base_different_from_16_to_base_10(number_1, base)
    number_2 = convert_number_from_base_different_from_16_to_base_10(number_2, base)
    return convert_number_from_base_10_to_base_different_from_16(number_1 + number_2, base)


def subtract_two_numbers_in_base(base, number_1, number_2):
    if base == 10:
        return number_1 - number_2
    if base == 16:
        number_1 = convert_number_from_base_16_to_base_10(number_1)
        number_2 = convert_number_from_base_16_to_base_10(number_2)
        return convert_number_from_base_10_to_base_16(number_1 - number_2)
    number_1 = convert_number_from_base_different_from_16_to_base_10(number_1, base)
    number_2 = convert_number_from_base_different_from_16_to_base_10(number_2, base)
    return convert_number_from_base_10_to_base_different_from_16(number_1 - number_2, base)


def multiply_number_with_digit_in_base(base, number, digit):
    if base == 10:
        return number * digit
    if base == 16:
        number = convert_number_from_base_16_to_base_10(number)
        digit = convert_number_from_base_16_to_base_10(digit)
        return convert_number_from_base_10_to_base_16(number * digit)
    number = convert_number_from_base_different_from_16_to_base_10(number, base)
    digit = convert_number_from_base_different_from_16_to_base_10(digit, base)
    return convert_number_from_base_10_to_base_different_from_16(number * digit, base)


def divide_number_with_digit_in_base(base, number, digit):
    if base == 10:
        return number // digit, number % digit
    if base == 16:
        number = convert_number_from_base_16_to_base_10(number)
        digit = convert_number_from_base_16_to_base_10(digit)
        quotient = convert_number_from_base_10_to_base_16(number // digit)
        if number % digit == 0:
            remainder = '0'
        else:
            remainder = convert_number_from_base_10_to_base_16(number % digit)
    else:
        number = convert_number_from_base_different_from_16_to_base_10(number, base)
        digit = convert_number_from_base_different_from_16_to_base_10(digit, base)
        quotient = convert_number_from_base_10_to_base_different_from_16(number // digit, base)
        if number % digit == 0:
            remainder = 0
        else:
            remainder = convert_number_from_base_10_to_base_different_from_16(number % digit, base)
    return quotient, remainder
