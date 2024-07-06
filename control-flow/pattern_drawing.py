# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks side by side without advancing to a new line
        for col in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        row += 1
