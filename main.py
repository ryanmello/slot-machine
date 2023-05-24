import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number greater than 0")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like? (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? (" + str(MIN_BET) + "-" + str(MAX_BET) + "): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        if bet * lines > balance:
            print("Insufficient funds")
        else:
            break
    
    total_bet = bet * lines
    
    print(f"You are betting ${bet} on {lines} lines.")
    print(f"Total Bet: ${total_bet}")
    
main()
    
