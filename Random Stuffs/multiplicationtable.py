while True:
    try:
        usernumber = int(input("Please enter a number and I shall give you the multiples: "))
        usertable = int(input("How high would you like the multiplication table to go?"))
    
        for i in range(1, usertable + 1):
            print(f"{usernumber} x {i} = {usernumber * i}")
     
        
        playagain = input("Would you like to play again? yes or no: ").lower().strip()
        if playagain != "yes":
            print("Thanks for using see ya next time!")
            break
    except ValueError:  # Catch incorrect inputs
        print("Oops! Please enter a valid number.")
        continue

