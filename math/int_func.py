import string


digits = string.digits + string.ascii_lowercase
numbers = {}

for i in range(len(digits)):
    numbers[digits[i]] = i


def my_int(num: str, base: int = 10) -> int:
    result, mult = 0, 1

    nlist = list(num)
    nlist.reverse()

    for ch in nlist:
        result += numbers[ch] * mult
        mult *= base

    return result


def int_to_str(num: int, base: int) -> str:
    pass
