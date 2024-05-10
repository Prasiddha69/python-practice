# class and object  oop concept
# class-blueprint of object .it defines how the obj need to be looking like .
# class name always starts from uppercase.
# object -anything that we see through our eyes can be said . also known as instance of a class.
# function defined inside class are refered as method. 
# every class has identity(unique name) state(attribute) and behaviour(method)
# class Student:
#     def __init__(self): # dundun method(double underscore)/magic method. 
#     # init method is compulsary.
#         self.firstname = "Prasiddha"
#         self.lastname = "Pokhareal"
#         self.age = 22
#  # this above class Student has 3 character/property or fields,atttribute ,instance var(firstname,lastname.age)

# # obj creation/instantization.
# a = Student() # here a is reference variable(var pointing obj) and Student() is object 
 # After obj creation init method automatically afai run bhayera mem ma address allocate garxha /obj/var create garxha.           


# class Me:
#     def __init__(self,fn,ln,a):
#         self.fname = fn
#         self.lname = ln
#         self.age = a
# b = Me("Ram","Shrestha",39)# self ma kei pass garnu pardaina . 
# c = Me("Sita","Thapa",28)       

# init method bhaneko constructor in other language.It also detrermines the amount of space req to store the value iin mem.

# self is the ref variable that point to currently running obj in mem.
# The first argument self refers to the current object. mathi ko case ma b,c outside the class.

# accessing  class properties outside the scope of class. 
# print(b.fname,b.lname,b.age) # obj name.propert name
# print(c.fname,c.lname,c.age)

# # del class property.

# # del b.fname
# # print(b.fname,b.lname,b.age)

# # update class property.
# b.fname ="Rio"
# print(b.fname,b.lname,b.age)

# class Cooperate:
#     def __init__(self,fnmae,lname,prof):
#         self.firstname = fnmae
#         self.lastname = lname
#         self.profession = prof

#     def descp(self):
#         print(f"{self.firstname} {self.lastname} is a very honorable {self.profession}.")
# a = Cooperate("Ram","Bhujal","Doctor")
# b = Cooperate("Sita","Rimal","Banker")           
# a.descp()
# b.descp()
       


# instance variables
    # variables whose values depends on objects 
    # represented by self inside the class and by object name outside of the class
    # copy of instance variables is created for every object
# static variables\ class variable
    # variables whose values changes from class to class but for objects of particular class it remains the same.
    # represented by class name both inside and outside of the class
    # copy of static variables is created only once.
# class Student:
#     # class variables(shared by all obj)
#     school_name = 'ABC School'

#     # constructor
#     def __init__(self, name, age):
#         # instance variables (every obj has its own)
#         self.name = name
#         self.age = age

# s1 = Student("Harry", 12)
# # access instance variables
# print('Student:', s1.name, s1.age)

# # access class variable
# print('School name:', Student.school_name)

# # Modify instance variables
# s1.name = 'Jessa'
# s1.age = 14
# print('Student:', s1.name, s1.age)

# # Modify class variables
# Student.school_name = 'XYZ School'
# print('School name:', Student.school_name)


# class ,instance ,static method.
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

# # class methods demo
# class Student:
#     # class variable
#     school_name = 'ABC School'

#     # constructor
#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age

#     # instance method
#     def show(self):
#         # access instance variables and class variables
#         print('Student:', self.name, self.age, Student.school_name)

#     # instance method
#     def change_age(self, new_age):
#         # modify instance variable
#         self.age = new_age

#     # class method
#     @classmethod # decorator nesessary bcze to distinguish btn class and init method
#     def modify_school_name(cls, new_name):
#         # modify class variable
#         cls.school_name = new_name

#     @staticmethod
#     def add():
#         print(1+1)

#     @staticmethod
#     def add_2(i,j):
#         print(i+j)


# s1 = Student("Harry", 12)

# # call instance methods
# s1.show()
# s1.change_age(14)

# # call class method
# Student.modify_school_name('XYZ School')
# # call instance methods
# s1.show()
# call static method 
# Student.add()
# Student.add_2(2,3)

# public variables
    # variables that can be accessed inside and outside of the class
    # by default variables are public 
    # unwanted modification can happen if the variables are public
# class A:
#     def __init__(self,name):
#         self.name=name
# a = A("rama")
# print(a.name)

# private variables(__name)
# variables that can not  be accessed  outside of the class
# unwanted modification cannot  happen outside the class  if the variables are private 
# class A:
#     def __init__(self,name):
#         self.__name=name
# a = A("rama")
# print(a.__name)# access nai garna didaina no attribute bhanxha.

# accessing private variable  outside of class we use getter and setter

# class Mero_Nam:
#     def __init__(self,fn,ln,ag):
#         self.__name=fn
#         self.__last_name=ln
#         self.__age=ag
#     def get_name(self): # getter jasle  private value excess matra garna dinxha and takes parameter self (init var) and cls (for class variable)  only.
#         return self.__name
 # real world ma setter method authorized user le matra use garna pauxha.   
#     def set_name(self,nage): # setter jasle private value change garna dinxha and takes parameter init var self and new value.
#             if nage < 0:
#                 print("invalid input ")
#             else :
#                 self.__age=nage
            
       

# s =Mero_Nam("Prasiidha","Pokharel","22")    
# print(s.get_name())   # calling getter 
# s.set_name(-28) # calling setter
   
# assignmet:


# class Bank:
#     interest_rate = 12
#     gov_holiday = [1,7,13,14,21,25,27]
#     def __init__(self,fn,ln,ag,bal = 0):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = ag
#         self.balance = bal
#     def deposit(self,amt):
#         if amt < 0:
#             print ("invalid amount choosen")
#         else:    
#             self.balance = int(self.balance) +int(amt)  
#             print(f"Current Balance :{self.balance}") 
#     def withdraw(self,w):
#         n = int(self.balance)-int(w)
#         if n < 0:
#             print("insufficient balance to withdraw")
#         else:    
#             print(f"Amount after withdraw:{n}") 
#             self.balance = n  
#     @classmethod
#     def set_interest(cls,interest):
#         print(f"New interest :{interest}%")
#         cls.interest_rate = interest
#     @classmethod
#     def get_interest(cls):
#         print(f"Current interest :{cls.interest_rate}%")
#     @classmethod
#     def chk_holiday(cls,holiday):
#            for i in Bank.gov_holiday:
#                 if holiday == i:
#                     print("Bank Holiday")
#                     break
                
#                 else:
#                     print("No Bank Holiday") 
#                     break   
                              
# b = None
# while 1:
#     a ="""Choose among the Following to proceed:
#     1 to open bank account
#     2 to check balance
#     3 to deposit balance
#     4 to withdraw balance
#     5 to check interest rate
#     6 to set interest rate
#     7 to check holidays
#     """
    
#     print (a)
#     s =int(input("Enter ur choice "))
#     if s ==1:
#         fn,ln,ag=input("enter your firstname,lastname,age ").split()
#         b= Bank(fn,ln,ag)
#         print(f"Welcome {fn.capitalize()} {ln.capitalize()} of age {ag} to our bank. You have successfully created an account")
#     elif s==2 and b is not None:
#         print(f"Balance :{b.balance}")
#     elif s==3 and b is not None:
#         z=int(input("Enter the amount to deposit "))
#         b.deposit(z)
#     elif s==4 and b is not None:
#         p =input("Enter the amount to withdraw ")
#         b.withdraw(p)
        
#     elif s==5:
#         print(f"{Bank.interest_rate}%")
#     elif s==6:
#         x =int(input("Enter the required interest rate to be implemented ")) 
#         Bank.set_interest(x) 
#         Bank.interest_rate = x
#     elif s==7:
#         h =int(input("Enter ur date "))
#         Bank.chk_holiday(h)        
#     elif b is None:
#         print("Create a account first")
#     else:
#         print("Invalid option choosen") 
                        

# Same question making variable private
# class Bank:
#     __interest_rate = 12
#     __gov_holiday = [1,7,13,14,21,25,27]
#     def __init__(self,fn,ln,ag,bal = 0):
#         self.__first_name = fn
#         self.__last_name = ln
#         self.__age = ag
#         self.__balance = bal
#     def gt_balance(self):
#         return(self.__balance)
    
#     def deposit(self,amt):
#         if amt < 0:
#             print ("invalid amount choosen")
#         else:    
#             self.__balance = int(self.__balance) +int(amt)  
#             print(f"Current Balance :{self.__balance}") 
#     def withdraw(self,w):
#         n = int(self.__balance)-int(w)
#         if n < 0:
#             print("insufficient balance to withdraw")
#         else:    
#             print(f"Amount after withdraw:{n}") 
#             self.__balance = n  
#     @classmethod
#     def set_interest(cls,interest):
#         print(f"New interest :{interest}%")
#         cls.__interest_rate = interest
#     @classmethod
#     def get_interest(cls):
#         print(f"Current interest :{cls.__interest_rate}%")
#     @classmethod
#     def chk_holiday(cls,holiday):
#            for i in Bank.__gov_holiday:
#                 if holiday == i:
#                     print("Bank Holiday")
#                     break
                
#                 else:
#                     print("No Bank Holiday") 
#                     break   
                              
# b = None
# while 1:
#     a ="""Choose among the Following to proceed:
#     1 to open bank account
#     2 to check balance
#     3 to deposit balance
#     4 to withdraw balance
#     5 to check interest rate
#     6 to set interest rate
#     7 to check holidays
#     """
    
#     print (a)
#     s =int(input("Enter ur choice "))
#     if s ==1:
#         fn,ln,ag=input("enter your firstname,lastname,age ").split()
#         b= Bank(fn,ln,ag)
#         print(f"Welcome {fn.capitalize()} {ln.capitalize()} of age {ag} to our bank. You have successfully created an account")
#     elif s==2 and b is not None:
#         print(f"Balance :{b.gt_balance()}")
#     elif s==3 and b is not None:
#         z=int(input("Enter the amount to deposit "))
#         b.deposit(z)
#     elif s==4 and b is not None:
#         p =input("Enter the amount to withdraw ")
#         b.withdraw(p)
        
#     elif s==5:
#         print(f"{Bank.interest_rate}%")
#     elif s==6:
#         x =int(input("Enter the required interest rate to be implemented ")) 
#         Bank.set_interest(x) 
        
#     elif s==7:
#         h =int(input("Enter ur date "))
#         Bank.chk_holiday(h)        
#     elif b is None:
#         print("Create a account first")
#     else:
#         print("Invalid option choosen") 
    
# for sir ko soln refer class note OOP_exercise.py




# variance huda pani sd use garnu ko karan sd provides reliable mean of measure.