"""
Banking ATM simulator App
"""

class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""
        1. Enter 1 for generate pin
        2. Enter 2. for change pin
        3. Enter 3. for check balance
        4. Enter 4. for withdraw
        5. Anything else for exit
        """)
        if user_input == "1":
            self.generate_pin()
        elif user_input == "2":
            self.change_pin()
        
        elif user_input == "3":
            self.check_balance()
        
        elif user_input == "4":
            self.withdraw()

        else:
            exit()

    def generate_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("Pin generated successfully!")
        self.menu()

    def change_pin(self):
        user_pin = input("Enter your existing pin: ")

        if user_pin == self.pin:
            new_pin= input("Enter your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully!")
        else:
            print("some error occured while changing pin re-enter your existing pin!")

        self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print("Your current balance: ",self.balance)
        else:
            print("some error occured re-enter your correct pin!")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            withdraw_balance = int(input("Enter amount: "))
            if withdraw_balance <= self.balance:
                self.balance = self.balance - withdraw_balance
                print("Collect cash!")
            else:
                print("You do not have sufficient amount to withdraw!")
        else:
            print("some error occured re-enter your correct pin!")
        self.menu()


obj = Atm()