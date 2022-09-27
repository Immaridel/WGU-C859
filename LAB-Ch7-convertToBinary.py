def int_to_reverse_binary(int1):
    stringcat = ''
    while int1 > 0:
        string1 = (int1 % 2)
        stringcat += str(string1)
        int1 = int1 // 2
    return(stringcat)

def string_reverse(next):
    return(next[::-1])

if __name__ == '__main__':
    number_in = int(input())

    from_string = (int_to_reverse_binary(number_in))
    print(string_reverse(from_string))