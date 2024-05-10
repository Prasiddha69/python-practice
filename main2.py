# any no to octa or hexa
# n = 32
# print("%o"%n)# octave 
# print("%hx"%n)#hexa

# error handling.
# syntatical error
# runtime error


# try catch/except finally.

# try:
#     fn= input("enter the first name ")
#     ln= input("enter the last name ")  # risky code try ma 
#     print((fn/ln))
# except:
#     print("error occured") # error aayo bhani try block ma ani  matra except run hunxha 
# else:
#     print("smooth running of code") # error xhaina bhani try ma ani matra run.       

# finally:
#     print("j hos crash bhayena ")  # always run hunxha.



# file handling(jun mode ma kholyo tei mode ma kam garni)



# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# while excessing the path of file we need to start with r""
# f =open(r"/Users/prasiddha/Desktop/python/valentines.txt","w")
# print(f.write("hello")) # because tyo path ko / ko meaning pre define xha python ma.

# f = open("valentines.txt","r")

# reads all the file content.
# print(f.read())

# print(f.read(4))# read specific term in index 4 ra yo case ma ordering 1 dheki not o


# print(f.read(4))# yo case ma duitai combine hunxha.4 place samma ani then next line  ma next 5 index ko word.
# print(f.read(5))

# print(f.readline())# pura first line 
# print(f.readline())# pura first line and sec line
# print(f.readline(4))# first line ko 4 index samma ko

# for line in f.readlines():
#     print(line.strip())  # spaces haru sab harauxha


# f = open("valentines.txt", "r")
# for x in f:
#   print(x)


# f = open("valentines.txt","w")
# print(f.write("4"))# write le chai previous kura lai overwrite garxha

# f =open("valentines.txt","a")
# print(f.write("4"))# append le pahila ko ma add garxha

# file open garera kam sakepachi u need to close that file.
# f = open('valentines.txt', 'a')
# f.write('\nYes yes yes!')
# print(f.closed)
# f.close()
# print(f.closed)

# manually file close garnu bhanda use context manager 
# context manager
# with open('valentines.txt', 'r') as f:
#     print(f.read())
#     print(f.closed)

# print(f.closed)

# to delete a file

# import os
# os.remove("valentines.txt")


# importing packages. first install package  using pip install "package name",for example  
# pip install Django,pip install pywhatkit
# import webbrowser
# webbrowser.open("https://www.youtube.com/results?search_query=young+dumb+and+broke")






