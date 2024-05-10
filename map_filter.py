# list comprehension

# it creates a new list from an existing list.

a = list(range(50))

# even = []
# for item in a:
#         if item % 2 == 0:
#                 even.append(item)

# print(even)

# even = [item for item in a if item % 2 == 0]

# given, 
        # names = ['harsh', 'ramesh', 'shyam', 'hari', 'Harry', 'rita']
        # select only names that starts with h or H


names = ['harsh', 'ramesh', 'shyam', 'hari', 'Harry', 'rita']
# new_names = []
# for name in names:
#         if name.lower().startswith('h'):
#                 new_names.append(name)

# new_names = [name for name in names if name.lower().startswith('h')]

# given,
# names = ['harsh', 'ramesh', 'shyam', 'hari', 'harry', 'rita']
        # select only names that has i or I in it

# names = ['harsh', 'ramesh', 'shyam', 'hari', 'harry', 'rita']
# names = [name for name in names if 'i' in name.lower()]

# given,
        # range(100), select only even numbers that are multiple of 5
# num = [n for n in range(100) if n % 2 == 0 and n % 5 == 0]
# print(num)


# given, 
        # names = ['harsh', 'ramesh', 'shyam', 'hari', 'harry', 'rita']

        # capitalize the first letter 

# names = ['harsh', 'ramesh', 'shyam', 'hari', 'harry', 'rita']
# new_names = [name.capitalize() for name in names]


# lambda function/ anonymous function

# def square_it(n):
#         return n ** 2

# s = lambda n: n ** 2

# print(s(2))

# a = lambda x,y: x + y

# print(a(2,3))

# def is_even(n):
#         return True if n% 2==0 else False

# num = [1,2,3,4,5,6,7,8,9,10]

# print(list(filter(is_even, num)))

# print(list(filter(lambda x: True if x % 2 == 0 else False, [1,2,3,4,5,6,7,8,9,10])))

# num = [1,2,3,4,5,6,7,8,9,10]
# even = [n for n in num if n % 2 == 0]

# num = [1,2,3,4,5,6,7,8,9,10]

# print(list(map(lambda x : x ** 2, num)))

# new_num = [n**2 for n in num]
# print(new_num)


# [1,2,3,4,5,6,7,8,9,10]
# [2,4,6,8,10]


names = ['harsh', 'ramesh', 'shyam', 'hari', 'harry', 'rita', 'Hannah', 'hannah']
# select only the names that starts with h 
print(list(filter(lambda x: True if x.lower().startswith('h') else False, names)))

# change the name to all capitalize
print(list(map(lambda x: x.capitalize(), names)))

# change all name to upper case
print(list(map(lambda x: x.upper(), names)))

# get the length of each name 
print(list(map(lambda x: len(x), names)))

# select all the names that are palindrome disregarding case sensitivity 
print(list(filter(lambda name: True if name.lower() == name.lower()[::-1] else False, names)))


# price = ['$200,000', '$500,000', '$50,000', '62,000']
# # calculate mean of the above price list

# def clean_price(p):
#         a = p.replace('$', '').replace(',', '')
#         return int(a)


# clean_price_list = list(map(clean_price, price))
# print(sum(clean_price_list) / len(clean_price_list))

