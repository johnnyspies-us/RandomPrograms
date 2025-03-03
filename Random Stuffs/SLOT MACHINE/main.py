import os
import random

# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Slot machine symbols & their counts
SYMBOLS = {
    "🍒": 4,  # Common
    "🍋": 6,  # More common
    "🔔": 3,  # Less common
    "💎": 2   # Rare
}

# Payout multipliers
PAYOUTS = {
    "🍒": 2,
    "🍋": 3,
    "🔔": 5,
    "💎": 10
}

def deposit():
    while True:
        clear_screen()
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")     

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else: 
            print("Please enter a number.")

def spin_slots():
    """Generates a 3x3 slot machine spin"""
    reels = []
    all_symbols = []

    # Create weighted symbol list
    for symbol, count in SYMBOLS.items():
        all_symbols.extend([symbol] * count)

    for _ in range(COLS):
        reel = random.sample(all_symbols, ROWS)
        reels.append(reel)

    return reels

def print_slots(reels):
    """Prints the slot machine grid"""
    for row in range(ROWS):
        print(" | ".join(reels[col][row] for col in range(COLS)))

def check_winnings(reels, bet, lines):
    """Checks if there are winning lines and calculates winnings"""
    winnings = 0
    winning_lines = []

    for row in range(lines):  
        if reels[0][row] == reels[1][row] == reels[2][row]:  
            symbol = reels[0][row]
            winnings += bet * PAYOUTS[symbol]  
            winning_lines.append(row + 1)  

    return winnings, winning_lines

def main():
    balance = deposit()
    
    while True:
        clear_screen()
        print(f"Current balance: ${balance}")
        
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    clear_screen()
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    # Spin the slot machine
    slots = spin_slots()
    print_slots(slots)

    # Check winnings
    winnings, winning_lines = check_winnings(slots, bet, lines)
    balance += winnings - total_bet  

    if winnings > 0:
        print(f"🎉 You won ${winnings} on lines {winning_lines}!")
    else:
        print("❌ No wins this time!")

    print(f"Your new balance is: ${balance}")

main()
