def main():
    total = 0
    count = 0
    try:
        infile = open("numbers.txt", "r")
        for line in infile:
            total += float(line)
            count += 1
        infile.close()
        if count > 0:
            average = total / count
            print("Sum:", total)
            print("Average:", average)
        else:
            print("The file contains no numbers.")
    except IOError:
        print("Error: could not open or read numbers.txt")
    except ValueError:
        print("Error: the file contains a non-numeric value.")

main()
