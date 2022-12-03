def add_2_numbers_in_base(base, number_1, number_2):
    if base == 10:
        return number_1 + number_2
    result = 0
    carry = 0
    number_of_digits = max(len(str(number_1)), len(str(number_2)))
    power = 0
    while number_of_digits > 0:
        intermediate_result = number_1 % 10 + number_2 % 10 + carry
        carry = intermediate_result // base
        result += (intermediate_result % base)*(10**power)
        power += 1
        number_2 //= 10
        number_1 //= 10
        number_of_digits -= 1
    result += carry*(10**power)
    return result


def subtract_2_numbers_in_base(base, number_1, number_2):
    if base == 10:
        return number_1 - number_2
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


print(add_2_numbers_in_base(6, 543, 32))
print(subtract_2_numbers_in_base(6, 343, 521))
