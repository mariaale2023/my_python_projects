mylist = []

mylist = [1,2,3]

mylist = ["Mouse" , [1,2,3] ] #nested 

mylist = [ "A", " L", "E"]

# print(mylist[2]) #E
print(mylist[ -1]) #E


# add item to the loist with "APPEND"
mylist.append(17)
print(mylist)

print(mylist[1:3])

# dir(mylist)
# # append()	Adds an element at the end of the list
# # clear()	Removes all the elements from the list
# # copy()	Returns a copy of the list
# # count()	Returns the number of elements with the specified value
# # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # index()	Returns the index of the first element with the specified value
# # insert()	Adds an element at the specified position
# # pop()	Removes the element at the specified position
# # remove()	Removes the first item with the specified value
# # reverse()	Reverses the order of the list
# # sort()	Sorts the list
# n = mylist.copy()
# print(n)

# m = mylist.count(10)
# print(m)
# L = mylist.reverse()
# print(L)

for i in mylist:
  print(i)


# If you need both the index and the item, use the enumerate function:
  for index, item in enumerate(mylist):
    print ("The element index is ",index," and the value is ", item)

# If you need only the index, use range and len:

for i in range(len(mylist)):
  print("The element index is ", i)


i = iter(mylist)
item = i.__next__()
print(item)  # fetch first value
print(i)

print("An item in the sample list is ", item)
item = i.__next__() # fetch second value
print("An item in the sample list is ", item)
item = i.__next__() # fetch second value
print("An item in the sample list is ", item)

name_imput = ["Maria","Alejandra","Vasquez", "Ahumada"]
full_name = " ".join(name_imput)
print(full_name, "\n")

my_name = ['H','o','l','a',' ','M','a','r','i', 'a']
print(my_name[:-6])
print(my_name[5:])
print(my_name[:])



#-------------------
print("\n\n")

# import time

# counter_time = True
# seconds = 10
# end = 0

# while (counter_time):
#   print(seconds)
#   time.sleep(0.5)
#   seconds -= 1
#   if( end >= seconds):
#     counter_time = False
#     print(seconds)
# print("The End")

numbers = [1, 2, 3, 4, 5, 5]
tuples = (1, 2, 3, 4, 5, 5)
square_mnumber = [str(element) + "a" for element in numbers]


print(square_mnumber.count("5a"))
print(dir(tuples))
print(dir(numbers))

import sys
print(dir(sys))

print(help(sys.getsizeof))
