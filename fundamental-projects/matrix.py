# imports
import string

# getting the inputs from the user

def get_input() -> list:

    row1 = input("give me the first row (separated by spaces): ")
    while not validate_input(row1):
        print("Invalid input, try again\n" \
        "   (sample input: 1 2 3)")
        row1 = input("give me the first row (separated by spaces): ")

    row2 = input("give me the second row (separated by spaces): ")
    while not validate_input(row2):
        print("Invalid input, try again\n" \
        "   (sample input: 1 2 3)")
        row2 = input("give me the second row (separated by spaces): ")

    row3 = input("give me the third row (separated by spaces): ")
    while not validate_input(row3):
        print("Invalid input, try again\n" \
        "   (sample input: 1 2 3)")
        row3 = input("give me the third row (separated by spaces): ")

    output = row1.split(" ") + row2.split(" ") + row3.split(" ")
    for i in range(len(output)):
        output[i] = int(output[i])

    return output

# validate input

def validate_input(user_input: str) -> bool:
    if len(user_input) != 5:
        return False
    for _ in user_input[::2]:
        if not _ in string.digits:
            return False
    for _ in user_input[1::2]:
        if _ != " ":
            return False
    return True

def validate_order(order) -> bool:
    if order in [1, 2]:
        return True
    return False

# calculate the sum of the rows

def rows_sum(matrix: list) -> list:
    output = [0, 0, 0]
    for i in range(3):
        output[i] += matrix[3*i] + matrix[3*i+1] + matrix[3*i+2]

    return output

# calculate the sum of the columns

def cols_sum(matrix: list) -> list:
    output = [0, 0, 0]
    for i in range(3):
        output[i] += matrix[i] + matrix[i+3] + matrix[i+6]

    return output

# configure the output message

def config_output(rows_sum: list, cols_sum: list) -> str:
    
    return f"Row sums:\n" \
    f"   row1 -> {rows_sum[0]}\n" \
    f"   row2 -> {rows_sum[1]}\n" \
    f"   row3 -> {rows_sum[2]}\n\n" \
    f"column sums:\n" \
    f"   column1: {cols_sum[0]}\n" \
    f"   column2: {cols_sum[1]}\n" \
    f"   column3: {cols_sum[2]}\n"

# main function

def main():
    print("Hey there! This is a matrix simple calculator!")
    while True:
        order = int(input(
            "What do you want to do?\n" \
            "1. Calculate rows and columns sum of a matrix\n" \
            "2. Exit\n" \
            "order: "
        ))
        if not validate_order(order):
            print("Invalid order, try again")
            continue

        if order == 2:
            print("\nGoodbye!")
            break
        
        if order == 1:
            input_list = get_input()
            output = config_output(rows_sum(input_list), cols_sum(input_list))
            print(output)


if __name__ == "__main__":
    main()