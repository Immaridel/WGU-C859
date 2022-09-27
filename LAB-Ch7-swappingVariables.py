def swap_values(user_val1, user_val2):
    newuv1 = user_val2
    newuv2 = user_val1
    valcat = newuv1, newuv2
    print('{} {}'.format(newuv1, newuv2))
    return valcat


if __name__ == '__main__':
    input1 = input()
    input2 = input()

    swap_values(input1, input2)
