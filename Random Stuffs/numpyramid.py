
n = int(input("Put a number in here"))

for i in range(1, n + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for numbers in the row
        print(j, end=" ")  # Print the number with space
    print()  # Move to the next line after each row