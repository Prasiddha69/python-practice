# Write a program that takes a number as user input. If the user input is an even number it should print it is an even number else it should print it is an odd number.

# num = int(input('Enter a number '))
# if num % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd.') 



# num = int(input('Enter a number '))
# if num % 2 == 0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd.') 

# Write a program that takes a string as user input and print the name is too long if the string length is greater than 10
# name = input('Enter a name ')
# if len(name) > 10:
#     print('Name is too long')

# Write a program that takes a string and print vowel is present if vowels are present else print vowel is not present.

# user_input = input('Enter a string ').lower()

# if 'a' in user_input or 'e' in user_input or 'i' in user_input or 'o' in user_input or 'u' in user_input:
#     print('Vowel is present')

# Make a calculator
# Enter first number
# Enter second number
# enter operator allowed operators are + - * /

# if user enter - and the difference is negative number, the program should ask wether to print absolute value or not. if y print absolute value else print the negative value

# if division, print greater number divided by smaller number.

 
# first_num = int(input('Enter first number '))
# second_num = int(input('Enter second number '))
# operator = input('Enter an operator ')

# if operator not in ['+', '-', '*' , '/']:
#     print('invalid operator')
# else:
#     if operator == '+':
#         print(f'The sum of {first_num} and {second_num} is {first_num + second_num}')
#     elif operator == '-':
#         value = first_num - second_num
#         if value < 0:
#             absolute_value_choice = input('Do you want to print absolute value').lower()
#             if absolute_value_choice == 'y':
#                 print(f'The difference of {second_num} and {first_num} is {value * -1}')
#             else:
#                 print(f'The difference of {first_num} and {second_num} is {first_num - second_num}')
#         else:
#             print(f'The difference of {first_num} and {second_num} is {first_num - second_num}')
#     elif operator == '*':
#         print(f'The product of {first_num} and {second_num} is {first_num * second_num}')

#     elif operator == '/':
#         division_value = None
#         if first_num > second_num: 
#             division_value = round(first_num /  second_num, 2)
#             print(f'{first_num} divided by {second_num} is {division_value}')
#         else:
#             division_value = round(second_num / first_num, 2)
#             print(f'{second_num} divided by {first_num} is {division_value}')


# student_grade = {'ram': 92, 'shyam': 78, 'hari': 65, 'rita': 45, 'sita': 32, 'gita': 26}

# name = input('Enter your name ').lower()

# if name in student_grade:
#     grade = student_grade[name]

#     if grade >= 80:
#         print(f'Hello {name.capitalize()}. Your garde is {grade}')
#     elif grade >= 60:
#         print(f'Hello {name.capitalize()}. Your garde is {grade}')
#     elif grade >= 50:
#         print(f'Hello {name.capitalize()}. Your garde is {grade}')
#     else:
#         print(f"Mom's flying chappal received at the rate of {grade} km/hr")
# else:
#     print('Name not found.')



# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(2, 10, 2)))

