def evenorodd(number):
    if number % 2 == 0:
        print("Congrats! Your number is even!")
    else:
        print("Your number is odd!")

while True:
    number = int(input("User, please enter a number and I will magically tell you if it's even or odd: "))
    
    evenorodd(number)

    playagain = input("Would you like to play again? Enter '1' for Yes or '2' for No: ")

    if playagain != "1":  # If user doesn't enter "1", exit the loop
        print("Thanks for playing! Goodbye!")
        break

