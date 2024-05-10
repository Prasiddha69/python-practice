# thislist = ['apple', 'banana', 'cherry', 'mango', 'orange']

# thislist[1:3] = ['avocado', 'kiwi']# index 1 ra 2 ko content change.

# print(thislist)

# tuple 
# a = ()
# b = tuple()

# print(type(a))
# print(type(b))

days_in_week = ('sun', 'mon', 'tues', 'wed', 'thurs', 'frid', 'sat')

# heterogenous
# a = (1, 1.1, True, 'ram')
# print(a)

# indexed/ordered
# print(days_in_week[0])
# print(days_in_week[-1])


# immutable


# print(len(days_in_week))
# print('sun' in days_in_week)


days_in_week = ('sun', 'mon', 'tues', 'wed', 'thurs', 'frid', 'sat')
# del days_in_week[0]
# print(days_in_week)

# a = (1,2,3)
# b = (4,5,6)
# print(a+b)

# a = ('1',)
# print(type(a))

# print(days_in_week.count('sun'))

# i = (1,2,3,4)

# i,j,k = (1,2,3)
# print(i)
# print(j)
# print(k)

# a = set()
# print(type(a))

# a = {1,2,3,4,4,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,6,6}
# print(a)# duplicate value remove and no order of display

# a = {1,2,'ramesh', True}# bool value lai ignore garxha.
# print(a)


# names = {'ramesh', 'ram', 'shyam', 'hari', 'rita'}
# print(names)

# mutable


names = {'ramesh', 'ram', 'shyam', 'hari', 'rita'}
# names.add('rama')
# print(names)

# names.remove('ramesh')
# print(names)

# names.discard('umesh')
# print(names)

# a = {1,2,3,4,5,6,7}
# b = {5,6,7,8,9,10,11,12}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))

# a = (1,2,3,4)
# print(list(a))
# print(set(a))

# a = [1,2,3,4]
# print(tuple(a))
# print(set(a))


# I have a tuple of names 
    # ('ram', 'shyam', 'hari')   (ram, shyam, rita, hari)

# ['ram', 'ramesh', 'ram', 'ramesh', 'sita', 'rita', 'ram']

# names = ('ram', 'shyam', 'hari')
# temp = list(names)
# temp.insert(2, 'rita')
# names = tuple(temp)
# print(names)

# print(len(set(['ram', 'ramesh', 'ram', 'ramesh', 'sita', 'rita', 'ram'])))

# names = ['ram', 'ramesh', 'ram', 'ramesh', 'sita', 'rita', 'ram']
# unique_name = set(names)
# print(len(unique_name))