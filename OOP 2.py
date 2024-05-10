# class Student:
#     __school_name = 'Deerwalk School'
#     __school_address = 'Sifal'
#     def __init__(self, fn, ln, addr, a):
#         self.__first_name = fn
#         self.__last_name = ln
#         self.__address = addr
#         self.__age = a

# p = Student('ramesh', 'dahal', 'balaju', 29)
# print(p.__age)

# types of variables --> instance, static variables

# instance variables
    # variables whose values depends on objects 
    # represented by self inside the class and by object name outside of the class
    # copy of instance variables is created for every object

# static variables
    # variables whose values changes from class to class but for objects of particular class it remains the same.
    # represented by class name both inside and outside of the class
    # copy of static variables is created only once.


# private variables
# public variables
    # variables that can be accessed inside and outside of the class
    # by default variables are public 
    # unwanted modification can happen if the variables are public



# bank name
# bank phone number 123456
# bank headquarter address
# bank branch address
# brank branch phone number
# branch id

class bank:
    bank_name = 'Bro bank'
    bank_phone_number = '123456'
    bank_hq_address = 'Amazing City'
    def __init__(self, bn_addr, bn_ph_num, id):
        self.branch_address = bn_addr
        self.branch_phone_number = bn_ph_num
        self.branch_id = id
        