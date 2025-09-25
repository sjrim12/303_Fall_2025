import string
import datetime

alphabet = list(string.ascii_lowercase)

def encode(input_text, shift):
    result = ""
    for char in input_text:
        if char.isalpha():
            base = ord('a')
            char = char.lower()
            shifted = (ord(char) - base + shift) % 26
            new_char = chr(base + shifted)
            result += new_char
        else:
            result += char
    return (alphabet, result)

def decode(input_text, shift):
    result = ""
    for char in input_text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base - shift) % 26
            new_char = chr(base + shifted)
            result += new_char
        else:
            result += char
    return result

class BankAccount:
    def __init__(self,name='Rainy',ID=1234,create_date=datetime.date.today(),balance = 0):
        if create_date > datetime.date.today():
            raise Exception("Invalid Creation date")
        self.name = name
        self.ID = ID
        self.create_date = create_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Negative deposit amounts are not allowed")
            return
        self.balance += amount
        print('New Balance: ', self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("New Balance: ", self.balance)

    def view_balance(self):
        print ("Current Balance is :", self.balance)

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        acct_age = (datetime.date.today() - self.create_date).days
        if acct_age < 180:
            print("Cannot withdraw from account until it has existed from 180 days")
            return
        if amount < 0:
            print("Cannot withdraw negative amount")
            return
        elif amount > self.balance:
            print("Cannot withdraw more than the account balance")
            return
        return super().withdraw(amount)
    
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        super().withdraw(amount)
        if self.balance < 0:
            self.balance -= 30
            print("You have incurred a $30 fee for overdrafting your account")
        return
# 303_Fall_2025
