# str1="James"
# print(str1[0::2])
# str3 = "JhonDipPeta"
# print(str3[4:7])

# s1 = "Ault"
# s2 = "Keloly"

# # s3=s1[:2]+s2[:]+s1[2:]
# # print(s3)

# # s4=s1[0]+s2[0]+s2[int(len(s1)/2):int(len(s1)/2)+1]
# # print(s4)
# s5=s2[int(len(s2)/2):int(len(s2)/2)+1]
# print(s5)

# xtos={"emma":89,"jane":98,"lily":78}
# # mia=xtos

# mia=dict(xtos)
# mia.update({"emma":45})
# print(mia)
# print(xtos)
# Special Case :

# lin=[1,2,3,4,5]
# # mint=lin
# mint=list(lin)
# mint.append(90)
# print(mint)
# print(lin)



# l1=[1,2,3,4,5,8,7]

# for item in l1:
#   print(item)

# print(l1[0:len(l1)])
# l2 = [3,4,"ram","hari"]
# l1.extend(l2)
# print(l1)


# # ra func ma return pachi ko kei run hudaina .
# def fnd_(a):
#     if a > 5:
#       return True
#     else: 
#        return "no" # yaha else block chaldaina bcze mathi ko return pachi func exit hunxha.
# print(fnd_(4))  how?



# pynative exercise
# qn 1
# no1 = 40
# no2 = 30
# if no1 * no2 <= 1000:
#     print(f"the product is {no1 * no2}.")
# else:
#     print(f"the sum is  {no1 + no2}.")    

# qn 2
# def num_val(s):
#     for n in range(0,s+1,1):
#         print(f"previous no is {n-1}, current no is {n}, sum is {(n-1)+n} ")
# num_val(10)

#qn 3
# inp = input("enter a string")
# idx = 0
# for i in inp:
#     if idx % 2 == 0:
#         print(i)
#     idx = idx+1

# q4
# z = int(input("enter a no"))
# a = "pynative"
# print(a[z:])

#q5 
# lst =[1,2,3,4,6,9]   
# if lst[0] == lst[len(lst)-1]:
#     print("True")
# else:
#     print("False")   

# q6
# lst = [10,31,45,21,1] 
# for item in lst:
#     if item % 5 == 0:
#         print(item)

# q7
# cnt = 0
# str1 = "My name name is Anthony Gunsalvis. The Name is given to me by my fam"
# print(str1.lower().count("name"))

# q8
# for num in range(10):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print("\n")   

# q9
# i = "454"
# if i == i[::-1]:
#     print("yes")
# else:
#     print("false")    

# q10
# l1 =[1,2,3,4,5,6]
# l2 =[8,9,10,11,12]
# l3 =[]
# for item in l1:
#     if item % 2 == 0:
#         l3.append(item)
# for term in l2:
#     if term % 2 != 0:
#         l3.append(term)       
# print(l3)         

# practice from pynative

# func for name and age
# def fun1(a,b):
#     return a+b ,a*b
# print(fun1(20,7))

# def my_name(a,b):
#     print(a+b)
# my_name(50,60)

# yur_name = my_name
# yur_name(50,66)
    
                        
# def evn_no():
#     a = []
#     for i in range(4,30,2):
#         a.append(i)
#     return a 

        
# print(evn_no())
        
# list join in strinf
# l=['nepal']
# m=["ind"]
# a="".join(l+m)
# print(a)

# l1=[3,6,9,12,115,18,21]
# l2=[4,8,12,16,20,24,28]
# l3=[]
# for i in range(0,len(l1)):
#     if i % 2 !=0:
#         l3.append(l1[i])
# for i in range(0,len(l2)):
#         if i%2 ==0:
#              l3.append(l2[i])    
# print(l3)


# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# ch1= sample_list[:int(len(sample_list)/3)]
# ch2=sample_list[int(len(sample_list)/3):int(len(sample_list)/3)+3]
# ch3=sample_list[int(len(sample_list)/3)+3:]

# print(ch1)
# print(ch1[::-1])
# print(ch2)
# print(ch2[::-1])
# print(ch3)
# print(ch3[::-1])
# def cnt(a):
#     dict={}
#     for i in a:
#         c=a.count(i)
#         dict.update({i:c})
#     return dict
# print(cnt([11, 45, 8, 23, 14, 12, 78, 45, 89]))
# l1 =[10,20,3,32,41]
# # print(l1.index(10))
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # print(list1[2][2][1])
# for i,j in zip(l1,list1):
#     print(i,j)




# class Nepal:
#     religion = "hinduism"
#     def __init__(self,nm,ag):
#         self.name = nm
#         self.age = ag
#     def chk(self):
#         print(self.name,self.age,Nepal.religion)
    
#     def on(self):
#         self.name ="Ramwesh"  
   
#     @classmethod
#     def chg(cn,rgn):
#         cn.religion = rgn
         
# a = Nepal("ram",22)
# a.chk()
# a.on()
# a.chk()
# Nepal.chg("muslim")
# a.chk()



# class Bank:
#     bank_name="Deerwalk Development Bank"
#     bank_phone="909784894"
#     bank_headquater="Sifal"
#     def __init__(self,bbn,bbpn,bid):
#         self.branch_address=bbn
#         self.branch_phone_no=bbpn
#         self.branch_id=bid
# a = Bank("gaushala",414141,91)
# print(a.branch_address,a.branch_id,a.branch_phone_no)
# print(Bank.bank_headquater)
# print(Bank.bank_name)
# print(Bank.bank_phone)        
                   

# a,b,c =input('enter fname,lname,age ').split()    
# print(a)              
# print(b)              
# print(c)              
# sup ="nkm"
# for i in sup:
    
#     if "k" == i:
#         print("true")
#         continue
#     else:
        
#         continue   
# print("false")  
# gov_holiday=[1,4,5,6,7]
# def chk_holiday(holiday):
#            for i in gov_holiday:
#                 if holiday == i:
                    
#                     print("Bank Holiday")
#                     break
                    
                
#                 else:
#                     print("no holiday")
#                     break
                    
                    
                    
                         
# chk_holiday(99)         
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


# Print all name which starts with either 'h' or 'h'                       
# name=["harsh","ramesh","shyam","hari","Harry","rita"]
# names=[item for item in  name if item.lower().startswith("h")]
# print(names)
                        
# select only names with i or I in it
# na=["harsh","ramesh","shyam","harI","Harry","rita"]
# naa=[i for i in na if 'i' in i.lower()]
# print(naa)


# select only multiple of five

# num = [i for i in range(1,100) if i%5 ==0]
# print(num)

    

    # Lamda one liner/simple func lai matra use garni.
# all anonymous fun are lamda but all lamda are not anonymous.



# filter func le bool value matra linxhaeg filter(abc) abc need to give boolen(True,False) .
# filter fun lai direct print garna mildaina like print(filter(...))
# we need to convert it to some iterables like list or sothng else.


# map le chai bhako value lai change/edit garna help garxha 
# filter le chai bhako bata choose garna help garxha

# starts with h or H using filter
# name=["harsh","ramesh","shyam","hari","Harry","rita","hannah","RaAr"]
# n =list(filter(lambda x:True if  x.lower().startswith("h") else False ,name))
# print(n)
# change all to capital case.
# print(list(map(lambda x: x.capitalize(),name)))
# change all to upper case.
# print(list(map(lambda x:x.upper(),name)))
# length of each name.
# print(list(map(lambda x:len(x),name)))
# print palindrom disregard case sensitivity.
# print(list(filter(lambda x:True if x[::-1].lower()== x[::].lower()else False,name)))


# price =['$200.00','$500.00','$50.000','63000.00']
# calc mean of above.





a =input("enter a string ")
def chkpal(n):
    if n[:]==n[::-1]:
        return print("Palindrom")
    return print("Not palindrom")
chkpal(a)


!pip
