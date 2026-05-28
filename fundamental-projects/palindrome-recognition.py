# getting the inputs

def get_input() -> str:
    user_input = input("Enter the string: ")
    return user_input

# palindrome recognition

def is_palindrome(string: str) -> bool:
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

# configuing the output based on the input

def config_output(input: bool) -> str:
    if input == True:
        return "The string is a palindrome.\n"
    else:
        return "The string is not a palindrome.\n"
    
# validate order of the user

def validate_order(order) -> bool:
    if not order in [1, 2]:
        return False
    return True

# main function

def main():
    print("Hey there! This program helps you detect if a string is palindrome or not!\n")
    while True:
        order = int(input("\nWhat do you wanna do?\n"
            "1. Detect a palindrome string\n"
            "2. Exit\n" \
            "order: "
        ))
        if not validate_order(order):
            print("Wrong order! Please give me a valid one (1 or 2)")
            continue

        if order == 2:
            print("\nGoodbye!")
            break
        
        else:
            output = config_output(
                        is_palindrome(
                            get_input()
                        )
                    )
            print(output)


if __name__ == "__main__":
    main()