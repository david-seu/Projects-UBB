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


def equalize_string_number_to_given_length(number, length):
    while len(number) < length:
        number = '0' + number
    return number


def add_2_number_in_base_16(number_1, number_2):
    result = ''
    carry = 0
    if len(number_1) > len(number_2):
        number_2 = equalize_string_number_to_given_length(number_2, len(number_1))
    else:
        number_1 = equalize_string_number_to_given_length(number_1, len(number_2))
    while len(number_1) > 0:
        intermediate_result = convert_string_base_16_to_digit(number_1[-1])\
                              + convert_string_base_16_to_digit(number_2[-1]) + carry
        carry = intermediate_result // 16
        result = convert_digit_to_base_16(intermediate_result % 16) + result
        number_1 = number_1[:-1]
        number_2 = number_2[:-1]
    if carry != 0:
        result = convert_digit_to_base_16(carry) + result
    return result


def add_2_numbers_in_base_different_from_16(base, number_1, number_2):
    result = 0
    carry = 0
    number_of_digits = max(len(str(number_1)), len(str(number_2)))
    power = 0
    while number_of_digits > 0:
        intermediate_result = number_1 % 10 + number_2 % 10 + carry
        carry = intermediate_result // base
        result += (intermediate_result % base) * (10 ** power)
        power += 1
        number_2 //= 10
        number_1 //= 10
        number_of_digits -= 1
    result += carry * (10 ** power)
    return result


def subtract_2_numbers_in_base_16(number_1, number_2):
    result = ''
    borrow = 0
    if len(number_1) > len(number_2):
        number_2 = equalize_string_number_to_given_length(number_2, len(number_1))
    else:
        number_1 = equalize_string_number_to_given_length(number_1, len(number_2))
    sign = False
    if number_2 > number_1:
        number_2, number_1 = number_1, number_2
        sign = True
    while len(number_1) > 0:
        intermediate_result = convert_string_base_16_to_digit(number_1[-1]) \
                              - convert_string_base_16_to_digit(number_2[-1]) -borrow
        if intermediate_result < 0:
            borrow = 1
            intermediate_result += 16
        result = convert_digit_to_base_16(intermediate_result % 16) + result
        number_1 = number_1[:-1]
        number_2 = number_2[:-1]
    if sign:
        return f'-{result}'
    return result


def subtract_2_numbers_in_base_different_from_16(base, number_1, number_2):
    result = 0
    borrow = 0
    number_of_digits = max(len(str(number_1)), len(str(number_2)))
    power = 0
    sign = False
    if number_2 > number_1:
        number_2, number_1 = number_1, number_2
        sign = True
    while number_of_digits > 0:
        intermediate_result = number_1 % 10 - number_2 % 10 - borrow
        if intermediate_result < 0:
            borrow = 1
            intermediate_result += base
        result += (intermediate_result % base) * (10 ** power)
        power += 1
        number_2 //= 10
        number_1 //= 10
        number_of_digits -= 1
    if sign:
        return -result
    return result


def multiply_number_with_digit_in_base_16(number_1, number_2):
    result = ''
    carry = 0
    while len(number_1) > 0:
        intermediate_result = convert_string_base_16_to_digit(number_1[-1]) * \
                              convert_string_base_16_to_digit(number_2) + carry
        carry = intermediate_result // 16
        result = convert_digit_to_base_16(intermediate_result % 16) + result
        number_1 = number_1[:-1]
    if carry != 0:
        result = convert_digit_to_base_16(carry) + result
    return result


def multiply_number_with_digit_in_base_different_from_16(base, number_1, number_2):
    result = 0
    carry = 0
    number_of_digits = len(str(number_1))
    power = 0
    while number_of_digits > 0:
        intermediate_result = number_1 % 10 * number_2 + carry
        carry = intermediate_result // base
        result += (intermediate_result % base) * (10 ** power)
        power += 1
        number_1 //= 10
        number_of_digits -= 1
    result += carry * (10 ** power)
    return result


def divide_number_with_digit_in_base_16(number_1, number_2):
    quotient = ''
    residue = 0
    while len(number_1) > 0:
        intermediate_result = residue * 16 + convert_string_base_16_to_digit(number_1[0])
        residue = intermediate_result % convert_string_base_16_to_digit(number_2)
        quotient += convert_digit_to_base_16(intermediate_result // convert_string_base_16_to_digit(number_2))
        number_1 = number_1[1:]
    return quotient, convert_digit_to_base_16(residue)


def divide_number_with_digit_in_base_different_from_16(base, number_1, number_2):
    quotient = 0
    residue = 0
    number_of_digits = len(str(number_1))
    while number_of_digits > 0:
        intermediate_result = residue * base + number_1 // (10 ** (number_of_digits - 1))
        residue = intermediate_result % number_2
        quotient = quotient * 10 + intermediate_result // number_2
        number_1 %= 10 ** (number_of_digits - 1)
        number_of_digits -= 1
    return quotient, residue


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

def 

print(add_2_number_in_base_16('ABCD', 'E9F'))
print(add_2_numbers_in_base_different_from_16(6, 543, 32))
print(subtract_2_numbers_in_base_16('FDE', 'B97A'))
print(subtract_2_numbers_in_base_different_from_16(6, 343, 521))
print(multiply_number_with_digit_in_base_16('BF8', 'A'))
print(multiply_number_with_digit_in_base_different_from_16(5, 134, 3))
print(divide_number_with_digit_in_base_16('F09D', 'A'))
print(divide_number_with_digit_in_base_different_from_16(5, 134, 3))
print(conversion_number_from_source_base_to_destination_base_rapid_conversions('F8', 16, 8))
