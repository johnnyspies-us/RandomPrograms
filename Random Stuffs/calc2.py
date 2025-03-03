import math

# Get valid operation choice
while True:
    try:
        askoperation = input("""
        What kinda math ya wanna do?
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        Enter your choice (1-4): """)

        operation = int(askoperation)
        
        if operation < 1 or operation > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue  # Ask again
        break  # Valid input, exit loop
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")

# Get valid integer inputs
while True:
    try:
        user_input1 = input("Enter an integer: ")
        user_input2 = input("Enter a second integer: ")
        integer_value1 = int(user_input1)
        integer_value2 = int(user_input2)
        print("You entered:", integer_value1, "and", integer_value2)
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer.")
3
# Perform the chosen operation
if operation == 1:
    print("The sum of these integers is:", integer_value1 + integer_value2)
elif operation == 2:
    print("The difference of these integers is:", integer_value1 - integer_value2)
elif operation == 3:
    print("The product of these integers is:", integer_value1 * integer_value2)
elif operation == 4:
    if integer_value2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The quotient of these integers is:", integer_value1 / integer_value2)
