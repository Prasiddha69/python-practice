# string list tuple set dictionary --> iterables

# names = ['ram', 'shyam', 'hari', 'rita', 'sita']

# for name in names:
#     print(name)

# for a in 'ramesh':
#     print(a)

grade = {'ram': 35, 'shyam': 82, 'hari': 55, 'rita': 40}
# for item in grade:
#     print(item)
# for item in grade.values():
#     print(item)

# for k, v in grade.items():
#     print(k, v)


# for item in range(1, 10):
#     print(item)

# given,
    # names = ['ram', 'shyam', 'hari', 'rita']
    # 1.  print the length of each name
    # 2. print each name in capitalized letter.
    # print capitalized name with index.
        # the value at 0 index is ram
        # the value at 1 index is shyam
    # print the first two names only
    
    # check wether hari exist in the list or not using loop. disregard case sensitivity.

names = ['ram', 'shyam', 'hari', 'rita']
# for name in names:
#     print(len(name))

# for name in names:
#     print(name.capitalize())

# for index in range(len(names)):
#     print(f'The value at {index} index is {names[index]}')

# i = 0
# while i < 2:
#     print(names[i])
#     i = i + 1

# for index in range(2):
#     print(names[index])

names = ['ram', 'shyam', 'hari', 'rita', 'sita', 'gita', 'nita']

# for item in names:
#     if item.lower() == 'hari':
#         print('found')
#         break

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# for no in numbers:
#     if no % 2 == 0:
#         continue
#         print(no)
#     else:
#         print(no)


# l = [[1,2,3], [4,5,6], [7,8,9]]
# for item in l:
#     for val in item:
#         print(val)

# for item in range(2, 21):
#     if item % 2 == 0:
#         print(item)

# for item in range(2, 21, 2):
#     print(item)


# a = [1,2,3,4,5,6,7,8,9,10]
# print(max(a))
# print(min(a))

i=input("enter ur name")
print(i)