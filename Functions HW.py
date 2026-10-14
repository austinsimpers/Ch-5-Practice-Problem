def validate(low, high):
    value = int(input("Enter a value between " + str(low) + " and " + str(high) + " "))
    while value < low or value > high:
        print("Error: value out of range.")
        value = int(input("Enter a value between " + str(low) + " and " + str(high) + " "))
    return value

def main():
    print("Please enter a time: hours, then minutes.")
    hours = validate(0, 23)
    minutes = validate(0, 59)
    print("You entered", hours, "hours and", minutes, "minutes.")

main()
