# is_running = True
 
# while is_running:
#     answer = input("What is the meaning of life?...\n")
#     if answer == "42":
#         print("Correct! Well done!\n")
#         # correct answer, so exit loop - reset is_running
#         is_running = False
#     else:
#         print("Sorry that is the wrong answer.... "
#               "Try again!\n")
 
# x = input("Press any key to exit.")

# ---------------------------------------------------------------------

# number_of_tries = 3

# while True:
#   answer = input("What is the menaing of life..\n")
#   if answer == "Dead":
#     print("Correct")
#     # how the answer is correct, exit the loop with break
#     break 
#   else: 
#     print("Sorry, try again...\n")
#     #number_of_tries = number_of_tries - 1 
#     number_of_tries -= 1

#   #check if number of tries and break if none left
#   if number_of_tries == 0:
#     print("You have run out of goes. sorry")
#     break

# x = input("Press Enter to exit.")


# ---------------------------------------------------------------------

# number_of_tries_names = 3
# name = ""
# while len(name) == 0:
#   name = input("Enter your name: ")
#   number_of_tries_names -= 1
  
#   if number_of_tries_names == 0:
#     print(" You are out of goes. Sorry")
#     if len(name) > 0:
#       print (f"Hello {name}") 

#     break
  
# print("Press Entre to exit the loop")


# ---------------------------------------------------------------------

# Write a program with a while loop that prints 1 through to n in square brackets. 
# For example, if the user enters 6 then the program should display4
# [1] [2] [3] [4] [5] [6]


# number = 0
# new_number = int(input("Insert a number to start the loop..\n"))

# while number < new_number:
#   print("[",number + 1,"] ")
#   number += 1


# ---------------------------------------------------------------------

# Challenge 2
# Write a program with a while loop that computes the sum of the first n positive integers:
# sum = 1 + 2 + 3 + ... + n
# Examples:
# n = 5    sum = 15
# n = 19  sum = 190

# number = int(input("Insert a number to start the sum..\n"))
# sum = 0
# counter = 0 

# while counter <= number:
#   sum = sum + counter
#   counter += 1

# print(f"{sum}")
# print("\nn = ", number, " sum = ",sum,"\n\n")

# ---------------------------------------------------------------------

# p = int(input("Please enter an increment\n\n"))
# q = int(input("Please enter an ending number\n\n"))
# counter = 10
# number = 10
# starting_number = (10 % p) + 10
# while counter < q:
#   print(starting_number,end=", ")
#   starting_number = starting_number + p
#   counter += p

# ---------------------------------------------------------------------

import random

dirty = True
scrub_count = 0


while (dirty):
  scrub_count += 1
  print("Scrub the pan: {}" .format(scrub_count))
  print("Rinse & check if is clean")

  if not random.randint(0,9):
    print("All clean!")
    dirty = False
  else:
    print("Still dirty..")


# ---------------------------------------------------------------------







  

 


 
  



