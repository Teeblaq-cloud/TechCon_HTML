# Ask the user to input a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    # Increment the row counter
    row += 1
