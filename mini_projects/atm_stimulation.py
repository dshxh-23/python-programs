from custom_modules import custom_getters
from custom_modules import custom_exceptions

class ATM:

    # Constructor
    def __init__(self):
        self.balance = 0

    # Getter
    @property
    def balance(self):
        return self._balance
    
    # Setter
    @balance.setter
    def balance(self, bal):
        self._balance = bal   

    # Instance Methods
    def deposit(self):
        amt = custom_getters.get_float("Enter amount to deposit: ", 0, 999999)
        self.balance += amt

    def withdraw(self):
        while True:
            try:
                amt = custom_getters.get_float("Enter amount to withdraw: ", 0, 999999)
                if amt > self.balance:
                    raise ValueError
            except ValueError:
                print("Not enough balance..")
        
    # Some class methods
    @classmethod
    def display_menu(cls):
        print("1.\tCheck Balance")
        print("2.\tDeposit")
        print("3.\tWithdraw")
        print("4.\tExit")

    @classmethod
    def get_choice(cls):
        while True:
            try:
                ip = input("INPUT: ")
                choice = int(ip)
                if choice not in range(1, 5):
                    raise custom_exceptions.InvalidValueError
                return choice
            except custom_exceptions.InvalidValueError:
                print("Kindly enter an integer between 1 to 4")
            except ValueError:
                print("Kindly enter an integer between 1 to 4")



def main():
    atm = ATM()
    while True:
        ATM.display_menu()
        ip = ATM.get_choice()
        if ip == 1:
            print(f"\nBalance: {atm.balance}\n")
        elif ip == 2:
            atm.deposit()
        elif ip == 3:
            atm.withdraw()
        else:
            break
        



if __name__ == "__main__":
    main()