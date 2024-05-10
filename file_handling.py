# file handling

# f = open('filename' , 'mode')  read (r), write(w), append(a)

# f = open('valentines.txt', 'r')

# # # reads all the file content.
# # print(f.read())

# # print(f.read(4))
# # print(f.read(5))

# print(f.readline())
# print(f.readline())

# print(f.readlines())

# for line in f.readlines():
#     print(line.strip())

# try:
#     f = open('saraswoti_puja.txt', 'r')
# except FileNotFoundError:
#     print('file name doesnot exist.')
# except:
#     print('an error occured')


# f = open('valentines.txt', 'w')
# f.write('Did you buy chocolates yet?')

# f = open('test.txt', 'w')

# f = open('valentines.txt', 'a')
# f.write('\nYes yes yes!')
# print(f.closed)
# f.close()
# print(f.closed)

# context manager
# with open('valentines.txt', 'r') as f:
#     print(f.read())
#     print(f.closed)

# print(f.closed)