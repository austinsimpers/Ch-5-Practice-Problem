def get_input():
    return float(input("Enter a positive number to add (negative to quit): "))

def add_numbers(total, number):
    return total + number

def print_output(total):
    print(f"The total is: {total}")

def main():
    total = 0
    while True:
        number = get_input()
        if number < 0:
            break
        total = add_numbers(total, number)
    print_output(total)

main()
