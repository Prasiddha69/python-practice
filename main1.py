# refer pynative and w3schools ,coryshepher.pypi.org for package and module.

#print("Hello World")
#print() displays output

# Python Indentation
# i=1
# if(i>5):
#  print ("i is greater")
# print("ok")

# variable are the name given to the container (it stores value for future reference)
#i = 5
#print(i)



# Rules for naming variable.
# alphanumeric character(a-z,0-9)
# Underscore is allowed
# name can't start with numbers
# name can't be reserved word
# keywoard can't be used.


# Line Continuation in python
# print(10+20+
#       30+40+50+60+70
#      )
# OR
# print(
#     10+\
#     20+\
#     30+\
#     40+\
#     50+\
#     60+70
#      )



# i=10
# print(i)


#in python all uppercase is constant 
# PI=3.14
# PI=5.43
# print(PI)


#p=13
# g=10.55
# b=type(p)
# a=type(g)
# print(a)
# print(b)

#Arthimetic operation"""

# +,-,*,/
# a=2+3
# b=2-1
# c=2*2
# d=3/1
# print(a,b,c,d)
# Division ko ans Float ma usually
#Note: termial ma run garni ho bhane language  filename.extension eg python main.py


# print(100//3)# (//) floor division


"""Logical or nor & and"""
#or and and gate
# print(True and False)
# print(False and False)
# print(True and True)
# print(False and True)

# print(False or False)
# print(False or True)
# print(True or True)
# print(True or False)



# 0,empty string ,None ,{},[],()=False and any thing else is True like num ,string
#  For True 
# print(bool(-6+4j))
# print(bool(-4))
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))
# # For False
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# Precedence
# NOT>>AND>>OR
#  Comparision operator ==,!=,>
#  <
#  >=,<=
# print(True != False == False)
# print(3>=4)
# print(21>=4)
# print(4>=4)
# print(3==4)
#print(True+False)
# if (5==4 or 10!= 5):
#     print("Atleast one is true")
# elseif (5==1):
#      print("Both false")    
# else:
#     print ("Bye")      

# print((True or False)and False or False and(True and False)or True)



#STRINGS ARE BEING TAUGHTED(string are immutable ie changes are occured in instance)

# string_concatination
# first_name="Ramesh"
# last_name="Bro"
# print(first_name + " " +last_name)
# print(first_name,last_name)(bich ma , le j lai ni concatinate garda with space inbuild)
# # datatype defines data type that can be merged.
# a="2"
# b="4"
# print(a+b)
#len()
# Python is Case sensetive and sequence oriented
# x="brother "
# print("bt" in x)
# i="pap"
# j="PAP"
# if(i==j): 
#     print("ok")
# print("no") 

#Membership operator
#not and notin
# upper ,lower,captilize,title, count,repalce,split,strip 
# a=" hey,Hbro"
# print(a.capitalize())
# print(a.title())
# print(a.split(","))
# print(a.strip())
# print(a.count('h')) #count is case sensitive
# a='REY Bro'
# print(a.replace("Bro","Stro"))# yo pani case sensistive

#Formatting a String
# age =27; kind="jolly"
# txt = "My name is John, and I am {}  and am {}"
# print(txt.format(age,kind))[order matters first ma order halenxha then kind]

# Formatting using indexing
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {1} dollars for {0} pieces of item {2}."
# print(myorder.format(quantity, itemno, price))#[order does't matter index wise value are placed]

# differenc btw single ,double and tripple quotation
# print('''Umesh''s class's''')
# a="tamemwl,"
# print(a[3])
# print(a[3:len(a)])
# print(a[-1])
# print(a[0:7:2])
# x="need for speed "
# print(x[0:len(x):3])
# print(x[::])
# print(x[1:4:9])
# print(x[3:])
# for reverse print(x[::-1])


# Printing middle and last char of string
# z=a[int(len(a)/2):int(len(a)/2)+1]
# print(z)
#for last char 
# p=a[len(a)-1] or a[-1]
# print(p)
# for middle 3 char
# str ="rasmkinamdumhum"
# a=int(len(str)/2)
# b=int(len(str)/2)+1  
# r =str[a-1:b+1] 
# print(r)

# to join list content in string.

# use (" ".join(ls1+ls2))
# to display content of 2 or more list ,tuple  at a time.
#  Use the zip() function. 
# This function takes two or more iterables (like list, dict, string),
#  aggregates/add them in a tuple, and returns it.
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x = zip(a, b)
# print(x)

# Escape Character
# d="no\"sir\"we are here" #here \ is not printed
# print(d)


# Assignment 1:

# greeting="hello"
# first_name="umesh"
# last_name="regmi"
# x=greeting.capitalize()
# y=first_name.capitalize()
# z=last_name.capitalize()
# print(x+" "+ y+" " +z)

#or

# greeting="hello"
# first_name="umesh"
# last_name="regmi"
# x=greeting[0].upper()+greeting[1:]
# y=first_name[0].upper()+first_name[1:]
# z=last_name[0].upper()+last_name[1:]
# print(x+" "+y+" "+z)

#or
# import string 
# greeting="hello"
# first_name="umesh"
# last_name="regmi"
# r = string.capwords(greeting)
# s=string.capwords(first_name)
# t=string.capwords(last_name)
# print(r+" "+s+" "+t)
  
  # Class 4
  
# typecasting ,formatted string ,input function.


# casting can be done while defining variable.
# i=int(3.9)
# j=str(0)
# k=bool(8)

#type conversion
# i="5"
# print(float(i))
# print(bool(i))
# print(int(i))
# j=4+3j complex ko type casting not possible

#input function
# var=input("enter name")
# var2=input("enter last name")
# var3=input("enter age")

# taking multiple input in single line
# x,y,z =input("enter the three names ").split()
# print(x)
# print(y)
# print(z)

# print(var)
# print(var2)
# print(var3)
# x=(var[0].upper() + var[1:])
# y=(var2[0].upper() + var2[1:])
# z=(var3[0].upper() + var3[1:])
# print("Hi i am ",x,y,"."," I am currently",z,"years old.")



# first_name = (input("enter first name "))
# last_name = (input("enter last name "))
# age = (int(input("enter your age ")))
# future_age=(age +5)

#  print("Hi" ,first_name.capitalize(),last_name.capitalize(),".You are ",age,"and will be",future_age,"in the next 5 years .")

# + use garera concatinate garda int lai str ma convert garnu parcha natra type mismatch huncha. same kura ,use garera garyau bhane covertion  not required.
# print("Hi"+first_name.capitalize()+last_name.capitalize()+".You are "+str(age)+"and will be"+str(future_age)+"in the next 5 years .")

#  Fstring

# print(f"Hi {first_name.capitalize()} {last_name.capitalize()}.I am {age} years now and will be {future_age} after next five year.")
# #Or
# vat="Hi {} {}.I am {} years now and will be {} after next five year."
# print(vat.format(first_name.capitalize(),last_name.capitalize(),age,future_age))

#LIST ,Tuple,Dictonary, Set 

# p=['ram', 'shyam', 'hari'] 
# #z=['ram''shyam''hari']
# r={"name":'ram',"age" :'shyam',"gender":'hari'}
# q=("hari" ,"shyam")

#s=("hari:"'sun'"shyam:"'mon')
# p.remove("ram") if aautai kura duble xha bhani first wala lai remove garxha.
# p.pop() by default last index gayo. tara if pop(2) 2 index ko particularly hataunxha.
# print(p+z)

# Note   remember 
# l1=[1,2,3,4,5,6]
# l2=l1.append(9)
# print(l1) 
# print(l2) #yesko ans none aauxha . 


# del p garyo bhani list nai udxha and clear p garyo bhani content matra udxha.

# sort() le sadhai assending ,reverse() le tyo list ulto bata(last element first ma ) not decending 
# decending ko lagi p.sort(reverse=True)
# by default sort are case sensitive . For case insensitive sort 
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# by default sort le none return garxha.so 
# a=["a","e","i","b","c"]
# print(a.sort()) #(none aauxha instead )
# a.sort()
# print(a)

# List,tuple,set are hetrogeneous
# a list,tuple,set containig different datatype envolved. a[1.1,1,True,"ram"]
# both tuple and list are indexed and ordered , list mutable(changable original mai change hunxha unlike string  )
# Note set are unordered and doesn't contain duplicate unlike list,no slicing
# t={"ram","gita","mia","sara"}
# z=t.update(["woo"])
# #z and r are different"""
# r=t.update("woo")#error update only dict tyo pani with key value within {}.
# # print(z)
# # print(t)
# print(z)
# print(type(p))
# print(type(q))
# print(type(r))
# print(type(s))
 # char of dict 
# hetrogeneous ,mutable,and if a key value is repeted the later one replaces the first one.
# z={"ram":34,"shyam":22,"ram":45}
# if a key is not availabe it adds the key  z=["ramesh"]=34,print(z)
# print(z.get("shyam"))
# print(z.keys())
# print(z.values())
# print(z.items())


# Nesting in dict
# a={"name":"ram","age":22,"city":{"zone":"bagmati","district":"ktm"}}
# print(a["city"]["zone"])



# to append
# p=['ram', 'shyam', 'hari'] 
# r={"name":'ram',"age" :'shyam',"gender":'hari'}


# p.append("rama") #append le sadhai last ma halxha so we can't provide index using append.
# p.insert(1,"rama")
# print(p)

# r.update({"name":""})# r being dict.
# print(r)

#
#print(p)

#tuple with single value is always treated as char with it
# a=(1)
# print(type(a)) this is not tuple , try print("1",)comma is imp.


# tuple unpacking
# i,j,k=(1,2,3)
# print(i)
# print(j)
# print(k)


# (l,*m,n,)=(1,2,3,4,5,6,7,8,9,)
# print(l)
# print(m)
# print(n)
# p=(1,2,3,4,4,5,6)
# print(p.count(4))

# extend() method le list ma j ni jod dinxha ra yo muni ko case ma thislist ma add garxha.
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# Note list ma no add function, tuple ma no append,add or insert as tuple are immutable.set ma no append(no last ,first ) ,insert hudaina ,add matra huxha because non indexed. 
# Replacing a string from list ,tupple 
#set ma no pop but only remove because no indexing ani we can also use discard jasle if no element error faldaina unlike remove .
#p[0]="Shyam"
# print(p)

# More on sets. set can't be changed but element can only be add or substract not edited.
# a={1,2,3,4,5,6,7}
# b={5,6,7,8,9}
# print(a.difference(b))
# print(a.union(b))
# print(a.intersection(b))
# print(b.difference(a))

#type conversion any list,tuple ,set to any among these three tara set ma lagda index ra order can be changed or gone.

"""replace string in dict"""
# r['name']="Sila"
# print(r)
'''LENGHT OF STRING,tuple ,list '''
# x=" we are nepali by birth"
# print(len(x))
#print(x[0:6])
"""Indexing ko lagi"""
#print(x[0])
"""range ko lagi
"""
#print(x[0:3])

# Using range function 
# for i in range(10, 15, 1):
#   print( i, end=', ') 15 include hudaina . ra range func ma we can't use float.


'"White space remove'''
#print(x.strip())
"""To  replace a text """
#print(x.replace("w",'n'))
"""Very Very important ."""
# xtos={"emma":89,"jane":98,"lily":78}
# mia=xtos# original mai change like view 

# # mia=dict(xtos)# orgi ma no change like copy 
# mia.update({"emma":45})
# print(mia)
# print(xtos)

# Dict ko value diyera key nikalni tarika.Not feasible for common case.

# Assignment 2
# names = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita']
# find total number of students present today.
# print(len(names))
# check if ram is present diregarding case sensitivity.
# print('RAM'.lower() in names)
# remove gita from the list.
# print(names.remove('gita'))
# add nita to the second position
# print(names.insert(1, 'nita'))
# remove the third student from the list
# print(names.pop(2))  #del names[2]
# access/print the last name in the list. suppose you don't know the last index value.
# print(names[len(names)-1])



# Assignment 3


# ('ram', 'shyam', 'hari')-->   (ram, shyam, rita, hari)

# tup=("ram","shyam","hari")
# asap=list(tup)
# asap.insert(2,"rita")
# turp=tuple(asap)
# print(turp)

# ['ram', 'ramesh', 'ram', 'ramesh', 'sita', 'rita', 'ram'] count unique char in this list.

# z=["ram","ramesh","ram","ramesh","sita","rita","ram"]
# wee=set(z)
# x=list(wee)
# print(x)
# print(len(x))

# Assignment 4
# user bata name input linu (case insensitive ) ani teslai correspoding grade sanga print.
# name_dict={"ram":32,"shyam":85,"hari":25,"rita":30}
# inp_ask=input("enter ur req name ").lower()
# print(f"Hi {inp_ask.capitalize()}.Your grade is {name_dict[inp_ask]}")


# if and else condition.
# if 2>3: 
#     print("true")
# elif 3>4:
#     print("false")        
# else:
#     print("no case")


# if 2>3:
#     print("true")
# if 3>2:
#     print("false")        
# else:
#     print("no case")

# if 5>3:
#     pass
# else:
#     print("no case")

# fn = input("enter a name ")
# age = int(input("enter the age "))

# if fn == "Prasiddha":
#     if age >30:
#         print("Bro budo bhayau")
#     elif age > 22 and age < 25:  
#         print("Bro thikai raixhau")
#     else:
#         print("Kam xhaina bacha raixhau")    
# else:
#     print("ke hawa jasto name diyeko hau")        


# Short end if and else
# a=3 ;b=5
# print("Wrong") if a>b else print("this is right ")

# a=user_name % 2==0





# Assignment 5

# Write a program that takes a number as user input. If the user input is an even number it should print it is an even number else it should print it is an odd number.
# user_num=int(input("Enter ur desired no "))

# if (user_num % 2 ==0):
#     print("The no is even.")
# else:
#     print("The no is odd.")    

            # or
# user_num=int(input("Enter ur desired no "))
# if (user_num % 2 ==0):
#     print(f"{user_num} is even." )
# else:
#     print(f"{user_num} is odd.")    
# Same question for loop lagayera.
# user_num=input("Enter ur desired no ")
# for no in user_num:
#     raw=int(user_num)
#     if raw % 2 == 0:
#         print(" no is even")
#         break
#     else:
#         print("no is odd")   
#         break 


# Write a program that takes a string as user input and print the name is too long if the string length is greater than 10

# user_inp=input("enter the name ")
# if (len(user_inp) > 10):
#     print(f"{user_inp }, your name is too long.")
# else:
#     print(user_inp)    
   


# Write a program that takes a string and print vowel is present if vowels are present else print vowel is not present.

# user_input=input("Enter the string ").lower()
# if "a" in user_input or "e" in user_input or "i" in user_input or "o"in user_input or "u" in  user_input :
#   print("present")
# else:
#    print("Vowel not present")  
  
# user_input=input("Enter the string ").lower()
# vowels="aeiou"
# for no in user_input:
#     if no in vowels:
#         print("present")
#         break
#     else:
#        print("not present")
#        break    # break lako karan repetadely  print na hos bhanera.natra loop break na bhayera repeated hunxha.
    
# Make a calculator
# Enter first number
# Enter second number
# enter operator allowed operators are + - * /

# if user enter - and the difference is negative number, the program should ask wether to print absolute value or not. if y print absolute value else print the negative value

# if division, print greater number divided by smaller number.
                 
        
        
# a=int(input("enter first no "))
# b=int(input("enter second no "))
# operator=["+","-","*","/"]
# c=input("enter ur desired operator ")
# if c not in  operator:
#      print("choose appropriate operator ") 
# else:
#       if c == "+":
#            print(a+b)
#       elif c == "-":
#         if(a-b) < 0:
#           ask=input("print absolute or not ")
#           if ask.lower() == "yes":
#             print(abs(a-b))
#           else:
#              print(a-b)
#         else:
#            print(a-b)         
#       elif c =="*":
#          print(a*b)  
#       else:
#          v=a/b
#          if v>1:
#            print(round(v,2))
#          else:
#             print(round((1/v),2))
            
 

      
       


# Take a dict{"ram":92,"shyam":78,"hari":65,"rita":45,"sita":32,"gita":26}.provide message acc to grades obtained. and show error if student not in dict is asked about.

# user_grade={"ram":92,"shyam":78,"hari":65,"rita":45,"sita":32,"gita":26}
# inp_user=input("enter name ").lower()
# if inp_user in user_grade:
#     if user_grade[inp_user] >= 50 :
#       print(f"HI {inp_user.capitalize()}.You got satisfactory mark  of  {user_grade[inp_user]}.")
#     elif user_grade[inp_user] >= 60 :
#       print(f"HI {inp_user.capitalize()}.You got pass mark  of  {user_grade[inp_user]}.")  
#     elif user_grade[inp_user] >= 80:
#       print(f"HI {inp_user.capitalize()}.You got good  mark  of  {user_grade[inp_user]}.")  
#     else:
#       print(f"Mom's flying chappal received at {user_grade[inp_user]}km/hr. ")   
# else:
#   print("Details of the name not found")       


# None datatype.
# value taha na bhako variable which we will deal in future. used for space efficiency in professional practice.

# While loop

# i = 0
# while i < 5:
#     print("Hello World")
#     i = i + 1

# names= ["ram","shyam","har","rita","sita"]
# i = 0
# while i<5:
#     print(names[i])
#     if i == 4:
#       break
#     i = i + 2
    



# user_grade={"ram":92,"shyam":78,"hari":65,"rita":45,"sita":32,"gita":26}


# user_grade={"ram":92,"shyam":78,"hari":65,"rita":45,"sita":32,"gita":26}
# while True:
#   inp_user = input("enter name ").lower()
#   if inp_user in user_grade:
#           if user_grade[inp_user] >= 50 :
#             print(f"HI {inp_user.capitalize()}.You got satisfactory mark  of  {user_grade[inp_user]}.")
#           elif user_grade[inp_user] >= 60 :
#             print(f"HI {inp_user.capitalize()}.You got pass mark  of  {user_grade[inp_user]}.")  
#           elif user_grade[inp_user] >= 80:
#             print(f"HI {inp_user.capitalize()}.You got good  mark  of  {user_grade[inp_user]}.")  
#           else:
#             print(f"Mom's flying chappal received at {user_grade[inp_user]}km/hr. ")   
#   else:
#         print("Details of the name not found") 


# For loop: infinite loop ma jadaina. bcze last index ma gayera aafai stop hunxha

# item=["ram","shyam","hari"]
# for variable in item:
#     print(variable)

# for name in item:
#     print(name)



# dict={"ram":34,"shyam":56,"hari":54}
# for name in dict.values():
#     print(name)


# dict={"ram":34,"shyam":56,"hari":54}
# for name in dict.items():
#     print(name)

# dict={"ram":34,"shyam":56,"hari":54}
# for k,v in dict.items():
#     print(k,v)    

# Class Practice 

names = ['ram', 'shyam', 'hari', 'rita']

# 1.  print the length of each name
# for item in name:
#     print(len(item))
# 2. print each name in capitalized letter.
# for item in name:
#     print(item.capitalize())
# print capitalized name with index.
# the value at 0 index is ram
# the value at 1 index is shyam
# for item in range(len(names)):
#      print(f" the value at  {item}  is {names[item]}") #yaha item bhaneko numeric val xha.
# print the first two names only
# for item in range(2):
#     print(name[item])
    
# check wether hari exist in the list or not using loop. disregard case sensitivity.
# name =["ram","shyam","hari","sita","gita"]

# for item in name:
#     if item.lower() =="hari":
#         print(f"{item} found")
        
    
            
# print no from 2 to 20 even no:
# for item in range(2,20,2):
#    print(item) 

# for item in range(2,10):
#     if item % 2 == 0:
#         print(item)
               

# continue in loop



# for no in range(1,20):
#     if no % 2 == 0:
       
#         continue
#     print(no)


# nested for loop
# namew=[[1,2,3,4],[63,45,67,87],[98,78,65]]
# for item in namew:
#     for val in item:
#         print(val)



# Functions in python.
# collection of statements that perform a specific task.


# def function_name():  # function declaration or defination.
#     pass
# function_name()  function call or invoke  and this is necessary. and funct can't be called before it is defined.

# def add():
#     print(2+2)
# add()    

# arguments/parameter --> extra info provided to function to process. 

# def add (i,j): # i,j are parameters and are used to define func
#     print(i +j)
# add(1,2)   # 1,2 are arguments  are used when we call func. 

# function ma parameter ra arguments ko positing/order in which given  are imp natra order mismatch.
# To solve order mismatch we use keyword args.

# def info(fn,ln,age,addr,country):
#     print(f"Hello {fn} {ln}.You are {age} years old and live in {addr} {country}.")
# info(ln="Pokharel",fn="Prasiddha",country="nepal",addr="jayabageshwori",age=22)    

# default args  yaha balance (yesko value argument ma overwrite garena bhane parameter ma j cha tei hunxha.)
# def info(fn,ln,age,addr,country,balance=0 ):
#     print(f"Hello {fn} {ln}.You are {age} years old and live in {addr} {country}. You have bank balance of {balance}")
# info(ln="Pokharel",fn="Prasiddha",country="nepal",addr="jayabageshwori",age=22) 

# note 
# def fun(name,age):
#     print(name,age)
# fun(name="ram",23)# yo error ho bcze position arg first then only key fun("emma",age=23)

# def ma(name,age,sex):
#     print(name,age,sex)
# ma(age=23,name="ram",sex="m")    

# variable/ multiple length args ra yo positional hunxha ie position matters.

# def add(*args):
#     print(sum(args))
# add(-2,1,3)   
# add()
# add(1)  yesle tupple ma store garxha


# multiple length keyword args(kwargs)

# def add(**kwargs):
#     print(kwargs)

# add(i=2,j=1)
# add(i=1,j=2,k=3)  
# add (i=1)  # yesle generally dict ma store garxha.


# return in func
# Note if print matra garnu xha bhani function def bhitrai  print garnu natra return garera aru kam bhahira garnu .  industry  standard  anusar a function should perform one task at a time .

# def mean(i,j):
#     avg=(i+j)/2
#     return avg
# val=mean(12000,45000) # return le jaha call garyo tei return hunxha. in this case mean yaha call bhako xha
# if (val>3000):
#     print("rich")
# else:
#    print("broke")    

# func call matra garna chahi return not needed.
# def fnd_(a):
#     if a > 5:
#         print("ok")
# fnd_(7)     
    

# if func def ma aru kei kam garera  bahira use/call garyo bhani none dinxha.yesko lagi exclusively return needed.

# def mean(i,j):
#     avg=(i+j)/2
   
# val=mean(12000,45000) # yo case ma none aauxha bcze func mean le none return gareko xha .
# print(val)
# # ra func ma return pachi ko kei run hudaina .
# def fnd_(a):
#     if a > 5:
#       return True
#     else: 
#        return "no" # yaha else block chaldaina bcze mathi ko return pachi func exit hunxha.
# print(fnd_(4)) 

#Below is the function display_student(name, age). 
# Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name, age):
#     print(name, age)
# # call using original name
# display_student("Emma", 26)
# # assign new name
# showStudent = display_student
# # call using new name
# showStudent("Emma", 26)


# Assignment
# a func that takes a string and return  len of the  string.

# def calc_len(a):
#     return(len(a))
# print(calc_len("Prasiddha")) 
    

# a func that takes a string and return last alphabet of  the string.

# def lst_alpha(a):
#     return a[-1]
# print(lst_alpha("Prasiddha"))    

# a func that takes string and return reverse of it.
# def revStr(a):
#     return(a[::-1])      
# rev=revStr("Prasiddha") 
# print(rev)

# a func that takes string and returns true if vowles present else false.

# def chk_vow(string):
#    if "a" in string or "e" in string or "i" in string or "o" in string or "u" in string:
#     return True
#    return False  

# print(chk_vow("Prtp"))
 

# funct that  take list of no and return sum of the list.

# def lst_sum(a):
#     return sum(a)
    
# tot=lst_sum([1,2,3,4,5,6])
# print(tot)


# func to take list of num and return mean of those no.
   # yo case ma func reuse gareko xah 
# def lst_sum(a):
#     return sum(a)

# def lst_mean(b):
#     z=lst_sum(b)
#     return (z /len(b))
# print(lst_mean([1,2,3,4,5,6]))


# func to take a num and  return true if no even else false for odd.

# def num_chk(a):
#      if a % 2 == 0:
#          return True
#      else:
#          return False

# print(num_chk(99))


# func to take a num and return true if no divisible by both 10 and 5 else false.  

# def chk_num(a):
#      if a % 5 == 0 and a % 10 == 0:
#           return True
#      return False
# val = chk_num(698)
# print(val)



# func to take string and check palindrom or not disregarding case sensitivity.


# def is_palindrom(a):
#     if a.lower() == a[::-1].lower():
#         print(" True Palindrom")
#     else:
#         print("False  Palindrom") # yaha print use gare pachi display gardiyo ani function ko kam over tara if tala kai use garni ho bhani return garnu. 
   
# is_palindrom("hanNaH") # yo case ma print garni ho bhani return garnai parxha natra none aauxha.

                

# func to take a string and return first vowel in the string.


# def frst_vwel(string):
#     vowels = "aeiou"
#     for char in string:
#         if char.lower() in vowels:
#             return char
          
# print(frst_vwel("Prasiddha"))    

# func to take a string and return first consonent in the string.

# def fst_consonent(a):
#     vowel="aeiou"
#     for item in a:
#         if item.lower() not in vowel:
#             return item
# print(fst_consonent("Rama"))        
            
# if same thing return hoina  print garnu pare ma.

# def frst_cnsont(string):
#     vowel="aeiou"
#     for char in string:
#         if char .lower()  not in vowel:
#             print(f"{char} is the first consonent")
#             break
# frst_cnsont("Prasiddha")                
    
# function that takes string and return total no of vowels present in it

# def vowl_count(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string:
#         if char.lower() in vowels:
#            count +=1
#     return count       

# print(vowl_count("nepali"))                

# func to take string and return no of conconant present in it.        
# def consnt_count(string):
#     consonant = "bcdfghjklmnpqrstvwzyz"
#     count = 0
#     for char in string:
#         if char.lower() in consonent:
#            count +=1
#     return count       

# print(consnt_count("Prasiddha")) 

# func to take string and return total no of vowel and consonent present in dict format.
# def vowl_count(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string:
#         if char.lower() in vowels:
#            count +=1
#     return count  
# def consnt_count(string):
#     consonant = "bcdfghjklmnpqrstvwzyz"
#     count = 0
#     for char in string:
#         if char.lower() in consonent:
#            count +=1
#     return count        
# def tot_item(string):
#     z=vowl_count(string) 
#     x=consnt_count(string)   
#     return dict(vowel=z,consonent=x)       

# print(tot_item("Prasiddha")) 

# func that take  a string  and returns occurance of u in it.
# def u_count(a):
#     count = 0
#     for item in a:
#         if "u" in item:
#             count+=1
#     return count
# print(u_count("Umesh sir in Uruguay"))  

# func that take a string and returns total occurance of u and U present in it asa a dict. 
# def u_count(a):
#     count = 0
#     for item in a:
#         if "u" in item:
#             count += 1
#     return count     
# def U_count(a):
#     count = 0
#     for item in a:
#         if "U" in item:
#             count += 1
#     return count
# def _count(a):
#     w = u_count(a)
#     v = U_count(a)
#     return dict(u=w,U=v) 
# print(_count("Umesh sir in urugUay"))


  #OR 
# def count_vowels_and_consonants(s):
#     vowels = "aeiou"
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     vowel_count = 0
#     consonant_count = 0
#     for char in s:
#         if char.lower() in vowels:
#             vowel_count += 1
#         elif char.lower() in consonants:
#             consonant_count += 1
#     return {"vowels": vowel_count, "consonants": consonant_count}

# s = input("Enter a string: ")
# result = count_vowels_and_consonants(s)
# print(result)

# func that take a string and calc total no of u present in the string disregarding case sensitivity.
# def chk_u(a):
#     count = 0
#     for item in a:
#         if "u" in item.lower():
#             count+=1
#     return count
# print(chk_u("umesh sir in UrugUay")) 


# Write a function that takes a date in the format '1994-05-06' or '1994/05/06'
# and return in the format {'year': '1994', 'month': '05', 'day': '06'}

# def _date(s):
#   new_date = None
#   for item in s:
#       if "-" in item:
#         new_date = s.split("-")
        
#       elif "/" in item:
#          new_date = s.split("/")
#   return {"year":new_date[0],"month":new_date[1],"day":new_date[2]}
# print(_date("1994-05-06"))

# Write a function that takes a list of numbers and returns only the even number collection.

# def _only_even(s):
#     coll =[]
#     for item in s:
#        if  item % 2 == 0:
#           coll.append(item)
#     return coll
# print(_only_even([1,2,3,4,5,6,7]))    
        
# write a function that takes an email address and check wether that email belongs to gmail or not (must emds with gmail.com)

# def take_email(s):
#     p = s.split("@")
#     if p[1].lower() == "gmail.com":
#         print("gmail")
#     else:
#        print("Not gmail")
# take_email('pprasid.1234@gmail.com')  

# Or 
# def email(em):
#     if em.endswith('gmail.com'):
#         return True
#     else:
#         return False
# print(email("hello.google@hotmail.com"))      

# given names
    # names = 'ram, shyam, hari, rita, sita, gita'. print it in list .


# def _name_list(n):
#     a = n.split(",")
#     print(list(a))
# _name_list("ram,shyam,hari,rita,sita,gita")    


# write a funciton that takes a list of names and separates only the names with vowels in it.

# def _list_names(l):
#     vowels="aeiou"
#     z=[]
#     for item in l:
#         for term in item:
#             if term in vowels:
#                 z.append(item)
#                 break
#     return z            
# print(_list_names(["dz","saugat","sishir","lyzm","hri"]))   


# write a program that takes a number input from the user and prints even number upto that number. The program should continuously ask the user for input.

# def only_evn(s):
#       for item in range(0,s+1,2):
#         print(item)
# while True:
#   inp=int(input("enter the no "))              
#   only_evn(inp)
            
 
# Scope of Variable in function
# global variable jasko scope through out the program.

# x = 5
# def fun1():
#     print(x)
 
# fun1()
# print(x)                   

# local variable jasko scope only within the program
# def fun2():
#     x = 5
#     print(x)
# fun2()
# print(x) #error aauxha   


# to change global variable within the function
# x = 69
# def fun3():
#     x=x+1
#     print(x)
# fun3()#in this case error as x is treated as local var so can't  be used without declared . 
  
# x = 69
# def fun3():
#     global x
#     x=x+1
#     print(x)  
# fun3()
# print(x)    

# i = 5
# def test():
#     i =10
#     print(i)

# test()# i = 5 
# print(i)# i = 10



# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne in listTwo) #explained carefully.

# a = "ram"
# b = "ram"
# print(a in b)
# print(a is b)



 