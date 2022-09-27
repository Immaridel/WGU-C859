def get_num_of_characters(input_str):
    caw = len(input_str)
    return(caw)


def output_without_whitespace(input_str):
    caw2 = str("")
    for i in input_str:
        if not i.isspace():
            caw2 = caw2 + i
    return(caw2)


if __name__ == '__main__':
    sent = input("Enter a sentence or phrase:\n\n")
    print(f"You entered: {sent}\n")
    print(f'Number of characters: {get_num_of_characters(sent)}')
    print(f'String with no whitespace: {output_without_whitespace(sent)}')
