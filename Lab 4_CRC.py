def performXOR(string_1, string_2):

    bin_string_1 = int(string_1, 2)
    bin_string_2 = int(string_2, 2)

    bin_string_xor = bin(bin_string_1, bin_string_2)[2:]
    zero_append = '0' * (3 - len(bin_string_xor))
    bin_string_xor = zero_append + bin_string_xor

    return bin_string_xor

def binaryDivision(divisor, dividend, check=False):

    if(check == False):

        dividend = dividend + ((len(divisor) - 1) * '0')
