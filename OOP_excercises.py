# class Bank:
#     __interest_rate = 12
#     __bank_name = 'Bro Bank'

#     def __init__(self, first_name, last_name, age):
#         self.__first_name = first_name
#         self.__last_name = last_name
#         self._age = age
#         self.__balance = 0

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, deposit_amount):
#         if deposit_amount < 0:
#             print('invalid amount')
#         else:
#             self.__balance = self.__balance + deposit_amount

#     def get_full_name(self):
#         return f'{self.__first_name} {self.__last_name}'

#     def withdraw_balance(self, withdrawl_amount):
#         if withdrawl_amount < 0:
#             print('invalid amount')
#         elif withdrawl_amount > self.__balance:
#             print('insufficient balance')
#         else:
#             self.__balance = self.__balance - withdrawl_amount

#     @classmethod
#     def get_bank_name(cls):
#         return cls.__bank_name

#     @classmethod 
#     def get_interest_rate(cls):
#         return cls.__interest_rate
    
#     @classmethod
#     def set_interest_rate(cls, new_rate):
#         if new_rate < 0:
#             print('invalid interest rate')
#             return
#         Bank.__interest_rate = new_rate

#     @staticmethod
#     def print_govt_holidays():
#         print('Dashain ko masu khane bida is for 10 days')
#         print('Tihar ko sel khane bida is for 5 days')
    
# account = None
# while True:

#     print('*' * 50)
#     print(f'Welcome to {Bank.get_bank_name()}')

#     choice = input('Enter 1 to open an account. \nEnter 2 to check balance. \nEnter 3 to deposit balance. \nEnter 4 to withdraw balance. \nEnter 5 to get interest rate. \nEnter 6 to set interest rate. \nEnter 7 to check holdays. ')

#     print('*' * 50)

#     if choice == '1':
#         fn = input('Enter first name ')
#         ln = input('Enter last name ')
#         age = input('Enter age ')

#         account = Bank(first_name=fn, last_name=ln, age=age)

#         print(f'Congratulations {account.get_full_name().title()}')
    
#     elif choice == '2'and account is not None:
#         print(f'Your current balance is {account.get_balance()}')
    
#     elif choice == '3' and account is not None:
#         deposit_amount = float(input('Enter deposit amount '))
#         rounded_amount = round(deposit_amount, 2)
#         account.set_balance(deposit_amount=deposit_amount)
#         print(f'Updated balance is {account.get_balance()}')

#     elif choice == '4' and account is not None:
#         withdrawl_amount = float(input('Enter withdrawl amount '))
#         account.withdraw_balance(withdrawl_amount)
#         print(f'Updated balance is {account.get_balance()}')

#     elif choice == '5':
#         rate = Bank.get_interest_rate()
#         print(f"Bank's current interest rate is {rate}")

#     elif choice == '6':
#         print('WARNING!!')
#         print('DONOT CHANGE INTEREST RATE WITHOUT PERMISSION')
#         rate_change_choice = input('Enter 0 to exit and 1 to continue ')
#         if rate_change_choice == '0':
#             continue
#         elif rate_change_choice == '1':
#             new_rate = int(input('Enter new interest rate '))
#             Bank.set_interest_rate(new_rate)
#             print(f'Updated interest rate is {Bank.get_interest_rate()}')

#     elif choice == '7':
#         Bank.print_govt_holidays()
    
#     elif account is None:
#         print('Please create account first.')
#     else:
#         print('Please enter a valid choice')