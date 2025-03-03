import math

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

askoperation = input("""
                 What would you like to do with these integers?
                  1. Add
                  2. Subtract
                  3. Multiply
                  4. Divide
                  """)

operation = int(askoperation)

if operation == 1:
    print("These integers added together are equal to ", (integer_value1 + integer_value2))\
elif operation == 3:
    print("These integers multiplied by eachother are equal to", (integer_value1*integer_value2))
elif operation == 4:
    print("These integers divided by eachother are equal to ",(integer_value1/integer_value2))
elif  operation == 2:
    print("These integers subtracted from eachother are equal to ", (integer_value1 - integer_value2))
else operation >= 5 or < 1:
    print("Please choose a valid operator!") 