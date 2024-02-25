class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

def main():
    atm = ATM()
    
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Your balance is:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            if atm.deposit(amount):
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if atm.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid amount.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
