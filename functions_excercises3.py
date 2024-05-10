# Write a function that takes a date in the format '1994-05-06' or '1994/05/06'
# and return in the format {'year': '1994', 'month': '05', 'day': '06'}


# Write a function that takes a list of numbers and returns only the even number collection.
# def extract_even_numbers(l):
#     even = []

#     for item in l:
#         if item % 2 == 0:
#             even.append(item)
#     return even


# write a function that takes an email address and check wether that email belongs to gmail or not (must emds with gmail.com)
# def is_gmail(email):
    # if email.lower().endswith('gmail.com'):
    #     return True
    # else:
    #     return False

    # splitted_email = email.split('@')
    # if splitted_email[1].lower() == 'gmail.com':
    #     return True
    # else:
    #     return False


# given names
    # names = ['ram, shyam, hari, rita, sita, gita', 'rythm', 'rrr', 'zzr']
# write a funciton that takes a list of names and separates only the names with vowels in it.
# def find_even_names(l):
#     even_names = []

#     for item in l:
#         if 'a' in item.lower() or 'e' in item.lower() or 'i' in item.lower() or 'o' in item.lower() or 'u' in item.lower():
#             even_names.append(item)
#     return even_names
# print(find_even_names(['ram, shyam, hari, rita, sita, gita', 'rythm', 'rrr', 'zzr']))

# write a program that takes a number input from the user and prints even number upto that number. The program should continuously ask the user for input.

# def find_even_numbers(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             print(i)
#         i = i + 1


# while True:
#     num = int(input('Enter a number '))
#     find_even_numbers(num)


# def find_even_numbers(n):
#     for item in range(0, n+1, 2):
#         print(item)




# Write a function that takes a date in the format '1994-05-06' or '1994/05/06'
# and return in the format {'year': '1994', 'month': '05', 'day': '06'}
# def clean_date(d):
#     splitted_date = None
#     if '-' in d:
#         splitted_date = d.split('-')
#     elif '/' in d:
#         splitted_date = d.split('/')

#     return {'year': splitted_date[0], 'month': splitted_date[1], 'day': splitted_date[2]}

# print(clean_date('1994/05/06'))




# i = 5

# print(i)

# def test():
#     print(i)

# test()


# def test():
#     i = 10
#     print(i)
# test()
# print(i)

# i = 5
# def test():
#     i = 10
#     print(i)

# test()
# print(i)



# salary = 5000

# def increase_salary():
#     global salary
#     salary = salary + 2000 


# increase_salary()
# print(salary)








