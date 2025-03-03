
import os
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
JACKPOT_MULTIPLIER = 50
JACKPOT_CHANCE = 100  # 1 in 100 chance

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def deposit():
    while True:
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
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")

def spin_slot_machine():
    return random.randint(1, JACKPOT_CHANCE) == 1  # 1 in JACKPOT_CHANCE chance

def main():
    balance = deposit()
    while True:
        clear_screen()
        print(f"Current balance: ${balance}")
        lines = get_number_of_lines()
        
        while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
            else:
                break
        
        balance -= total_bet
        print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
        
        if spin_slot_machine():
            winnings = bet * JACKPOT_MULTIPLIER
            print(f"JACKPOT!!! You won ${winnings}!")
            balance += winnings
        else:
            print("No jackpot this time. Better luck next spin!")
        
        print(f"Your new balance is ${balance}")
        
        if balance <= 0:
            print("You're out of money! Game over.")
            break
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(f"You cashed out with ${balance}. Thanks for playing!")
            break

if __name__ == "__main__":
    main()
