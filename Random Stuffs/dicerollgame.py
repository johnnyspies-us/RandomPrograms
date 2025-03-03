import random
def script():
# Function to roll a single die
    def diceroll():
        return random.randint(1, 6)  # Ensures values from 1 to 6

# Rolling three dice
    dicenum = diceroll()
    dicenum1 = diceroll()
    dicenum2 = diceroll()

# Display results
    print("Your first roll landed on:", dicenum)
    print("Your second roll landed on:", dicenum1)
    print("Your third roll landed on:", dicenum2)

# Calculate score
    score = dicenum + dicenum1 + dicenum2

# Display score evaluation
    if score == 18:
        print("You got the highest score!", score)
    elif score < 10:
        print("You got a decent score!", score)
    elif score >= 10 and score < 18:
        print("You got a bad score!", score)
    elif score == 3:
        print("You got the worst score!", score)

    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
script()