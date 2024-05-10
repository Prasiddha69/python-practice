# class Student:
#     __school_name = 'Deerwalk School'
#     __school_address = 'Sifal'
#     def __init__(self, fn, ln, addr, a):
#         self.__first_name = fn
#         self.__last_name = ln
#         self.__address = addr
#         self.__age = a

#     def get_full_name(self):
#         return f'{self.__first_name} {self.__last_name}'

#     def get_age(self):
#         return self.__age

#     @classmethod
#     def school_name(cls):
#         return Student.__school_name

#     @staticmethod
#     def add():
#         print(1+1)

#     @staticmethod
#     def add_2(i,j):
#         print(i+j)


# s = Student('ram', 'hari', 'nepal', 28)
# Student.add()
# Student.add_2(2,3)
# print(Student.school_name())
# print(s.get_full_name())
# print(s.get_age())
# Type of methods
# instance method
    # methods that access instance variable 
    # self should be the first parameter
    # accessed by using object name outside of the class and by using self inside the class
# classmethod
    # method that access class level/static variable 
    # cls should be the first parameter
    # @classmethod decorator is required
    # access by using class name both inside and outside of the class
# staticmethod
    # does not depend on either class or object
    # @staticmethod decorator is required
    # can be paramterized or parameterless
    # accessed by using class name both inside and outside of the class


# class Student:
#     __school_name = 'Deerwalk School'
#     __school_address = 'Sifal'
#     def __init__(self, fn, ln, addr, a):
#         self.__first_name = fn
#         self.__last_name = ln
#         self.__address = addr
#         self.__age = a

    # def get_full_name(self):
    #     return f'{self.__first_name} {self.__last_name}'

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         if new_age < 0:
#             print('invalid age')
#         else:
#             self.__age = new_age


# s = Student('ram', 'hari', 'nepal', 28)
# s.set_age(35)
# print(s.get_age())

# four pillars of OOP
# inheritance
# encapsulation
# abstraction
# polymorphism

# print(1+1)
# print('1' + '1')


# base class/parent class/ super class
# class Employee:  
#     def __init__(self, fn, ln, addr, a):
#         self.first_name = fn
#         self.last_name = ln
#         self.address = addr
#         self.age = a

# class FullTimeEmployee(Employee):
#     pass

# f = FullTimeEmployee('ram', 'hari', 'balaju', 25)
# print(f.first_name, f.last_name, f.address, f.age)




# design a bank class with following properties
    # first name, last name, age , balance = 0, interest_rate = 12
    # get_balance --> returns current balance
    # deposit_balance() --> deposits given amoubt to the current balance
    # withdraw_balance() --> withdraws given amopunt from current balance.
    # get_interest_rate() --> returns the current interest rate
    # set interest rate () --> updates the current interest rate with given rate
    # print government holidays list


# The program should provide the user with following options 
# 1 to open bank account
# 2 to check balance
# 3 to deposit balance
# 4 to withdraw balance
# 5 to check interest rate
# 6 to set interest rate
# 7 to check holidays