import math

def  show_hello():
  print("Hello, this is a first fiunction \n\n")
print("testing mu fisrts defines function \n\n")


# invoking function
show_hello()
# invoking function again
show_hello()


# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

dir(math)
print( math.pi)

def triangle_area(a, b):
  return 0.5 * a * b

print(triangle_area(3, 6))
print("\n\n")

def cm(feet = 0,  inches = 0):
  inches_to_cm = inches * 2.54
  feet_to_cm = feet * 12 * 2.54
  return inches_to_cm + feet_to_cm
print(cm(5,8))
print(cm(feet= 5 , inches = 8))
print(cm(inches = 8, feet= 5)) # if write to the order way
print(cm(feet = 5))
print(cm(inches = 70 ))

print("\n\n")
print("---------------------")


def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))

counter = 0
print("Testing my second user defined function...\n\n")
counter += 1

show_hello(counter)

print("---------------------")
first_number = 6
second_number = 4

def show_difference(number_1, number_2):
  print("Fisrt number is {0}.\n"
        "second number is {1}.\n"
        "The differnce between them is {2}".format(number_1, number_2, (number_1 - number_2)))

# print(show_difference(first_number, second_number))
show_difference(first_number, second_number)
print("\n")

show_difference(13, 2)


print("---------------------")
print("SCOPE")

 
# score = 3
# def show_new_score():
#   score = score  + 1
#   print(score)

# show_new_score()

# print(score)

print("---------Other option------------")

# score = 3
# def show_new_score(parameter):
#   parameter = parameter  + 1
#   print("thi is parameter equal to {0}".format(parameter))
#   return parameter

# score = show_new_score(parameter)


# score = 4
 
# def get_new_score(param_score):
#     param_score += 1
#     print("You got another point...\n"
#           "Your score is now {0}.\n"
#           .format(param_score))
#     return param_score
# # some run code
# x = int(input("insert a number"))
# # invoking the function and using it to set the new score
# score = x + get_new_score(score)
# score = x + get_new_score(score)
# score = x + get_new_score(score)

print("---------------------")
name = "Maria"

def show_name():
  name = "Ale"
  print(name)

print(show_name())
show_name()
print(name)

print("---------------------")

def show_age(age):
  print('Myage 10 year ago was {0} \n'
  .format(age - 10))
  

show_age(30)

print("---------------------")
def show_young_age(my_age, my_name):
    print("My age 10 years ago was {0}.\n"
          "My name is {1}."
          .format(my_age - 10, my_name))
 
# invoking function
show_young_age(22, "Tuheitia")

print("---------------------")

# Remember that functions have their own scope. Variables declared in a function only have scope in the function block.
def example_function():
    # Variable 'local_var' is declared within the function's scope
    local_var = 42
    print("Inside the function: local_var =", local_var)

# Call the function
example_function()

# Try to access 'local_var' outside the function (this will result in an error)
# Uncommenting the line below will raise a NameError
# print("Outside the function: local_var =", local_var)

print("---------------------")

#String

string_1 = "Wuaaauuu!!!"
print("The third letter of string_1 is {0}\n".format(string_1[2]))
print("The length of string_1 is {0}\n".format(len(string_1)))
print("The letter 'u' appears {0} times\n".format(string_1.count("u")))

string_2 = "here is a translation: Haera mai ki konei means come here!"

konei_endindex = string_2.find("konei")
print(konei_endindex)
# konei_endindex = string_1.find("konei") + len("konei")
# print("The end index position of konei is {0}\n"
#       .format(konei_endindex))


here_position = string_2.find("here", konei_endindex, len(string_2))
print("Looking for the string_2 here, anytime after konei...\n\n"
      "The string_2 here appears at index position..{0}"
      .format(here_position))

print("---------------------")
string_3 = "Ka mate kāinga tahi ka ora kāinga rua."
 
print("Does this string start with Ka?....{0}\n".format(string_3.startswith("Ka")))
 
print("Does this string start with Tr?....{0}\n".format(string_3.startswith("Tr")))
 
print("Does this string end with rua?....{0}\n".format(string_3.endswith("rua.")))

print(string_3.isalnum())    #check if all char are alphanumeric 
print(string_3.isalpha())         #check if all char in the string are alphabetic
print(string_3.isdigit())         #test if string contains digits
print(string_3.istitle())         #test if string contains title words
print(string_3.isupper())         #test if string contains upper case
print(string_3.islower())         #test if string contains lower case
print(string_3.isspace())         #test if string contains spaces
 
print("---------------------")

string_4 = "Hello World"
 
# replacing part of a string
print("Replacing part of a string...\n{0}"
      .format(string_4.replace("Hello", "Goodbye")),
      "\n")

      #Changing Upper and Lower Case Strings
string_upper_Case = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_upper_Case.upper()),
      "\n")

string_lower_Case = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_lower_Case.lower()),
      "\n")

print("Making a string title case...\n{0}"
      .format(string_4.title()),
      "\n")

print("Making a string capitalised...\n{0}"
      .format(string_4.capitalize()),
      "\n")
  
print("Making a string swap case...\n{0}"
      .format(string_4.swapcase()),
      "\n")

print("Reversing and inserting characters to a string...\n{0}"
      .format(" ".join(reversed(string_4))))

print("---------------------\n")

original_string = "Hello, World!"
reversed_iterator = reversed(original_string)

# Convert the reversed iterator back to a string
reversed_string = ''.join(reversed_iterator)

print("Original string:", original_string)
print("Reversed string:", reversed_iterator)
print("Reversed string:", reversed_string)


print("---------------------\n")

string_6 = "It's only after we've lost everything " \
           "that we're free to do anything\n"
print(string_6)


# splitting the string
print("Splitting the string...\n{0}"
      .format(string_6.split()),
      "\n")
 
# splitting the string on the letter e
print("Splitting the string on the letter e...\n{0}"
      .format(string_6.split("e")),
      "\n")