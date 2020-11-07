from mymath.int_func import my_int as mi, int_to_str as i2s

if __name__ == '__main__':
    n1 = input('Please, type number 1: ')  # n1='12af'
    n2 = input('Please, type number 2: ')  # n2='3b'
    input_base = mi(input('Input base: '))
    output_base = mi(input('Output base: '))

    ni1 = mi(n1, input_base)
    ni2 = mi(n2, input_base)

    res = i2s(ni1 + ni2, output_base)

    print('Result for "' + n1 + '+' + n2 + '":')  # Result for "12af+3b":
    print(res)
