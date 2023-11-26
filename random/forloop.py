
import random
# user_input = int(input("Please enter the number of times "
#                        "that you wish to see the message."))

# for i in range(user_input):
#     print("hello world....", i)


# ---------

# user_input = int(input("Please enter a number for the size"
#                        "of the shape you wish to create.\n\n\n"))

# for i in range(user_input):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# for i in range(user_input, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# # answer: 10

# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# # * * * * * * 
# # * * * * * * * 
# # * * * * * * * * 
# # * * * * * * * * * 
# # * * * * * * * * * * 
# # * * * * * * * * * 
# # * * * * * * * * 
# # * * * * * * * 
# # * * * * * * 
# # * * * * * 
# # * * * * 
# # * * * 
# # * * 
# # * 

# -----------------------------------

# # time.time(): Returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC). This is often used for measuring elapsed time.

# # time.sleep(seconds): Suspends the execution of the current thread for the specified number of seconds.

# # time.localtime(): Returns the current time as a time.struct_time object, which represents the time in a more structured format (year, month, day, etc.).

# # time.strftime(format, time_struct): Formats a time.struct_time object into a string according to the given format.
# import time

# for second in range (10, 0 , -1):
#   print(second)
#   time.sleep(1)
# print("Happy new Year")

# --------------------------------

# # Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# # Note : Use 'continue' statement.
# # Expected Output : 0 1 2 4 5

# for i in range(6):
#   if (i == 3):
#     continue
#   print (i, end=" ")

# --------------------------------
# # Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# #  x % 7 == 0
# #  x % 5 == 0
# user_imput = int(input("insert a number between 2000 to 5000 \n\n"))
# for i in range (0, user_imput):
#   if (i % 7 == 0 and i % 5 == 0):
#     print(i)



# --------------------------------
# 21. Write a Python program to print the alphabet pattern 'L'.
# Expected Output:

#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****

letter_L=""

for row in range (0 ,7):
  for column in range (0, 7):
    if (( column == 1 ) or (row == 6  and column != 0 and column < 6 )):
      letter_L = letter_L + "*"
    else:
      letter_L= letter_L + " "
  letter_L = letter_L + "\n"
  print(letter_L)
  
  

