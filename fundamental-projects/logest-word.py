# getting the input string

def get_input() -> str:
    string = input("Give me your sentence: ")
    while len(string) == 0:
        string = input("Give me your sentence: ")
        print("Enter a non-empty string!")

    return string

# finding the longest word(s)

def longest_word(string: str) -> list:
    input_list = string.split(" ")
    longest_word_len = 0
    output_list = []
    for word in input_list:
        if len(word) == longest_word_len:
            output_list.append(word)
        elif len(word) > longest_word_len:
            longest_word_len = len(word)
            output_list.clear()
            output_list.append(word)
        
    return output_list

# validators

def validate_order(order) -> bool:
    if order in [1, 2]:
        return True
    return False

# configuring the output

def config_output(words_list: list) -> str:
    output = "Longest word(s): \n"
    for word in words_list:
        output += word + f" ({len(word)} letters)\n"

    return output

# main function

def main():
    print("Hello! This is a tool you can use to find the "
        "longest words in a string! (and burn your valuable time btw)\n")
    while True:
        order = int(input("What do you want to do?\n"
        "1. Find the longest word in a sentense\n"
        "2. Exit\n" \
        "order: "
        ))
        if not validate_order(order):
            print("Invalid order, try again")
            continue

        if order == 2:
            print("Have a nice day!")
            break

        else:
            output = config_output(
                longest_word(
                    get_input()
                )
            )
            print(output)

if __name__ == "__main__":
    main()