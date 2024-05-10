class Student:
    def __init__(self, fn, ln, a):  # dunder method/ magic method
        self.first_name = fn
        self.last_name = ln
        self.age = a
    
a = Student('umesh', 'regmi', 29)
b = Student('ramesh', 'dahal', 24)

# access properties outside of the class
# print(a.first_name, a.last_name, a.age)
# print(b.first_name, b.last_name, b.age)

# del
# del a.first_name
# print(a.first_name)

# update 
a.first_name = 'rama'
print(a.first_name, a.last_name, a.age)



