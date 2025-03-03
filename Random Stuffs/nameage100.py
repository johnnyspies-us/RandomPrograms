def program():
    print("Welcome user to my magnificent program!")
    usersname = input("So user, what should I call you? ")
    
    age = int(input(f"Okay, {usersname}, might as well get your age too just so we're on the same page: "))
    
    year_turn_100 = (2025 - age) + 100  # Now correctly using 2025
    
    print(f"Well hello, {usersname}! I see you're {age} years old. Did you know that you will turn 100 in the year {year_turn_100}?")

program()